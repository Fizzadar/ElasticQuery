# ElasticQuery
# File: elasticquery/util.py
# Desc: utility functions for converting args/kwargs to Elasticsearch DSL

from .exception import InvalidArg


def _check_type(key, expected_type, arg):
    if isinstance(expected_type, basestring):
        if arg._eq_type != expected_type[1:]:
            raise InvalidArg('{} should be a {}'.format(key, expected_type[1:].title()))

    elif not isinstance(arg, expected_type):
        raise InvalidArg('{} should be a list of {}'.format(key, expected_type))

def _check_arg(key, expected_type, arg):
    if isinstance(expected_type, list):
        if not isinstance(arg, list):
            raise InvalidArg('{} should be a list'.format(key))

        if expected_type:
            for arg in arg:
                _check_type(key, expected_type[0], arg)

    elif expected_type is not None:
        _check_type(key, expected_type, arg)

    else:
        if isinstance(arg, dict) or isinstance(arg, list):
            raise InvalidArg('{} should be a string or integer'.format(key))

def _parse_args(args, argspec):
    struct = {}
    arg_length = len(args)

    for i, (key, expected_type) in enumerate(argspec):
        if i <= arg_length:
            _check_arg(key, expected_type, args[i])
            struct[key] = args[i]

    return struct

def _parse_kwargs(kwargs, kwargspec):
    struct = {}

    for (key, expected_type) in kwargspec:
        if key in kwargs:
            _check_arg(key, expected_type, kwargs[key])
            struct[key] = kwargs.pop(key)

    return struct

def make_struct(definition, *args, **kwargs):
    '''Generates a Filter or Query object based on it's definition and the input arguments.'''
    # Single type
    if isinstance(definition, basestring):
        _check_arg('', definition, args[0])
        struct = args[0]

    # List type (compound and/or filters)
    elif isinstance(definition, list):
        _check_arg('', definition, list(args))
        struct = args

    # Kwarg type
    else:
        struct = {}

        # Field type ({field: {args}})
        if definition.get('field'):
            if definition.get('value'):
                field_struct = _parse_args(args[1:], definition.get('args', {}))['_value']
            else:
                field_struct = {}
                field_struct.update(_parse_args(args[1:], definition.get('args', {})))
                field_struct.update(_parse_kwargs(kwargs, definition.get('kwargs', {})))

            if 'field_process' in definition:
                field_struct = definition['field_process'](field_struct)

            struct[args[0]] = field_struct

        # Normal type ({args})
        else:
            struct.update(_parse_args(args, definition.get('args', {})))
            struct.update(_parse_kwargs(kwargs, definition.get('kwargs', {})))

        # Always update with remaining kwargs
        struct.update(kwargs)

    if 'process' in definition:
        struct = definition['process'](struct)

    return struct


def unroll_struct(struct):
    '''Converts nested Filter and Query objects into nested dicts.'''
    if type(struct) in (list, tuple):
        return [unroll_struct(v) for v in struct]
    elif isinstance(struct, dict):
        return {k: unroll_struct(v) for k, v in struct.iteritems()}
    elif getattr(struct, '_eq_type', None):
        return unroll_struct(struct.dict())
    else:
        return struct


def _unroll_spec(spec):
    out_spec = []

    for arg in spec:
        if isinstance(arg, dict):
            for key, expected_type in arg.iteritems():
                if isinstance(key, tuple):
                    for sub_key in key:
                        out_spec.append((sub_key, expected_type))
                else:
                    out_spec.append((key, expected_type))
        else:
            out_spec.append((arg, None))

    return out_spec

def unroll_definitions(definitions):
    '''Unrolls definitions ensuring all arg/kwarg specs are tuples of (key, expected_type).'''
    for key, spec in definitions.iteritems():
        if isinstance(spec, dict):
            for arg_type in ['args', 'kwargs']:
                if arg_type in spec:
                    spec[arg_type] = _unroll_spec(spec[arg_type])
