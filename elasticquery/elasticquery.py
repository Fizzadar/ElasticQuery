# ElasticQuery
# File: elasticquery.py
# Desc: ElasticQuery itself

import json

from .dsl_util import unroll_struct


def _json_date(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError('{0} is not JSON serializable'.format(obj))


class ElasticQuery(object):
    '''
    A class for building ES queries.
    '''

    _es = None
    _index = None
    _doc_type = None

    _query = None

    def __init__(self, es=None, index=None, doc_type=None):
        '''
        Creates a new query object.
        '''

        self._es = es
        self._index = index
        self._doc_type = doc_type

        self._aggs = []
        self._suggesters = []

        # An empty query
        self._struct = {}

    def query(self, query):
        '''
        Set the query for this query.
        '''

        self._query = query

    def aggregate(self, *aggregates):
        '''
        Add one or more aggregates to this query.
        '''

        self._aggs.extend(aggregates)

    def suggest(self, *suggesters):
        '''
        Add one or more suggesters to this query.
        '''

        self._suggesters.extend(suggesters)

    def set(self, key, value):
        '''
        Set an arbitrary attribute on this query.
        '''

        self._struct[key] = value
        return self

    def from_(self, from_):
        '''
        Set the from/offset for this query.
        '''

        self._struct['from'] = from_
        return self

    def size(self, size):
        '''
        Set the size of this query.
        '''

        self._struct['size'] = size
        return self

    def timeout(self, timeout):
        '''
        Set the timeout for this query.
        '''

        self._struct['timeout'] = timeout
        return self

    def fields(self, fields):
        '''
        Set the fields/_source for this query.
        '''

        self._struct['_source'] = fields
        return self

    def sort(self, field, order=None):
        '''
        Sort this query.
        '''

        if 'sort' not in self._struct:
            self._struct['sort'] = []

        if not order:
            self._struct['sort'].append(field)
        else:
            self._struct['sort'].append({
                field: {
                    'order': order
                }
            })

        return self

    def dict(self):
        '''
        Returns the current query in dict format.
        '''

        # Just query? Use as-is
        if self._query:
            self._struct['query'] = self._query

        if self._aggs:
            aggs = {}
            for agg in self._aggs:
                aggs.update(agg.dict())

            self._struct['aggregations'] = aggs

        if self._suggesters:
            suggs = {}
            for sugg in self._suggesters:
                suggs.update(sugg.dict())

            self._struct['suggest'] = suggs

        return unroll_struct(self._struct)

    def get(self):
        '''
        Execute the current query (requires _es, _index & _doc_type).
        '''

        if self._es is None:
            raise ValueError('No Elasticsearch instance attached to this query')

        if self._index is None:
            raise ValueError('No index specified for this query')

        if self._doc_type is None:
            raise ValueError('No doc type specified for this query')

        return self._es.search(
            index=self._index,
            doc_type=self._doc_type,
            body=self.dict()
        )

    def json(self, **kwargs):
        '''
        Returns a JSON representation of the current query. Kwargs are passed to
        ``json.dumps``.
        '''

        return json.dumps(self.dict(), default=_json_date, **kwargs)
