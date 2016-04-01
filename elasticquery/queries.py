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
        'kwargs': (
            'operator', 'zero_terms_query', 'cutoff_frequency', 'boost', 'rewrite',
            'prefix_length', 'fuzziness', 'minimum_should_match', 'analyzer',
            'max_expansions'
        )
    },
    'multi_match': {
        'args': ({'fields': []}, 'query'),
        'kwargs': (
            'operator', 'zero_terms_query', 'cutoff_frequency', 'boost', 'rewrite',
            'prefix_length', 'fuzziness', 'minimum_should_match', 'analyzer',
            'max_expansions'
        )
    },
    'common': {
        'args': ('query',),
        'kwargs': (
            'minimum_should_match', 'high_freq', 'low_freq', 'high_freq_operator',
            'low_freq_operator', 'cutoff_frequency'
        ),
        'process': lambda q: {'body': q}
    },
    'query_string': {
        'args': ('query',),
        'kwargs': (
            {'fields': []}, 'default_field', 'default_operator', 'analyzer',
            'allow_leading_wildcard', 'lowercase_expanded_terms',
            'enable_position_increments', 'fuzzy_max_expansions', 'fuzziness',
            'fuzzy_prefix_length', 'phrase_slop', 'boost', 'analyze_wildcard',
            'auto_generate_phrase_queries', 'max_determinized_states',
            'minimum_should_match', 'lenient', 'locale', 'time_zone'
        )
    },
    'simple_query_string': {
        'args': ('query',),
        'kwargs': (
            {'fields': []}, 'default_operator', 'analyzer', 'flags', 'locale', 'lenient',
            'lowercase_expanded_terms', 'analyze_wildcard', 'minimum_should_match'
        )
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
    'function_score': {
        'args': ({'functions': []},),
        'kwargs': ({'query': '_query'},)
    },
    'dis_max': {
        'args': ({'queries': ['_query']},)
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
    'template': {
    },
    'script': {
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
    'span_or': {
        'args': ({'clauses': ['_query']},)
    },
    'span_not': {
        'kwargs': ({('include', 'exclude'): '_query'},)
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
