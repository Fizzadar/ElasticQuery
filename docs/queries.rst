Queries
=======

Note that all Query calls can also be passed additional keyword arguments not specified here, but no validation of inputs is done on them.




Query.geo_polygon
~~~~~~~~~~~~~~~~~

.. code:: python

    Query.geo_polygon(field, [points])


Query.terms
~~~~~~~~~~~

.. code:: python

    Query.terms(field, [value])


Query.simple_query_string
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Query.simple_query_string(query, fields=[])


Query.missing
~~~~~~~~~~~~~

.. code:: python

    Query.missing(field)


Query.span_containing
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Query.span_containing(Query, Query)


Query.span_multi
~~~~~~~~~~~~~~~~

.. code:: python

    Query.span_multi(Query)


Query.geohash_cell
~~~~~~~~~~~~~~~~~~

.. code:: python

    Query.geohash_cell(field, lat=None, lon=None)


Query.boosting
~~~~~~~~~~~~~~

.. code:: python

    Query.boosting(positive=None, negative=None)


Query.function_score
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Query.function_score([functions], query=Query)


Query.term
~~~~~~~~~~

.. code:: python

    Query.term(field, value, boost=None)


Query.nested
~~~~~~~~~~~~

.. code:: python

    Query.nested(path, Query)


Query.dis_max
~~~~~~~~~~~~~

.. code:: python

    Query.dis_max([Query])


Query.indices
~~~~~~~~~~~~~

.. code:: python

    Query.indices([indices], query=Query, no_match_query=Query)


Query.prefix
~~~~~~~~~~~~

.. code:: python

    Query.prefix(field, value, boost=None)


Query.geo_distance_range
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Query.geo_distance_range(field, lat=None, lon=None)


Query.has_parent
~~~~~~~~~~~~~~~~

.. code:: python

    Query.has_parent(parent_type, query=Query)


Query.fuzzy
~~~~~~~~~~~

.. code:: python

    Query.fuzzy(field, value, boost=None, fuzziness=None, prefix_length=None, max_expansions=None)


Query.geo_shape
~~~~~~~~~~~~~~~

.. code:: python

    Query.geo_shape(field, type=None, coordinates=[])


Query.regexp
~~~~~~~~~~~~

.. code:: python

    Query.regexp(field, value, boost=None, flags=None)


Query.span_or
~~~~~~~~~~~~~

.. code:: python

    Query.span_or([Query])


Query.more_like_this
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Query.more_like_this([fields], like_text)


Query.match_all
~~~~~~~~~~~~~~~

.. code:: python

    Query.match_all(boost=None)


Query.geo_distance
~~~~~~~~~~~~~~~~~~

.. code:: python

    Query.geo_distance(field, lat=None, lon=None)


Query.span_near
~~~~~~~~~~~~~~~

.. code:: python

    Query.span_near([Query])


Query.exists
~~~~~~~~~~~~

.. code:: python

    Query.exists(field)


Query.multi_match
~~~~~~~~~~~~~~~~~

.. code:: python

    Query.multi_match([fields], query)


Query.geo_bounding_box
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Query.geo_bounding_box(field, top_left=None, bottom_right=None)


Query.span_term
~~~~~~~~~~~~~~~

.. code:: python

    Query.span_term(field, value, boost=None)


Query.span_within
~~~~~~~~~~~~~~~~~

.. code:: python

    Query.span_within(Query, Query)


Query.ids
~~~~~~~~~

.. code:: python

    Query.ids([values], type=None)


Query.has_child
~~~~~~~~~~~~~~~

.. code:: python

    Query.has_child(type, query=Query)


Query.range
~~~~~~~~~~~

.. code:: python

    Query.range(field, gte=None, gt=None, lte=None, lt=None)


Query.bool
~~~~~~~~~~

.. code:: python

    Query.bool(must=[Query], must_not=[Query], should=[Query])


Query.common
~~~~~~~~~~~~

.. code:: python

    Query.common(query)


Query.wildcard
~~~~~~~~~~~~~~

.. code:: python

    Query.wildcard(field, value, boost=None)


Query.span_first
~~~~~~~~~~~~~~~~

.. code:: python

    Query.span_first(Query)


Query.query_string
~~~~~~~~~~~~~~~~~~

.. code:: python

    Query.query_string(query, fields=[])


Query.limit
~~~~~~~~~~~

.. code:: python

    Query.limit(value)


Query.span_not
~~~~~~~~~~~~~~

.. code:: python

    Query.span_not(include=Query, exclude=Query)


Query.type
~~~~~~~~~~

.. code:: python

    Query.type(value)


Query.constant_score
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Query.constant_score(query=Query)


Query.match
~~~~~~~~~~~

.. code:: python

    Query.match(field, query, operator=None, zero_terms_query=None, cutoff_frequency=None, boost=None)

