# ElasticQuery
# File: query.py
# Desc: ElasticQuery itself

import json

from .exception import NoESClient, NoIndexName, NoDocType # , InvalidField


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

        # An empty query
        self.structure = {}

    def _ensure_bool(self, query_type, name):
        '''Ensure we have a bool filter/quer struct prepared'''
        if not self.structure.get(query_type):
            self.structure[query_type] = {
                'bool': {
                    'must': [],
                    'should': [],
                    'must_not': []
                }
            }

    def _ensure_fields(self, fields):
        '''When we have a mapping, ensure the fields we use are valid'''
        pass
        # if self.__mapping__ is not None:
        #     mapping_fields = self.__mapping__.keys()
        #     fields = fields if isinstance(fields, list) else [fields]

        #     for field in fields:
        #         if field not in mapping_fields:
        #             raise InvalidField(field)

    def set(self, key, value):
        '''Set an arbitrary attribute on this query'''
        self.structure[key] = value
        return self

    def offset(self, offset):
        '''Offset the query results.'''
        self.structure['from'] = offset
        return self

    def size(self, size):
        '''Limit the number of query results.'''
        self.structure['size'] = size
        return self

    def timeout(self, timeout, time_type='s'):
        '''Set a timeout on the query.'''
        self.structure['timeout'] = '{}{}'.format(timeout, time_type)
        return self

    def sort(self, field, order=False):
        '''Sort the query results'''
        if 'sort' not in self.structure:
            self.structure['sort'] = []

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

    def query(self, query):
        '''
        Assign the queries query to one Query object (no bool).
        Note: this with overwrite/be overwritten by .must, .should & .must_not
        '''
        self.structure['query'] = query[2]

    def filter(self, filter):
        '''
        Assign the query filter to one Filter object (no bool).
        Note: this with overwrite/be overwritten by .must, .should & .must_not
        '''
        self.structure['filter'] = filter[2]

    def must(self, *must):
        '''Add one or more conditions which must be met by this query.'''
        for (query_type, fields, object) in must:
            self._ensure_fields(fields)
            self._ensure_bool(query_type, 'must')
            self.structure[query_type]['bool']['must'].append(object)

        return self

    def should(self, *should):
        '''Add one or more conditions which should be met by this query.'''
        for (query_type, fields, object) in should:
            self._ensure_fields(fields)
            self._ensure_bool(query_type, 'should')
            self.structure[query_type]['bool']['should'].append(object)

        return self

    def must_not(self, *must_not):
        '''Add one or more conditions which must not be met by this query.'''
        for (query_type, fields, object) in must_not:
            self._ensure_fields(fields)
            self._ensure_bool(query_type, 'must_not')
            self.structure[query_type]['bool']['must_not'].append(object)

        return self

    def aggregate(self, *aggregates):
        '''Add a aggregations to the query.'''
        if 'aggregations' not in self.structure:
            self.structure['aggregations'] = {}

        [
            self.structure['aggregations'].update(aggregate)
            for aggregate in aggregates
        ]
        return self

    def dict(self):
        '''Return the current query representation.'''
        return self.structure

    def json(self, indent=None):
        '''Return the current query as a JSON document.'''
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
