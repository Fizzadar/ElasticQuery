# ElasticQuery
# File: tests/test_api.py
# Desc: test full query output from ElasticQuery

from unittest import TestCase

from elasticquery import ElasticQuery, Query, Filter, Aggregate
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

    def test_just_filter(self):
        q = ElasticQuery()
        q.filter(Filter.terms('field', ['list', 'of', 'terms']))

        assert_equal(self, q.dict(), {
            'query': {
                'filtered': {
                    'filter': {
                        'terms': {
                            'field': ['list', 'of', 'terms']
                        }
                    }
                }
            }
        })

    def test_filter_and_query(self):
        q = ElasticQuery()
        q.filter(Filter.term('field', 'term'))
        q.query(Query.prefix('field', 'prefix'))

        assert_equal(self, q.dict(), {
            'query': {
                'filtered': {
                    'filter': {
                        'term': {
                            'field': 'term'
                        }
                    },
                    'query': {
                        'prefix': {
                            'field': 'prefix'
                        }
                    }
                }
            }
        })

    def test_aggregate(self):
        q = ElasticQuery()
        q.aggregate(Aggregate.terms('agg_name', 'field'))

        assert_equal(self, q.dict(), {
            'aggregates': {
                'agg_name': {
                    'terms': {
                        'field': 'field'
                    }
                }
            }
        })

    def test_filter_query_and_aggregate(self):
        q = ElasticQuery()
        q.filter(Filter.missing('field'))
        q.query(Query.match('field', 'query'))
        q.aggregate(Aggregate.max('agg_name', 'field'))

        assert_equal(self, q.dict(), {
            'query': {
                'filtered': {
                    'filter': {
                        'missing': {
                            'field': 'field'
                        }
                    },
                    'query': {
                        'match': {
                            'field': {
                                'query': 'query'
                            }
                        }
                    }
                }
            },
            'aggregates': {
                'agg_name': {
                    'max': {
                        'field': 'field'
                    }
                }
            }
        })
