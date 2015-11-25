# ElasticQuery
# File: elasticquery/filterquery.py
# Desc: The base queryfilter/aggregate classes & metaclasses

import json

from .dsl_util import make_struct, unroll_definitions, unroll_struct


class MetaFilterQuery(type):
    '''Metaclass mapping attributes to dsl objects on Filter/Query getattr.'''
    def __init__(cls, name, bases, d):
        super(MetaFilterQuery, cls).__init__(name, bases, d)
        unroll_definitions(cls._definitions)

    def __getattr__(cls, key):
        if key == '__test__':
            return None

        if key not in cls._definitions:
            raise cls._exception(key)

        # Generates a new class object with a struct based on the definitions
        return lambda *args, **kwargs: cls(
            key,
            make_struct(cls._definitions[key], *args, **kwargs)
        )

class MetaAggregate(MetaFilterQuery):
    '''Modified MetaFilterQuery.MetaAggregate getattr to handle aggregate names.'''
    def __getattr__(cls, key):
        if key == '__test__':
            return None

        if key not in cls._definitions:
            raise cls._exception(key)

        return lambda *args, **kwargs: cls(
            key,
            args[0],
            make_struct(cls._definitions[key], *args[1:], **kwargs)
        )

class MetaSuggester(MetaFilterQuery):
    '''Modified MetaFilterQuery.MetaSuggester getattr to handle suggester names and text.'''
    def __getattr__(cls, key):
        if key == '__test__':
            return None

        if key not in cls._definitions:
            raise cls._exception(key)

        return lambda *args, **kwargs: cls(
            key,
            args[0],
            args[1],
            make_struct(cls._definitions[key], *args[2:], **kwargs)
        )

class BaseFilterQuery(object):
    '''The base class which represents a Filter/Query struct.'''
    _struct = None
    _dsl_type = None

    def __init__(self, dsl_type, struct):
        self._dsl_type = dsl_type
        self._struct = struct

    def dict(self):
        # Handle reserved Python keyword alternatives (from_, or_)
        dsl_type = self._dsl_type[:-1] if self._dsl_type.endswith('_') else self._dsl_type

        return {
            dsl_type: unroll_struct(self._struct)
        }

    def __str__(self):
        return json.dumps(self.dict(), indent=4)

class BaseAggregate(BaseFilterQuery):
    '''Modified BaseFilterQuery to handle aggregate name storage.'''
    _name = None

    def __init__(self, dsl_type, name, struct):
        self._dsl_type = dsl_type
        self._struct = struct
        self._name = name

        self._aggs = []

    def dict(self):
        struct = {
            self._name: {
                self._dsl_type: unroll_struct(self._struct)
            }
        }

        if self._aggs:
            aggregates = {}

            for agg in self._aggs:
                aggregates.update(agg.dict())

            struct[self._name]['aggregations'] = aggregates

        return struct

    def aggregate(self, *aggregates):
        self._aggs.extend(aggregates)
        return self

class BaseSuggester(BaseFilterQuery):
    '''Modified BaseFilterQuery to handle suggester name & text storage.'''
    _name = None

    def __init__(self, dsl_type, name, text, struct):
        self._dsl_type = dsl_type
        self._struct = struct
        self._name = name
        self._text = text

        self._suggs = []

    def dict(self):
        struct = {
            self._name: {
                "text": self._text,
                self._dsl_type: unroll_struct(self._struct)
            }
        }

        if self._suggs:
            for sugg in self._suggs:
                struct.update(sugg.dict())

        return struct
