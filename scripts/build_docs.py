#!/usr/bin/env python

# ElasticQuery
# File: scripts/build_docs.py
# Desc: quick hack to auto-generate Markdown from the DSL definitions

from elasticquery.aggregates import AGGREGATES
from elasticquery.filters import FILTERS
from elasticquery.queries import QUERIES

STRING_TO_CLASS = {
    '_query': 'Query',
    '_filter': 'Filter'
}


def arg_to_string(arg):
    if isinstance(arg, list):
        if not arg:
            return '[]'

        if isinstance(arg[0], basestring):
            return '[{0}]'.format(STRING_TO_CLASS[arg[0]])

    if isinstance(arg, basestring):
        if arg in STRING_TO_CLASS:
            return STRING_TO_CLASS[arg]

    return str(arg)

def make_args_string(argspec, cls_name):
    if isinstance(argspec, basestring):
        return STRING_TO_CLASS[argspec]

    if isinstance(argspec, list):
        return '[{0}]'.format(STRING_TO_CLASS[argspec[0]])

    args = kwargs = None

    if 'args' in argspec:
        args = [
            arg[0] if arg[1] is None else arg_to_string(arg[1])
            for arg in argspec['args']
        ]

        if argspec.get('field'):
            args.insert(0, 'field')

        if cls_name == 'Aggregate':
            args.insert(0, 'name')

        args = ', '.join(args)

    if 'kwargs' in argspec:
        kwargs = []

        for kwarg in argspec['kwargs']:
            if isinstance(kwarg[0], tuple):
                for subarg in kwarg[0]:
                    kwargs.append('{0}={1}'.format(subarg, arg_to_string(kwarg[1])))
            else:
                kwargs.append('{0}={1}'.format(kwarg[0], arg_to_string(kwarg[1])))

        kwargs = ', '.join(kwargs)

    if args and kwargs:
        return '{0}, {1}'.format(args, kwargs)

    if args:
        return args

    if kwargs:
        return kwargs


def build_dsl_docs(definitions, title, cls_name, target_file):
    out = '# ElasticQuery {0} API\n'.format(title)

    for key, argspec in definitions.iteritems():
        args_string = make_args_string(argspec, cls_name)
        out = '{0}\n### `{1}.{2}({3})`\n'.format(out, cls_name, key, args_string)

    f = open(target_file, 'w')
    f.write(out)
    f.close()


build_dsl_docs(AGGREGATES, 'Aggregates', 'Aggregate', 'docs/aggregates.md')
build_dsl_docs(FILTERS, 'Filters', 'Filter', 'docs/filters.md')
build_dsl_docs(QUERIES, 'Queries', 'Query', 'docs/queries.md')

print 'Docs built!'
