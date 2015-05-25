from os import path
from unittest import TestCase

from jsontest import JsonTest
from dictdiffer import diff as dictdiff

from elasticquery import Filter, Query, Aggregate

CLASS_NAMES = {
    "_filter": Filter,
    "_query": Query
}


def _test_filterquery(self, filterquery, test_name, test_data):
    method = getattr(filterquery, test_name)

    def parse_arg(arg):
        if isinstance(arg, list):
            return [parse_arg(a) for a in arg]
        else:
            return CLASS_NAMES[arg](arg, {}) if (isinstance(arg, basestring) and arg.startswith('_')) else arg

    args = test_data.get('args', [])
    args = parse_arg(args)

    kwargs = test_data.get('kwargs', {})
    kwargs = {
        k: parse_arg(v) if isinstance(v, list) else parse_arg(v)
        for k, v in kwargs.iteritems()
    }

    output = method(*args, **kwargs).dict()

    try:
        self.assertEqual(output, test_data['output'])
    except AssertionError as e:
        print 'OUTPUT', output
        print 'EXPECTED', test_data['output']

        diff = list(dictdiff(output, test_data['output']))
        for d in diff:
            print d

        raise e


class TestFilters(TestCase):
    __metaclass__ = JsonTest

    jsontest_files = path.join('tests', 'filters')
    jsontest_function = lambda self, test_name, test_data: (
        _test_filterquery(self, Filter, test_name, test_data)
    )

class TestQueries(TestCase):
    __metaclass__ = JsonTest

    jsontest_files = path.join('tests', 'queries')
    jsontest_function = lambda self, test_name, test_data: (
        _test_filterquery(self, Query, test_name, test_data)
    )

class TestAggregates(TestCase):
    __metaclass__ = JsonTest

    jsontest_files = path.join('tests', 'aggregates')
    jsontest_function = lambda self, test_name, test_data: (
        _test_filterquery(self, Aggregate, test_name, test_data)
    )
