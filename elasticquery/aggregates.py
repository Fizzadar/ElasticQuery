# ElasticQuery
# File: elasticquery/aggregates.py
# Desc: internal ElasticQuery definitions mapping to Elasticsearch aggregate objects

from .dsl import BaseAggregate, MetaAggregate
from .exceptions import NoAggregateError

AGGREGATES = {
    # Metrics aggregations
    #

    'avg': {
        'args': ('field',)
    },
    'cardinality': {
        'args': ('field',)
    },
    'extended_stats': {
        'args': ('field',)
    },
    'geo_bounds': {
        'args': ('field',)
    },
    'geo_centroid': {
        'args': ('field',)
    },
    'max': {
        'args': ('field',)
    },
    'min': {
        'args': ('field',)
    },
    'percentiles': {
        'args': ('field',)
    },
    'percentile_ranks': {
        'args': ('field',)
    },
    'scripted_metric': {
    },
    'stats': {
        'args': ('field',)
    },
    'sum': {
        'args': ('field',)
    },
    'top_hits': {
    },
    'value_count': {
        'args': ('field',)
    },

    # Bucket aggregations
    #

    'children': {
        'args': ('type',)
    },
    'date_histogram': {
        'args': ('field', 'interval')
    },
    'date_range': {
        'args': ('field', {'ranges': []})
    },
    'filter': {
        'args': ({'filter': '_query'},)
    },
    'filters': {
        'args': ({'filters': ['_query']},)
    },
    'geo_distance': {
        'args': ('field', 'origin', {'ranges': []})
    },
    'geohash_grid': {
        'args': ('field',)
    },
    'global': {
    },
    'histogram': {
        'args': ('field', 'interval')
    },
    'ip_range': {
        'args': ('field', {'ranges': []})
    },
    'missing': {
        'args': ('field',)
    },
    'nested': {
        'args': ('path',)
    },
    'range': {
        'args': ('field', {'ranges': []})
    },
    'reverse_nested': {
    },
    'sampler': {
        'args': ('field',)
    },
    'significant_terms': {
        'args': ('field',)
    },
    'terms': {
        'args': ('field',)
    },

    # Pipeline aggregations
    #

    'avg_bucket': {
        'args': ('buckets_path',)
    },
    'derivative': {
        'args': ('buckets_path',)
    },
    'max_bucket': {
        'args': ('buckets_path',)
    },
    'min_bucket': {
        'args': ('buckets_path',)
    },
    'sum_bucket': {
        'args': ('buckets_path',)
    },
    'stats_bucket': {
        'args': ('buckets_path',)
    },
    'extended_stats_bucket': {
        'args': ('buckets_path',)
    },
    'percentiles_bucket': {
        'args': ('buckets_path',)
    },
    'moving_avg': {
        'args': ('buckets_path',)
    },
    'cumulative_sum': {
        'args': ('buckets_path',)
    },
    'bucket_script': {
        'args': ({'buckets_path': {}},)
    },
    'bucket_selector': {
        'args': ({'buckets_path': {}},)
    },
    'serial_diff': {
        'args': ('buckets_path',)
    }
}


class Aggregate(BaseAggregate):
    __metaclass__ = MetaAggregate

    _eq_type = 'aggregate'
    _definitions = AGGREGATES
    _exception = NoAggregateError
