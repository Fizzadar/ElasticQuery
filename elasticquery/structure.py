# ElasticQuery
# File: structure.py
# Desc: define structures for ES query elements

from .exception import ElasticQueryError


# Filter structures
class Filter(object):
    type = 'filter'

    @classmethod
    def nested(self, path, musts=[], shoulds=[], must_nots=[]):
        must = [v[1] for v in musts]
        should = [v[1] for v in shoulds]
        must_not = [v[1] for v in must_nots]

        return self.type, {
            'nested': {
                'path': path,
                self.type: {
                    'bool': {
                        'must': must,
                        'should': should,
                        'must_not': must_not
                    }
                }
            }
        }

    @classmethod
    def range(self, field, gt=None, gte=None, lt=None, lte=None):
        data = {
            'range': {
                field: {}
            }
        }
        if gt is not None:
            data['range'][field]['gt'] = gt
        if gte is not None:
            data['range'][field]['gte'] = gte
        if lt is not None:
            data['range'][field]['lt'] = lt
        if lte is not None:
            data['range'][field]['lte'] = lte

        return self.type, data

    @classmethod
    def prefix(self, **kwargs):
        return self.type, {
            'prefix': kwargs
        }

    @classmethod
    def term(self, **kwargs):
        return self.type, {
            'term': kwargs
        }

    @classmethod
    def terms(self, **kwargs):
        for key, value in kwargs.iteritems():
            if not isinstance(value, list):
                raise ElasticQueryError('terms values must be lists')

        return self.type, {
            'terms': kwargs
        }

    @classmethod
    def missing(self, field):
        if self.type == 'filter':
            return self.type, {
                'missing': {
                    'field': field
                }
            }
        else:
            return self.type, {
                'filtered': {
                    'filter': {
                        'missing': {
                            'field': field
                        }
                    }
                }
            }

    @classmethod
    def raw_string(self, string, default_operator='AND'):
        if self.type == 'filter':
            return self.type, {
                'query': {
                    'query_string': {
                        'query': string,
                        'default_operator': default_operator
                    }
                }
            }
        else:
            return self.type, {
                'query_string': {
                    'query': string,
                    'default_operator': default_operator
                }
            }

    @classmethod
    def string(self, default_operator='AND', list_operator='OR', **kwargs):
        and_filters = []
        for key, value in kwargs.iteritems():
            if isinstance(value, list):
                if len(value) > 0:
                    or_filters = []
                    for match in value:
                        or_filters.append(u'({0})'.format(match))

                    and_filters.append(u'({0}:({1}))'.format(key, u' {0} '.format(list_operator).join(or_filters)))
            else:
                and_filters.append(u'{0}:{1}'.format(key, value))

        query_string = u' {0} '.format(default_operator).join(and_filters)

        if self.type == 'filter':
            return self.type, {
                'query': {
                    'query_string': {
                        'query': query_string,
                        'default_operator': default_operator
                    }
                }
            }
        else:
            return self.type, {
                'query_string': {
                    'query': query_string,
                    'default_operator': default_operator
                }
            }

    @classmethod
    def or_filter(self, *args):
        if self.type == 'filter':
            return self.type, {
                'or': [arg[1] for arg in args]
            }
        else:
            return self.type, {
                'filtered': {
                    'filter': {
                        'or': [arg[1] for arg in args]
                    }
                }
            }


# Query structures
# inherits filters due to overlap
class Query(Filter):
    type = 'query'

    @classmethod
    def mlt(self, field, match, min_term_frequency=1, max_query_terms=False):
        settings = {
            'like_text': match
        }
        if min_term_frequency:
            settings['min_term_freq'] = min_term_frequency
        if max_query_terms:
            settings['max_query_terms'] = max_query_terms

        return self.type, {
            'more_like_this_field': {
                field: settings
            }
        }


# Aggregate structures
# named, so only return self-contained dict
class Aggregate(object):
    @classmethod
    def sub(self, aggregate, **aggregates):
        aggregate['aggregations'] = aggregates
        return aggregate

    @classmethod
    def sum(self, field):
        return {
            'sum': {
                'field': field
            }
        }

    @classmethod
    def avg(self, field):
        return {
            'avg': {
                'field': field
            }
        }

    @classmethod
    def min(self, field):
        return {
            'min': {
                'field': field
            }
        }

    @classmethod
    def max(self, field):
        return {
            'max': {
                'field': field
            }
        }

    @classmethod
    def stats(self, field):
        return {
            'stats': {
                'field': field
            }
        }

    @classmethod
    def extended_stats(self, field):
        return {
            'extended_stats': {
                'field': field
            }
        }

    @classmethod
    def missing(self, field):
        return {
            'missing': {
                'field': field
            }
        }

    @classmethod
    def value_count(self, field):
        return {
            'value_count': {
                'field': field
            }
        }

    @classmethod
    def histogram(self, field, interval):
        try:
            interval = int(interval)
        except ValueError:
            raise ElasticQueryError('interval must be a number')

        return {
            'histogram': {
                'field': field,
                'interval': interval
            }
        }

    @classmethod
    def date_histogram(self, field, interval='day'):
        return {
            'date_histogram': {
                'field': field,
                'interval': interval
            }
        }

    @classmethod
    def terms(self, field, size=None, shard_size=None):
        if size is None:
            size = 999999999
        if shard_size is None:
            shard_size = 999999999

        try:
            size = int(size)
            shard_size = int(shard_size)
        except ValueError:
            raise ElasticQueryError('size/shard_size must be a number or None')

        return {
            'terms': {
                'field': field,
                'size': size,
                'shard_size': shard_size
            }
        }

    @classmethod
    def nested(self, path):
        return {
            'nested': {
                'path': path
            }
        }

    @classmethod
    def filter(self, musts=[], shoulds=[], must_nots=[]):
        must = [v[1] for v in musts]
        should = [v[1] for v in shoulds]
        must_not = [v[1] for v in must_nots]

        return {
            'filter': {
                'bool': {
                    'must': must,
                    'should': should,
                    'must_not': must_not
                }
            }
        }
