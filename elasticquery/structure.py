# ElasticQuery
# File: structure.py
# Desc: define structures for ES query elements

from exception import ElasticQueryError

# Filter structures
class FilterStructs:
    type = 'filter'

    def nested( self, path, musts=[], shoulds=[], must_nots=[] ):
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

    def range( self, field, range_from=False, range_to=False ):
        data = {
            'range': {
                field: {}
            }
        }

        if isinstance( range_from, int ):
            data['range'][field]['from'] = range_from
        if isinstance( range_to, int ):
            data['range'][field]['to'] = range_to

        return self.type, data

    def prefix( self, **kwargs ):
        return self.type, {
            'prefix': kwargs
        }

    def term( self, **kwargs ):
        return self.type, {
            'term': kwargs
        }

    def terms( self, **kwargs ):
        for key, value in kwargs.iteritems():
            if not isinstance( value, list ):
                raise ElasticQueryError( 'terms values must be lists' )

        return self.type, {
            'terms': kwargs
        }

    def raw_string( self, string, default_operator='AND' ):
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

    def string( self, default_operator='AND', **kwargs ):
        and_filters = []
        for key, value in kwargs.iteritems():
            if isinstance( value, list ):
                if len( value ) > 0:
                    or_filters = []

                    for match in value:
                        or_filters.append( '{0}:{1}'.format( key, match ))

                    and_filters.append( '( {0} )'.format( ' OR '.join( or_filters )))
            else:
                and_filters.append( '{0}:{1}'.format( key, value ))

        query_string = ' {0} '.format( default_operator ).join( and_filters )

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


# Query structures
# inherits filters due to overlap
class QueryStructs( FilterStructs ):
    type = 'query'

    def mlt( self, field, match, min_term_frequency=1, max_query_terms=False ):
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
class AggregateStructs:
    def stats( self, field ):
        return {
            'stats': {
                'field': field
            }
        }

    def extended_stats( self, field ):
        return {
            'extended_stats': {
                'field': field
            }
        }

    def histogram( self, field, interval ):
        return {
            'histogram': {
                'field': field,
                'interval': interval
            }
        }

    def date_histogram( self, field, interval='day' ):
        return {
            'date_histogram': {
                'field': field,
                'interval': interval
            }
        }

    def terms( self, field ):
        return {
            'terms': {
                'field': field
            }
        }

    def nested( self, path, **kwargs ):
        aggregates = {}
        for key, value in kwargs.iteritems():
            aggregates[key] = value

        return {
            'nested': {
                'path': path
            },
            'aggregates': aggregates
        }


# Init for importing
Filter = FilterStructs()
Query = QueryStructs()
Aggregate = AggregateStructs()