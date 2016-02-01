# ElasticQuery
# File: elasticquery/queries.py
# Desc: internal ElasticQuery definitions mapping to Elasticsearch query objects

from .dsl import BaseQuery, MetaQuery
from .exceptions import NoQueryError

QUERIES = {
    'match_all': {
        'kwargs': ('boost',)
    },

    # Full text queries
    #

    'match': {
        'field': True,
        'args': ('query',),
        'kwargs': ('operator', 'zero_terms_query', 'cutoff_frequency', 'boost')
    },
    'multi_match': {
        'args': ({'fields': []}, 'query')
    },
    'common': {
        'args': ('query',),
        'process': lambda q: {'body': q}
    },
    'query_string': {
        'args': ('query',),
        'kwargs': ({'fields': []},)
    },
    'simple_query_string': {
        'args': ('query',),
        'kwargs': ({'fields': []},)
    },

    # Term level queries
    #

    'term': {
        'field': True,
        'args': ('value',),
        'kwargs': ('boost',)
    },
    'terms': {
        'field': True,
        'value_only': True,
        'args': ({'value': ['']},)
    },
    'range': {
        'field': True,
        'kwargs': ('gte', 'gt', 'lte', 'lt')
    },
    'exists': {
        'args': ('field',)
    },
    'missing': {
        'args': ('field',)
    },
    'prefix': {
        'field': True,
        'args': ('value',),
        'kwargs': ('boost',)
    },
    'wildcard': {
        'field': True,
        'args': ('value',),
        'kwargs': ('boost',)
    },
    'regexp': {
        'field': True,
        'args': ('value',),
        'kwargs': ('boost', 'flags')
    },
    'fuzzy': {
        'field': True,
        'args': ('value',),
        'kwargs': ('boost', 'fuzziness', 'prefix_length', 'max_expansions')
    },
    'type': {
        'args': ('value',)
    },
    'ids': {
        'args': ({'values': []},),
        'kwargs': ('type',)
    },

    # Compound queries
    #

    'constant_score': {
        'kwargs': ({'query': '_query'},)
    },
    'bool': {
        'kwargs': ({('must', 'must_not', 'should'): ['_query']},)
    },
    'dis_max': {
        'args': ({'queries': ['_query']},)
    },
    'function_score': {
        'args': ({'functions': []},),
        'kwargs': ({'query': '_query'},)
    },
    'boosting': {
        'kwargs': ({('positive', 'negative'): '_query'})
    },
    'indices': {
        'args': ({'indices': []},),
        'kwargs': ({('query', 'no_match_query'): '_query'},)
    },
    'limit': {
        'args': ('value',)
    },

    # Joining queries
    #

    'nested': {
        'args': ('path', {'query': '_query'}),
    },
    'has_child': {
        'args': ('type',),
        'kwargs': ({'query': '_query'},)
    },
    'has_parent': {
        'args': ('parent_type',),
        'kwargs': ({'query': '_query'},)
    },

    # Geo queries
    #

    'geo_shape': {
        'field': True,
        'kwargs': ('type', {'coordinates': []}),
        'field_process': lambda q: {'shape': q}
    },
    'geo_bounding_box': {
        'field': True,
        'kwargs': ('top_left', 'bottom_right')
    },
    'geo_distance': {
        'field': True,
        'kwargs': ('lat', 'lon')
    },
    'geo_distance_range': {
        'field': True,
        'kwargs': ('lat', 'lon')
    },
    'geo_polygon': {
        'field': True,
        'args': ({'points': []},)
    },
    'geohash_cell': {
        'field': True,
        'kwargs': ('lat', 'lon',)
    },

    # Specialized queries
    #

    'more_like_this': {
        'args': ({'fields': []}, 'like_text')
    },

    # Span queries
    #

    'span_term': {
        'field': True,
        'args': ('value',),
        'kwargs': ('boost',)
    },
    'span_multi': {
        'args': ({'match': '_query'},)
    },
    'span_first': {
        'args': ({'match': '_query'},)
    },
    'span_near': {
        'args': ({'clauses': ['_query']},)
    },
    'span_not': {
        'kwargs': ({('include', 'exclude'): '_query'},)
    },
    'span_or': {
        'args': ({'clauses': ['_query']},)
    },
    'span_containing': {
        'args': ({('little', 'big'): '_query'},)
    },
    'span_within': {
        'args': ({('little', 'big'): '_query'},)
    }
}


class Query(BaseQuery):
    __metaclass__ = MetaQuery

    _eq_type = 'query'
    _definitions = QUERIES
    _exception = NoQueryError
