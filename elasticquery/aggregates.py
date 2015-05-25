# ElasticQuery
# File: elasticquery/aggregates.py
# Desc: internal ElasticQuery definitions mapping to Elasticsearch aggregate objects

from .dsl import BaseAggregate, MetaAggregate
from .exception import NoAggregate

AGGREGATES = {
    'min': {
        'args': ('field',)
    },
    'max': {
        'args': ('field',)
    },
    'sum': {
        'args': ('field',)
    },
    'avg': {
        'args': ('field',)
    },
    'stats': {
        'args': ('field',)
    },
    'extended_stats': {
        'args': ('field',)
    },
    'value_count': {
        'args': ('field',)
    },
    'percentiles': {
        'args': ('field',)
    },
    'percentile_ranks': {
        'args': ('field',)
    },
    'cardinality': {
        'args': ('field',)
    },
    'geo_bounds': {
        'args': ('field',)
    },
    'top_hits': {
    },
    'scripted_metric': {
    },
    'global': {
    },
    'filter': {
        'args': ({'filter': '_filter'},)
    },
    'filters': {
        'args': ({'filters': ['_filter']},)
    },
    'missing': {
        'args': ('field',)
    },
    'nested': {
        'args': ('path',)
    },
    'reverse_nested': {
    },
    'children': {
        'args': ('type',)
    },
    'terms': {
        'args': ('field',)
    },
    'significant_terms': {
        'args': ('field',)
    },
    'range': {
        'args': ('field', {'ranges': []})
    },
    'date_range': {
        'args': ('field', {'ranges': []})
    },
    'ip_range': {
        'args': ('field', {'ranges': []})
    },
    'histogram': {
        'args': ('field', 'interval')
    },
    'date_histogram': {
        'args': ('field', 'interval')
    },
    'geo_distance': {
        'args': ('field', 'origin', {'ranges': []})
    },
    'geohash_grid': {
        'args': ('field',)
    }
}


class Aggregate(BaseAggregate):
    __metaclass__ = MetaAggregate

    _eq_type = 'aggregate'
    _definitions = AGGREGATES
    _exception = NoAggregate
