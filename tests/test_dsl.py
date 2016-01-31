# ElasticQuery
# File: tests/test_dsl.py
# Desc: tests for ElasticQuery DSL objects (Filter, Query, Aggregate)

from os import path
from unittest import TestCase

from jsontest import JsonTest

from elasticquery import Query, Aggregate, Suggester
from elasticquery.exceptions import (
    NoQueryError, NoAggregateError, NoSuggesterError,
    MissingArgError
)
from .util import assert_equal

CLASS_NAMES = {
    '_query': Query
}


def _test_query(self, query, test_name, test_data):
    method = getattr(query, test_name)

    def parse_arg(arg):
        if isinstance(arg, list):
            return [parse_arg(a) for a in arg]
        else:
            return (
                CLASS_NAMES[arg](arg, {})
                if (isinstance(arg, basestring) and arg.startswith('_'))
                else arg
            )

    args = test_data.get('args', [])
    args = parse_arg(args)

    kwargs = test_data.get('kwargs', {})
    kwargs = {
        k: parse_arg(v) if isinstance(v, list) else parse_arg(v)
        for k, v in kwargs.iteritems()
    }

    output = method(*args, **kwargs).dict()
    assert_equal(self, output, test_data['output'])


class TestQueries(TestCase):
    __metaclass__ = JsonTest

    jsontest_files = path.join('tests', 'queries')
    jsontest_function = lambda self, test_name, test_data: (
        _test_query(self, Query, test_name, test_data)
    )


class TestAggregates(TestCase):
    __metaclass__ = JsonTest

    jsontest_files = path.join('tests', 'aggregates')
    jsontest_function = lambda self, test_name, test_data: (
        _test_query(self, Aggregate, test_name, test_data)
    )


class TestSuggesters(TestCase):
    __metaclass__ = JsonTest

    jsontest_files = path.join('tests', 'suggesters')
    jsontest_function = lambda self, test_name, test_data: (
        _test_query(self, Suggester, test_name, test_data)
    )


class TestFails(TestCase):
    def test_no_query(self):
        with self.assertRaises(NoQueryError):
            Query.doesnotexist()

    def test_no_aggregate(self):
        with self.assertRaises(NoAggregateError):
            Aggregate.doesnotexist()

    def test_no_suggester(self):
        with self.assertRaises(NoSuggesterError):
            Suggester.doesnotexist()

    def test_missing_arg(self):
        with self.assertRaises(MissingArgError):
            Query.term(None)

    def test_invalid_arg(self):
        # Test passing not a list
        with self.assertRaises(ValueError):
            Query.bool(must=set())

        # And now an invalid list
        with self.assertRaises(ValueError):
            Query.bool(must=[None])

        # And now an invalid list
        with self.assertRaises(ValueError):
            Query.bool(must=[Aggregate.terms('test', 'test')])

        # And now an invalid list
        with self.assertRaises(ValueError):
            Query.range('field', gte=['error'])

        # Empty list should be OK/ignored
        Query.bool(must=[])
