#!/usr/bin/env python

# ElasticQuery testing
# This is not thorough and doesn't have 100% coverage
#
# Throughout we define some test structures/queries, tested against ES
# Source: http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/index.html
#
# Common names:
# value         = value_name1, value_name2, ...
# field         = field_name1, field_name2, ...
# number low    = 0
# number high   = 100
# lucene query  = QUERYSTRING

import sys
import json

from elasticquery import ElasticQuery, Filter, Query, Aggregate


# Some horrible helper functions
test_count = {'count': 1}


def error(message):
    print '\t[{0}] Error: {1}\n'.format(test_count['count'], message)
    sys.exit(1)


def success(message):
    print '\t[{0}] Success: {1}'.format(test_count['count'], message)


def test(name, got, want):
    if got != want:
        print 'want: {0}'.format(json.dumps(want))
        print 'got: {0}'.format(json.dumps(got))
        error('{0} fail'.format(name))
    else:
        success('{0}'.format(name))

    test_count['count'] += 1

print '\n[ElasticQuery] Begin tests!'

# Filters/Queries:
FILTERS = {
    'RANGE': {
        'range': {
            'field_name1': {
                'gt': 0,
                'lte': 100
            }
        }
    },
    'PREFIX': {
        'prefix': {
            'field_name1': 'value_name1'
        }
    },
    'TERM': {
        'term': {
            'field_name1': 'value_name1'
        }
    },
    'FILTER_TERMS': {
        'terms': {
            'field_name1': ['value_name1', 'value_name2'],
            'execution': 'bool'
        }
    },
    'QUERY_TERMS': {
        'terms': {
            'field_name1': ['value_name1', 'value_name2'],
        }
    },
    'FILTER_MISSING': {
        'missing': {
            'field': 'field_name1'
        }
    },
    'QUERY_MISSING': {
        'filtered': {
            'filter': {
                'missing': {
                    'field': 'field_name1'
                }
            }
        }
    },
    'RAW_FILTER_STRING': {
        'query': {
            'query_string': {
                'query': 'QUERYSTRING',
                'default_operator': 'AND'
            }
        }
    },
    'RAW_QUERY_STRING': {
        'query_string': {
            'query': 'QUERYSTRING',
            'default_operator': 'AND'
        }
    },
    'FILTER_STRING': {
        'query': {
            'query_string': {
                'query': 'field_name1:value_name1 AND (field_name2:((value_name2) OR (value_name3)))',
                'default_operator': 'AND'
            }
        }
    },
    'QUERY_STRING': {
        'query_string': {
            'query': 'field_name1:value_name1 AND (field_name2:((value_name2) OR (value_name3)))',
            'default_operator': 'AND'
        }
    },
    'NESTED_FILTER': {
        'nested': {
            'path': 'nested_path',
            'filter': {
                'bool': {
                    'must': [{
                        'term': {
                            'field_name1': 'value_name1'
                        }
                    }],
                    'should': [],
                    'must_not': []
                }
            }
        }
    },
    'QUERY_FILTERED': {
        'filtered': {
            'filter': {
                'match_all': {}
            },
            'query': {
                'match_all': {}
            }
        }
    },
    'QUERY_FUZZY_LIKE_THIS': {
        'fuzzy_like_this': {
            'fields': ['name', 'foo'],
            'like_text': 'test fuzzy'
        }
    },
    'QUERY_MULTI_MATCH': {
        'multi_match': {
            'fields': ['name', 'foo'],
            'type': 'cross_fields',
            'query': 'multi match',
        }
    },
    'FILTER_BOOL': {
        'bool': {
            'must': [
                {
                    'term': {
                        'field_name1': 'value_name1'
                    }
                }
            ],
            'should': [
                {
                    'term': {
                        'field_name3': 'value_name3'
                    }
                }
            ],
            'must_not': [
                {
                    'term': {
                        'field_name2': 'value_name2'
                    }
                }
            ],
            '_cache': True
        }
    },
}

# Test filters
print '[ElasticQuery] Testing: filters & queries'

query = Filter.range('field_name1', gt=0, lte=100)[2]
test('Filter.range', query, FILTERS['RANGE'])
query = Query.range('field_name1', gt=0, lte=100)[2]
test('Query.range', query, FILTERS['RANGE'])

query = Filter.prefix(field_name1='value_name1')[2]
test('Filter.prefix', query, FILTERS['PREFIX'])
query = Query.prefix(field_name1='value_name1')[2]
test('Query.prefix', query, FILTERS['PREFIX'])

query = Filter.term(field_name1='value_name1')[2]
test('Filter.term', query, FILTERS['TERM'])
query = Query.term(field_name1='value_name1')[2]
test('Query.term', query, FILTERS['TERM'])

query = Filter.terms(execution='bool', field_name1=['value_name1', 'value_name2'])[2]
test('Filter.terms', query, FILTERS['FILTER_TERMS'])
query = Query.terms(execution='bool', field_name1=['value_name1', 'value_name2'])[2]
test('Query.terms', query, FILTERS['QUERY_TERMS'])

query = Filter.missing('field_name1')[2]
test('Filter.missing', query, FILTERS['FILTER_MISSING'])
query = Query.missing('field_name1')[2]
test('Query.missing', query, FILTERS['QUERY_MISSING'])

query = Filter.raw_string('QUERYSTRING')[2]
test('Filter.raw_string', query, FILTERS['RAW_FILTER_STRING'])
query = Query.raw_string('QUERYSTRING')[2]
test('Query.raw_string', query, FILTERS['RAW_QUERY_STRING'])

