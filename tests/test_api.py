# ElasticQuery
# File: tests/test_api.py
# Desc: test full query output from ElasticQuery

from unittest import TestCase

from elasticquery import ElasticQuery, Query, Aggregate
from .util import assert_equal


class TestElasticQuery(TestCase):
    def test_misc(self):
        q = ElasticQuery()
        q.size(10)
        q.from_(50)
        q.timeout('60s')

        assert_equal(self, q.dict(), {
            'size': 10,
            'from': 50,
            'timeout': '60s'
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

    def test_query_and_aggregate(self):
        q = ElasticQuery()
        q.query(Query.match('field', 'query'))
        q.aggregate(Aggregate.max('agg_name', 'field'))

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
            }
        })
