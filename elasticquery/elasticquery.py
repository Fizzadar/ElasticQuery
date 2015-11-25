# ElasticQuery
# File: elasticquery.py
# Desc: ElasticQuery itself

import json

from .queries import Query
from .dsl_util import unroll_struct
from .exception import NoESClient, NoIndexName, NoDocType


def _json_date(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError('{0} is not JSON serializable'.format(obj))


class ElasticQuery(object):
    '''A class for building ES queries'''
    _es = None
    _index = None
    _doc_type = None

    _filter = _query = None

    def __init__(self, es=None, index=None, doc_type=None):
        self._es = es
        self._index = index
        self._doc_type = doc_type

        self._aggs = []
        self._suggesters = []

        # An empty query
        self._struct = {}

    def query(self, query):
        self._query = query

    def filter(self, filter_):
        self._filter = filter_

    def aggregate(self, *aggregates):
        self._aggs.extend(aggregates)

    def suggest(self, *suggesters):
        self._suggesters.extend(suggesters)

    def set(self, key, value):
        '''Set an arbitrary attribute on this query.'''
        self._struct[key] = value
        return self

    def from_(self, from_):
        self._struct['from'] = from_
        return self

    def size(self, size):
        self._struct['size'] = size
        return self

    def timeout(self, timeout):
        self._struct['timeout'] = timeout
        return self

    def fields(self, fields):
        self._struct['_source'] = fields
        return self

    def sort(self, field, order=None):
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
        if self._filter and self._query:
            self._struct['query'] = Query.filtered(
                filter=self._filter,
                query=self._query
            )
        elif self._filter:
            self._struct['query'] = Query.filtered(
                filter=self._filter
            )
        elif self._query:
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
        '''Execute the current query (requires _es, _index & _doc_type).'''
        if self._es is None:
            raise NoESClient()
        if self._index is None:
            raise NoIndexName()
        if self._doc_type is None:
            raise NoDocType()

        return self._es.search(
            index=self._index,
            doc_type=self._doc_type,
            body=self.dict()
        )

    def json(self, **kwargs):
        return json.dumps(self.dict(), default=_json_date, **kwargs)

    def __str__(self):
        return self.json(indent=4)
