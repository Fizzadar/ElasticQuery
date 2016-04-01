# ElasticQuery
# File: elasticquery/queries.py
# Desc: internal ElasticQuery definitions mapping to Elasticsearch query objects

from .dsl import BaseFilterQuery, MetaFilterQuery
from .exception import NoQuery

QUERIES = {
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
    'bool': {
        'kwargs': ({('must', 'must_not', 'should'): ['_query']},)
    },
    'boost': {
        'kwargs': ({('positive', 'negative'): '_query'})
    },
    'common': {
        'args': ('query',),
        'kwargs': (
            'minimum_should_match', 'high_freq', 'low_freq', 'high_freq_operator',
            'low_freq_operator', 'cutoff_frequency'
        ),
        'process': lambda q: {'body': q}
    },
    'constant_score': {
        'kwargs': ({'query': '_query', 'filter': '_filter'},)
    },
    'dis_max': {
        'args': ({'queries': ['_query']},)
    },
    'filtered': {
        'kwargs': ({'query': '_query', 'filter': '_filter'},)
    },
    'fuzzy_like_this': {
        'args': ({'fields': []}, 'like_text')
    },
    'fuzzy_like_this_field': {
        'field': True,
        'args': ('like_text',),
        'kwargs': (
            'max_query_terms', 'ignore_tf', 'fuzziness', 'prefix_length', 'boost', 'analyzer'
        )
    },
    'function_score': {
        'args': ({'functions': []},),
        'kwargs': ({'query': '_query', 'filter': '_filter'},)
    },
    'fuzzy': {
        'field': True,
        'args': ('value',),
        'kwargs': ('boost', 'fuzziness', 'prefix_length', 'max_expansions')
    },
    'geo_shape': {
        'field': True,
        'kwargs': ('type', {'coordinates': []}),
        'field_process': lambda q: {'shape': q}
    },
    'has_child': {
        'args': ('type',),
        'kwargs': ({'query': '_query', 'filter': '_filter'},)
    },
    'has_parent': {
        'args': ('parent_type',),
        'kwargs': ({'query': '_query', 'filter': '_filter'},)
    },
    'ids': {
        'args': ({'values': []},),
        'kwargs': ('type',)
    },
    'indices': {
        'args': ({'indices': []},),
        'kwargs': ({('query', 'no_match_query'): '_query'},)
    },
    'match_all': {
        'kwargs': ('boost',)
    },
    'more_like_this': {
        'args': ({'fields': []}, 'like_text')
    },
    'nested': {
        'args': ('path', {'query': '_query'}),
    },
    'prefix': {
        'field': True,
        'args': ('value',),
        'kwargs': ('boost',)
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
    'range': {
        'field': True,
        'kwargs': ('gte', 'gt', 'lte', 'lt',)
    },
    'regexp': {
        'field': True,
        'args': ('value',),
        'kwargs': ('boost', 'flags')
    },
    'span_first': {
        'args': ({'match': '_query'},)
    },
    'span_multi': {
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
    'span_term': {
        'field': True,
        'args': ('value',),
        'kwargs': ('boost',)
    },
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
    'top_children': {
        'args': ('type',),
        'kwargs': ({'query': '_query'},)
    },
    'wildcard': {
        'field': True,
        'args': ('value',),
        'kwargs': ('boost',)
    }
}


class Query(BaseFilterQuery):
    __metaclass__ = MetaFilterQuery

    _eq_type = 'query'
    _definitions = QUERIES
    _exception = NoQuery
