# ElasticQuery
# File: query.py
# Desc: ElasticQuery itself

import json

class ElasticQuery:
    def __init__( self ):
        self.structure = {
            'query': {
                'match_all': {}
            },
            'filter': {
                'match_all': {}
            },
            'aggregations': {},
            'sort': []
        }

    def _ensure_bool( self, type, name ):
        if self.structure[type].get( 'match_all' ) == {}:
            self.structure[type] = {
                'bool': {
                    'must': [],
                    'should': [],
                    'must_not': []
                }
            }

    def fields( self, fields ):
        self.structure['_source'] = fields
        return self

    def sort( self, field, order=False ):
        if not order:
            self.structure.sort.append( field )
        else:
            self.structure.sort.append({
                field: {
                    'order': order
                }
            })

        return self

    def aggregate( self, name, aggregate ):
        self.structure['aggregations'][name] = aggregate
        return self

    def must( self, data ):
        self._ensure_bool( data[0], 'must' )
        self.structure[data[0]]['bool']['must'].append( data[1] )
        return self

    def should( self, data ):
        self._ensure_bool( data[0], 'should' )
        self.structure[data[0]]['bool']['should'].append( data[1] )
        return self

    def must_not( self, data ):
        self._ensure_bool( data[0], 'must_not' )
        self.structure[data[0]]['bool']['must_not'].append( data[1] )
        return self

    def compile( self ):
        return json.dumps( self.structure )