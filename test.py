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
def error( message ):
    print '\t[{0}] Error: {1}\n'.format( test_count['count'], message )
    sys.exit( 1 )
def success( message ):
    print '\t[{0}] Success: {1}'.format( test_count['count'], message )

def test( name, got, want ):
    if got != want:
        print 'want: {0}'.format( json.dumps( want ))
        print 'got: {0}'.format( json.dumps( got ))
        error( '{0} fail: {1} != {2}'.format( name, got, want ))
    else:
        success( '{0}'.format( name ))

    test_count['count'] += 1

print '\n[ElasticQuery] Begin tests!'

# Filters/Queries:
FILTERS = {
    'RANGE': {
        'range': {
            'field_name1': {
                'from': 0,
                'to': 100
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
    'TERMS': {
        'terms': {
            'field_name1': ['value_name1', 'value_name2']
        }
    },
    'RAW_STRING': {
        'query_string': {
            'query': 'QUERYSTRING',
            'default_operator': 'AND'
        }
    },
    'STRING': {
        'query_string': {
            'query': 'field_name1:value_name1 AND (field_name2:((value_name2) OR (value_name3)))',
            'default_operator': 'AND'
        }
    },
    'NESTED_FILTER': {

    }
}

# Test filters
print '[ElasticQuery] Testing: filters & queries'
query = Query.range( 'field_name1', range_from=0, range_to=100 )[1]
test( 'Query.range', query, FILTERS['RANGE'] )

query = Query.prefix( field_name1='value_name1' )[1]
test( 'Query.prefix', query, FILTERS['PREFIX'] )

query = Query.term( field_name1='value_name1' )[1]
test( 'Query.term', query, FILTERS['TERM'] )

query = Query.terms( field_name1=['value_name1', 'value_name2'] )[1]
test( 'Query.terms', query, FILTERS['TERMS'] )

query = Query.raw_string( 'QUERYSTRING' )[1]
test( 'Query.raw_string', query, FILTERS['RAW_STRING'] )

query = Query.string( field_name1='value_name1', field_name2=['value_name2', 'value_name3'] )[1]
test( 'Query.string', query, FILTERS['STRING'] )



# Aggregates:
AGGREGATES = {
    'STATS': {
        'stats': {
            'field': 'field_name1'
        }
    },
    'EXTENDED_STATS': {
        'extended_stats': {
            'field': 'field_name1'
        }
    },
    'HISTOGRAM': {
        'histogram': {
            'field': 'field_name1',
            'interval': 100
        }
    },
    'DATE_HISTOGRAM': {
        'date_histogram': {
            'field': 'field_name1',
            'interval': 'day'
        }
    },
    'TERMS': {
        'terms': {
            'field': 'field_name1',
            'size': 999999999,
            'shard_size': 999999999
        }
    },
    'NESTED_STATS': {

    },
    'SUB_AGGREGATES': {
        'terms': {
            'field': 'field_name1',
            'size': 999999999,
            'shard_size': 999999999
        },
        'aggregations': {
            'sub_aggregate1': {
                'sum': {
                    'field': 'sub_field1'
                }
            }
        }
    },
    'FILTER_SUB_AGGREGATES': {
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
            'price_histogram': {
                'terms': {
                    'field': 'bp_now',
                    'size': 999999999,
                    'shard_size': 999999999
                },
                'aggregations': {
                    'option_count': {
                        'sum': {
                            'field': 'option_count_current'
                        }
                    }
                }
            }
        }
    }
}

# Test aggregates
print '[ElasticQuery] Testing: aggregates'
aggregate = Aggregate.stats( 'field_name1' )
test( 'Aggregate.stats', aggregate, AGGREGATES['STATS'] )

aggregate = Aggregate.extended_stats( 'field_name1' )
test( 'Aggregate.extended_stats', aggregate, AGGREGATES['EXTENDED_STATS'] )

aggregate = Aggregate.histogram( 'field_name1', interval=100 )
test( 'Aggregate.histogram', aggregate, AGGREGATES['HISTOGRAM'] )

aggregate = Aggregate.date_histogram( 'field_name1' )
test( 'Aggregate.date_histogram', aggregate, AGGREGATES['DATE_HISTOGRAM'] )

aggregate = Aggregate.terms( 'field_name1' )
test( 'Aggregate.terms', aggregate, AGGREGATES['TERMS'] )

aggregate = Aggregate.sub( Aggregate.terms( 'field_name1' ), **{ 'sub_aggregate1': Aggregate.sum( 'sub_field1' )})
test( 'Aggregate.sum + sub aggregate', aggregate, AGGREGATES['SUB_AGGREGATES'] )

aggregate = Aggregate.sub(
    Aggregate.filter( musts=[Filter.term( **{ 'key': 'value' } )] ), **{
        'price_histogram': Aggregate.sub(
            Aggregate.terms('bp_now'),**{
                'option_count':Aggregate.sum('option_count_current')
            }
        )
    }
)
test( 'Aggregate.filter + sub aggregate', aggregate, AGGREGATES['FILTER_SUB_AGGREGATES'] )

# Queries
QUERIES = {
    'RANGE_AGGTERMS_AGGSTATS': {
        'aggregations': {
            'test_aggregate1': {
                'terms': {
                    'field': 'field_name1',
                    'size': 999999999,
                    'shard_size': 999999999
                }
            },
            'test_aggregate2': {
                'stats': {
                    'field': 'field_name2'
                }
            }
        },
        'query': {
            'match_all': {}
        },
        'filter': {
            'bool': {
                'must': [
                    {
                        'range': {
                            'field_name1': {
                                'from': 0,
                                'to': 100
                            }
                        }
                    }
                ],
                'must_not': [],
                'should': []
            }
        },
        'sort': []
    }
}

# Test queries
query = ElasticQuery()
query.must( Filter.range( 'field_name1', 0, 100 ))
query.aggregate( 'test_aggregate1', Aggregate.terms( 'field_name1' ))
query.aggregate( 'test_aggregate2', Aggregate.stats( 'field_name2' ))
test( 'Full query: range + terms agg + stats agg', query.structure, QUERIES['RANGE_AGGTERMS_AGGSTATS'] )


# If we're still here, we're done!
print '[ElasticQuery] All tests complete!\n'
sys.exit( 0 )