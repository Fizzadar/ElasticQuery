# ElasticQuery
# File: filter_query.py
# Desc: define structs for ES Filters & Queries

from datetime import datetime


def inline_filter_queries(filter_queries):
    return [v[2] for v in filter_queries] if isinstance(filter_queries, list) else []


class Filter(object):
    type = 'filter'

    @classmethod
    def nested(self, path, must=None, should=None, must_not=None):
        must = inline_filter_queries(must)
        should = inline_filter_queries(should)
        must_not = inline_filter_queries(must_not)

        return self.type, path, {
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

        for range_key, range_value in data['range'][field].iteritems():
            if isinstance(range_value, datetime):
                data['range'][field][range_key] = range_value.isoformat()

        return self.type, field, data

    @classmethod
    def prefix(self, **kwargs):
        return self.type, kwargs.keys(), {
            'prefix': kwargs
        }

    @classmethod
    def term(self, **kwargs):
        return self.type, kwargs.keys(), {
            'term': kwargs
        }

    @classmethod
    def terms(self, execution='plain', **kwargs):
        if self.type == 'filter':
            kwargs.update({
                'execution': execution
            })

            return self.type, None, {
                'terms': kwargs
            }
        else:
            return self.type, None, {
                'terms': kwargs,
            }

    @classmethod
    def match(self, **kwargs):
        if self.type == 'filter':
            return self.type, kwargs.keys(), {
                'query': {
                    'match': kwargs,
                    'analyzer': None
                }
            }
        else:
            return self.type, kwargs.keys(), {
                'match': kwargs
            }

    @classmethod
    def missing(self, field):
        if self.type == 'filter':
            return self.type, field, {
                'missing': {
                    'field': field
                }
            }
        else:
            return self.type, field, {
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
            return self.type, [], {
                'query': {
                    'query_string': {
                        'query': string,
                        'default_operator': default_operator
                    }
                }
            }
        else:
            return self.type, [], {
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
            return self.type, [], {
                'query': {
                    'query_string': {
                        'query': query_string,
                        'default_operator': default_operator
                    }
                }
            }
        else:
            return self.type, [], {
                'query_string': {
                    'query': query_string,
                    'default_operator': default_operator
                }
            }

    @classmethod
    def or_filter(self, *args):
        if self.type == 'filter':
            return self.type, [], {
                'or': [arg[2] for arg in args]
            }
        else:
            return self.type, [], {
                'filtered': {
                    'filter': {
                        'or': [arg[2] for arg in args]
                    }
                }
            }


class Query(Filter):
    type = 'query'

    @classmethod
    def constant_score(self, query_type='filter', must=None, should=None, must_not=None):
        must = inline_filter_queries(must)
        should = inline_filter_queries(should)
        must_not = inline_filter_queries(must_not)

        return self.type, [], {
            'constant_score': {
                query_type: {
                    'bool': {
                        'must': must,
                        'should': should,
                        'must_not': must_not
                    }
                }
            }
        }

    @classmethod
    def mlt(self, field, match, min_term_frequency=1, max_query_terms=False):
        settings = {
            'like_text': match
        }
        if min_term_frequency:
            settings['min_term_freq'] = min_term_frequency
        if max_query_terms:
            settings['max_query_terms'] = max_query_terms

        return self.type, field, {
            'more_like_this_field': {
                field: settings
            }
        }
