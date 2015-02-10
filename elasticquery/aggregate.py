# ElasticQuery
# File: aggregate.py
# Desc: define structs for ES aggregations

from .exception import ElasticQueryException


class Aggregate(object):
    @classmethod
    def sub(self, (_, aggregate), **aggregates):
        aggregate['aggregations'] = {
            name: aggregate
            for name, (fields, aggregate) in aggregates.iteritems()
        }
        return None, aggregate

    @classmethod
    def sum(self, field):
        return None, {
            'sum': {
                'field': field
            }
        }

    @classmethod
    def avg(self, field):
        return None, {
            'avg': {
                'field': field
            }
        }

    @classmethod
    def min(self, field):
        return None, {
            'min': {
                'field': field
            }
        }

    @classmethod
    def max(self, field):
        return None, {
            'max': {
                'field': field
            }
        }

    @classmethod
    def stats(self, field):
        return None, {
            'stats': {
                'field': field
            }
        }

    @classmethod
    def extended_stats(self, field):
        return None, {
            'extended_stats': {
                'field': field
            }
        }

    @classmethod
    def missing(self, field):
        return None, {
            'missing': {
                'field': field
            }
        }

    @classmethod
    def value_count(self, field):
        return None, {
            'value_count': {
                'field': field
            }
        }

    @classmethod
    def histogram(self, field, interval):
        try:
            interval = int(interval)
        except ValueError:
            raise ElasticQueryException('interval must be a number')

        return None, {
            'histogram': {
                'field': field,
                'interval': interval
            }
        }

    @classmethod
    def date_histogram(self, field, interval='day'):
        return None, {
            'date_histogram': {
                'field': field,
                'interval': interval
            }
        }

    @classmethod
    def terms(self, field, size=None, shard_size=None):
        if size is None:
            size = 0
        if shard_size is None:
            shard_size = 0

        try:
            size = int(size)
            shard_size = int(shard_size)
        except ValueError:
            raise ElasticQueryException('size/shard_size must be a number or None')

        return None, {
            'terms': {
                'field': field,
                'size': size,
                'shard_size': shard_size
            }
        }

    @classmethod
    def nested(self, path):
        return None, {
            'nested': {
                'path': path
            }
        }

    @classmethod
    def filter(self, must=[], should=[], must_not=[]):
        must = [v[2] for v in must] if isinstance(must, list) else []
        should = [v[2] for v in should] if isinstance(should, list) else []
        must_not = [v[2] for v in must_not] if isinstance(must_not, list) else []

        return None, {
            'filter': {
                'bool': {
                    'must': must,
                    'should': should,
                    'must_not': must_not
                }
            }
        }
