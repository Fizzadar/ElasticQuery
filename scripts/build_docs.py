#!/usr/bin/env python

# ElasticQuery
# File: scripts/build_docs.py
# Desc: quick hack to auto-generate Markdown from the DSL definitions

from elasticquery.aggregates import AGGREGATES
from elasticquery.filters import FILTERS
from elasticquery.queries import QUERIES
from elasticquery.suggesters import SUGGESTERS

STRING_TO_CLASS = {
    '_query': 'Query',
    '_filter': 'Filter'
}


def arg_to_string(arg, field=None):
    if isinstance(arg, list):
        if not arg:
            if field:
                return '[{0}]'.format(field)
            else:
                return '[]'

        if isinstance(arg[0], basestring):
            if arg[0] not in STRING_TO_CLASS:
                return '[{0}]'.format(field)

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

    args = [
        arg[0] if arg[1] is None else arg_to_string(arg[1], field=arg[0])
        for arg in argspec.get('args', [])
    ]

    if argspec.get('field'):
        args.insert(0, 'field')

    if cls_name == 'Aggregate':
        args.insert(0, 'name')

    if args:
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


def gen_title_underline(char, string):
    return ''.join(char for _ in xrange(0, len(string)))


def build_dsl_docs(definitions, title, cls_name, target_file):
    title = '{0} API'.format(title)
    out = '{0}\n{1}\n'.format(title, gen_title_underline('=', title))

    out += '''
Note that all {1} calls can also be passed additional keyword arguments not specified here, but no validation of inputs is done on them.

'''.format(title, cls_name)

    out += '\n\n'

    for key, argspec in definitions.iteritems():
        args_string = make_args_string(argspec, cls_name)

        title_key = key
        if key.endswith('_'):
            title_key = '{0}\_'.format(key[:-1])

        method_title = '{0}.{1}'.format(cls_name, title_key)
        out += '\n{0}\n{1}\n'.format(method_title, gen_title_underline('~', method_title))

        out += '''
.. code:: python

    {0}.{1}({2})

'''.format(cls_name, key, args_string)

    f = open(target_file, 'w')
    f.write(out)
    f.close()


build_dsl_docs(AGGREGATES, 'Aggregates', 'Aggregate', 'docs/aggregates.md')
build_dsl_docs(FILTERS, 'Filters', 'Filter', 'docs/filters.md')
build_dsl_docs(QUERIES, 'Queries', 'Query', 'docs/queries.md')
build_dsl_docs(SUGGESTERS, 'Suggesters', 'Suggester', 'docs/suggesters.md')

print 'Docs built!'
