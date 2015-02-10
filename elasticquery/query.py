# ElasticQuery
# File: query.py
# Desc: ElasticQuery itself

import json

from .exception import NoESClient, NoIndexName, NoDocType, InvalidField


class ElasticQuery(object):
    '''A class for building ES queries'''
    __es__ = None
    __index__ = None
    __doc_type__ = None
    __mapping__ = None

    def __init__(self, es=None, index=None, doc_type=None, mapping=None):
        self.__es__ = es
        self.__index__ = index
        self.__doc_type__ = doc_type
        self.__mapping__ = mapping

        # A basic, empty, match-everything query
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

    def _ensure_bool(self, type, name):
        '''Ensure we have a bool filter/quer struct prepared'''
        if self.structure[type].get('match_all') == {}:
            self.structure[type] = {
                'bool': {
                    'must': [],
                    'should': [],
                    'must_not': []
                }
            }

    def _ensure_fields(self, fields):
        '''When we have a mapping, ensure the fields we use are valid'''
        if self.__mapping__ is not None:
            mapping_fields = self.__mapping__.keys()
            fields = fields if isinstance(fields, list) else [fields]

            for field in fields:
                if field not in mapping_fields:
                    raise InvalidField(field)

    def set(self, key, value):
        '''Set an arbitrary attribute on this query'''
        self.structure[key] = value
        return self

    def sort(self, field, order=False):
        '''Sort the query results'''
        if not order:
            self.structure['sort'].append(field)
        else:
            self.structure['sort'].append({
                field: {
                    'order': order
                }
            })

        return self

    def fields(self, fields):
        '''Limit the fields returned by this query'''
        self._ensure_fields(fields)
        self.structure['_source'] = fields
        return self

    def aggregate(self, name, (fields, aggregate)):
        '''Add an aggregation to the query'''
        self._ensure_fields(fields)
        self.structure['aggregations'][name] = aggregate
        return self

    def aggregates(self, *aggregates):
        '''Shortcut to add multiple aggregates at once'''
        [self.aggregate(*aggregate) for aggregate in aggregates]
        return self

    def must(self, *must):
        '''Add one or more conditions which must be met by this query'''
        for (type, fields, object) in must:
            self._ensure_fields(fields)
            self._ensure_bool(type, 'must')
            self.structure[type]['bool']['must'].append(object)

        return self

    def should(self, *should):
        '''Add one or more conditions which should be met by this query'''
        for (type, fields, object) in should:
            self._ensure_fields(fields)
            self._ensure_bool(type, 'should')
            self.structure[type]['bool']['should'].append(object)

        return self

    def must_not(self, *must_not):
        '''Add one or more conditions which must not be met by this query'''
        for (type, fields, object) in must_not:
            self._ensure_fields(fields)
            self._ensure_bool(type, 'must_not')
            self.structure[type]['bool']['must_not'].append(object)

        return self

    def dict(self):
        '''Return the current query representation'''
        return self.structure

    def json(self, indent=None):
        '''Return the current query as a JSON document'''
        return json.dumps(
            self.dict(), indent=indent
        )

    def get(self):
        '''Execute the current query (requires __es__, __index__ & __doc_type__)'''
        if self.__es__ is None:
            raise NoESClient()
        if self.__index__ is None:
            raise NoIndexName()
        if self.__doc_type__ is None:
            raise NoDocType()

        return self.__es__.search(
            index=self.__index__,
            doc_type=self.__doc_type__,
            body=self.structure
        )
