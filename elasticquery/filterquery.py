# ElasticQuery
# File: elasticquery/filterquery.py
# Desc: The base query class & metaclass

import json

from .util import make_dsl_object, unroll_definitions, unroll_struct


class MetaFilterQuery(type):
    def __init__(cls, name, bases, d):
        super(MetaFilterQuery, cls).__init__(name, bases, d)
        unroll_definitions(cls._definitions)

    def __getattr__(cls, key):
        if key == '__test__':
            return None

        if key not in cls._definitions:
            raise cls._exception(key)

        return lambda *args, **kwargs: make_dsl_object(
            cls, key, cls._definitions[key],
            *args, **kwargs
        )


class BaseFilterQuery(object):
    _type = None
    _struct = None
    _dsl_type = None

    def __init__(self, dsl_type, struct):
        self._struct = struct
        self._dsl_type = dsl_type

    def dict(self):
        dsl_type = self._dsl_type[:1] if self._dsl_type.endswith('_') else self._dsl_type

        return {
            dsl_type: unroll_struct(self._struct)
        }

    def __str__(self):
        return json.dumps(self.dict(), indent=4)
