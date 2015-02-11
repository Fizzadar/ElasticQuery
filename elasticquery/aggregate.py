# ElasticQuery
# File: aggregate.py
# Desc: define structs for ES aggregations

from .exception import ElasticQueryException


class AggregateDict(dict):
    _name = None

    def __init__(self, *args, **kwargs):
        super(AggregateDict, self).__init__(*args, **kwargs)
        self._name = self.keys()[0]

    def sub(self, *aggregates):
        if 'aggregations' not in self[self._name]:
            self[self._name]['aggregations'] = {}

        [
            self[self._name]['aggregations'].update(aggregate)
            for aggregate in aggregates
        ]

        return self


class Aggregate(object):
    @classmethod
    def sum(self, name, field):
        return AggregateDict({
            name: {
                'sum': {
                    'field': field
                }
            }
        })

    @classmethod
    def avg(self, name, field):
        return AggregateDict({
            name: {
                'avg': {
                    'field': field
                }
            }
        })

    @classmethod
    def min(self, name, field):
        return AggregateDict({
            name: {
                'min': {
                    'field': field
                }
            }
        })

    @classmethod
    def max(self, name, field):
        return AggregateDict({
            name: {
                'max': {
                    'field': field
                }
            }
        })

    @classmethod
    def stats(self, name, field):
        return AggregateDict({
            name: {
                'stats': {
                    'field': field
                }
            }
        })

    @classmethod
    def extended_stats(self, name, field):
        return AggregateDict({
            name: {
                'extended_stats': {
                    'field': field
                }
            }
        })

    @classmethod
    def missing(self, name, field):
        return AggregateDict({
            name: {
                'missing': {
                    'field': field
                }
            }
        })

    @classmethod
    def value_count(self, name, field):
        return AggregateDict({
            name: {
                'value_count': {
                    'field': field
                }
            }
        })

    @classmethod
    def histogram(self, name, field, interval):
        try:
            interval = int(interval)
        except ValueError:
            raise ElasticQueryException('interval must be a number')

        return AggregateDict({
            name: {
                'histogram': {
                    'field': field,
                    'interval': interval
                }
            }
        })

    @classmethod
    def date_histogram(self, name, field, interval='day'):
        return AggregateDict({
            name: {
                'date_histogram': {
                    'field': field,
                    'interval': interval
                }
            }
        })

    @classmethod
    def terms(self, name, field, size=None, shard_size=None):
        if size is None:
            size = 0
        if shard_size is None:
            shard_size = 0

        try:
            size = int(size)
            shard_size = int(shard_size)
        except ValueError:
            raise ElasticQueryException('size/shard_size must be a number or None')

        return AggregateDict({
            name: {
                'terms': {
                    'field': field,
                    'size': size,
                    'shard_size': shard_size
                }
            }
        })

    @classmethod
    def nested(self, name, path):
        return AggregateDict({
            name: {
                'nested': {
                    'path': path
                }
            }
        })

    @classmethod
    def filter(self, name, must=None, should=None, must_not=None):
        must = [v[2] for v in must] if isinstance(must, list) else []
        should = [v[2] for v in should] if isinstance(should, list) else []
        must_not = [v[2] for v in must_not] if isinstance(must_not, list) else []

        return AggregateDict({
            name: {
                'filter': {
                    'bool': {
                        'must': must,
                        'should': should,
                        'must_not': must_not
                    }
                }
            }
        })