query = Filter.string(field_name1='value_name1', field_name2=['value_name2', 'value_name3'])[2]
test('Filter.string', query, FILTERS['FILTER_STRING'])
query = Query.string(field_name1='value_name1', field_name2=['value_name2', 'value_name3'])[2]
test('Query.string', query, FILTERS['QUERY_STRING'])

query = Filter.nested('nested_path', must=[Filter.term(field_name1='value_name1')])[2]
test('Query.raw_string', query, FILTERS['NESTED_FILTER'])

query = Query.filtered(query=Query.match_all(), filter=Filter.match_all())[2]
test('Query.filtered', query, FILTERS['QUERY_FILTERED'])

query = Query.fuzzy_like_this(like_text='test fuzzy', fields=['name', 'foo'])[2]
test('Query.fuzzy_like_this', query, FILTERS['QUERY_FUZZY_LIKE_THIS'])

query = Filter.bool(must=[Filter.term(field_name1='value_name1')], must_not=[Filter.term(field_name2='value_name2')], should=[Filter.term(field_name3='value_name3')], _cache=True)[2]
test('Filter.bool', query, FILTERS['FILTER_BOOL'])

query = Query.multi_match(query='multi match', fields=['name', 'foo'], type='cross_fields')[2]
test('Query.multi_match', query, FILTERS['QUERY_MULTI_MATCH'])


# Aggregates:
AGGREGATES = {
    'STATS': {
        'agg_name': {
            'stats': {
                'field': 'field_name1'
            }
        }
    },
    'EXTENDED_STATS': {
        'agg_name': {
            'extended_stats': {
                'field': 'field_name1'
            }
        }
    },
    'HISTOGRAM': {
        'agg_name': {
            'histogram': {
                'field': 'field_name1',
                'interval': 100
            }
        }
    },
    'DATE_HISTOGRAM': {
        'agg_name': {
            'date_histogram': {
                'field': 'field_name1',
                'interval': 'day'
            }
        }
    },
    'TERMS': {
        'agg_name': {
            'terms': {
                'field': 'field_name1',
                'size': 0,
                'shard_size': 0
            }
        }
    },
    'NESTED_STATS': {

    },
    'SUB_AGGREGATES': {
        'agg_name': {
            'terms': {
                'field': 'field_name1',
                'size': 0,
                'shard_size': 0
            },
            'aggregations': {
                'sub_aggregate1': {
                    'sum': {
                        'field': 'sub_field1'
                    }
                }
            }
        }
    },
    'FILTER_SUB_AGGREGATES': {
        'agg_name': {
            'filter': {
                'bool': {
                    'should': [],
                    'must_not': [],
                    'must': [{
                        'term': {
                            'key': 'value'
                        }
                    }]
                }
            },
            'aggregations': {
                'histogram': {
                    'terms': {
                        'field': 'benchmark_value',
                        'size': 0,
                        'shard_size': 0
                    },
                    'aggregations': {
                        'option_count': {
                            'sum': {
                                'field': 'options'
                            }
                        }
                    }
                }
            }
        }
    }
}

# Test aggregates
print '[ElasticQuery] Testing: aggregates'
aggregate = Aggregate.stats('agg_name', 'field_name1')
test('Aggregate.stats', aggregate, AGGREGATES['STATS'])

aggregate = Aggregate.extended_stats('agg_name', 'field_name1')
test('Aggregate.extended_stats', aggregate, AGGREGATES['EXTENDED_STATS'])

aggregate = Aggregate.histogram('agg_name', 'field_name1', interval=100)
test('Aggregate.histogram', aggregate, AGGREGATES['HISTOGRAM'])

aggregate = Aggregate.date_histogram('agg_name', 'field_name1')
test('Aggregate.date_histogram', aggregate, AGGREGATES['DATE_HISTOGRAM'])

aggregate = Aggregate.terms('agg_name', 'field_name1')
test('Aggregate.terms', aggregate, AGGREGATES['TERMS'])

aggregate = Aggregate.terms('agg_name', 'field_name1')
aggregate.sub(Aggregate.sum('sub_aggregate1', 'sub_field1'))
test('Aggregate.sum + sub aggregate', aggregate, AGGREGATES['SUB_AGGREGATES'])

aggregate = Aggregate.filter(
    'agg_name',
    must=[Filter.term(**{'key': 'value'})]
).sub(
    Aggregate.terms('histogram', 'benchmark_value').sub(
        Aggregate.sum('option_count', 'options')
    )
)
test('Aggregate.filter + sub aggregate', aggregate, AGGREGATES['FILTER_SUB_AGGREGATES'])

# Queries
QUERIES = {
    'RANGE_AGGTERMS_AGGSTATS': {
        'aggregations': {
            'test_aggregate1': {
                'terms': {
                    'field': 'field_name1',
                    'size': 0,
                    'shard_size': 0
                }
            },
            'test_aggregate2': {
                'stats': {
                    'field': 'field_name2'
                }
            }
        },
        'filter': {
            'bool': {
                'must': [
                    {
                        'range': {
                            'field_name1': {
                                'gte': 0,
                                'lt': 100
                            }
                        }
                    }
                ],
                'must_not': [],
                'should': []
            }
        },
        'from': 0,
        'size': 10
    }
}

# Test queries
query = ElasticQuery()
query.must(Filter.range('field_name1', gte=0, lt=100))
query.aggregate(Aggregate.terms('test_aggregate1', 'field_name1'))
query.aggregate(Aggregate.stats('test_aggregate2', 'field_name2'))
query.offset(0)
query.size(10)
test('Full query: range + terms agg + stats agg', query.structure, QUERIES['RANGE_AGGTERMS_AGGSTATS'])


# If we're still here, we're done!
print '[ElasticQuery] All tests complete!\n'
sys.exit(0)
