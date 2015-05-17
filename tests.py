from os import path
from unittest import TestCase

from jsontest import JsonTest
from dictdiffer import diff as dictdiff

from elasticquery import Filter, Query


def _test_filterquery(self, filterquery, test_name, test_data):
    method = getattr(filterquery, test_name)

    args = test_data.get('args', [])
    kwargs = test_data.get('kwargs', {})

    output = method(*args, **kwargs).dict()
    try:
        self.assertEqual(output[test_name], test_data['output'])
    except AssertionError as e:
        print 'OUTPUT', output[test_name]
        print 'EXPECTED', test_data['output']

        diff = list(dictdiff(output[test_name], test_data['output']))
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
