# ElasticQuery
# File: tests/test_api.py
# Desc: test full query output from ElasticQuery

from datetime import datetime
from unittest import TestCase

from elasticquery import ElasticQuery, Query, Aggregate, Suggester
from elasticquery.elasticquery import _json_date

from .util import assert_equal


class FakeElasticSearch(object):
    def search(*args, **kwargs):
        return 'FakeElasticSearch'


class TestJsonDate(TestCase):
    def test_json_date(self):
        self.assertEqual(
            _json_date(datetime(2016, 01, 01, 0, 0, 0)),
            '2016-01-01T00:00:00'
        )

    def test_json_date_fail(self):
        with self.assertRaises(TypeError):
            _json_date(None)


class TestElasticQuery(TestCase):
    def test_misc(self):
        q = ElasticQuery()
        q.size(10)
        q.from_(50)
        q.timeout('60s')
        q.set('key', 'value')
        q.fields(('one_field', 'two_field'))

        assert_equal(self, q.dict(), {
            'size': 10,
            'from': 50,
            'timeout': '60s',
            'key': 'value',
            '_source': ['one_field', 'two_field']
        })

    def test_sort(self):
        q = ElasticQuery()
        q.sort('sort_field')

        assert_equal(self, q.dict(), {
            'sort': ['sort_field']
        })

    def test_sort_order(self):
        q = ElasticQuery()
        q.sort('sort_field', order='desc')

        assert_equal(self, q.dict(), {
            'sort': [{
                'sort_field': {
                    'order': 'desc'
                }
            }]
        })

    def test_just_query(self):
        q = ElasticQuery()
        q.query(Query.query_string('this is a querystring'))

        assert_equal(self, q.dict(), {
            'query': {
                'query_string': {
                    'query': 'this is a querystring'
                }
            }
        })

    def test_aggregate(self):
        q = ElasticQuery()
        q.aggregate(Aggregate.terms('agg_name', 'field'))

        assert_equal(self, q.dict(), {
            'aggregations': {
                'agg_name': {
                    'terms': {
                        'field': 'field'
                    }
                }
            }
        })

    def test_nested_aggregate(self):
        q = ElasticQuery()
        q.aggregate(Aggregate.terms('agg_name', 'field').aggregate(
            Aggregate.sum('sub_agg_name', 'sub_field')
        ))

        assert_equal(self, q.dict(), {
            'aggregations': {
                'agg_name': {
                    'terms': {
                        'field': 'field'
                    },
                    'aggregations': {
                        'sub_agg_name': {
                            'sum': {
                                'field': 'sub_field'
                            }
                        }
                    }
                }
            }
        })

    def test_suggester(self):
        q = ElasticQuery()
        q.suggest(Suggester.term('sugg_name', 'term text', 'term_field'))

        assert_equal(self, q.dict(), {
            'suggest': {
                'sugg_name': {
                    'text': 'term text',
                    'term': {
                        'field': 'term_field'
                    }
                }
            }
        })

    def test_query_aggregate_and_suggester(self):
        q = ElasticQuery()
        q.query(Query.match('field', 'query'))
        q.aggregate(Aggregate.max('agg_name', 'field'))
        q.suggest(Suggester.term('sugg_name', 'term text', 'term_field'))

        assert_equal(self, q.dict(), {
            'query': {
                'match': {
                    'field': {
                        'query': 'query'
                    }
                }
            },
            'aggregations': {
                'agg_name': {
                    'max': {
                        'field': 'field'
                    }
                }
            },
            'suggest': {
                'sugg_name': {
                    'text': 'term text',
                    'term': {
                        'field': 'term_field'
                    }
                }
            }
        })

    def test_get(self):
        # Test no ES
        q = ElasticQuery()
        with self.assertRaises(ValueError):
            q.get()

        # Test no index
        q = ElasticQuery(es=FakeElasticSearch())
        with self.assertRaises(ValueError):
            q.get()

        # Test no index
        q = ElasticQuery(es=FakeElasticSearch(), index='')
        with self.assertRaises(ValueError):
            q.get()

        # Test working
        q = ElasticQuery(es=FakeElasticSearch(), index='', doc_type='')
        self.assertEqual(q.get(), 'FakeElasticSearch')
