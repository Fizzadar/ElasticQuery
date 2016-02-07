ElasticQuery Client
===================

The main ``ElasticQuery`` class allows you to build Elasticsearch queries using a Pythonic
API:

.. code:: python

    from elasticquery import ElasticQuery, Query, Aggregate

    # Create a new query
    q = ElasticQuery()

    # Match something
    q.query(Query.match('some_field', 'some_text'))

    # Aggregate something
    q.aggregate(Aggregate.terms('my_terms', 'some_field'))


API
---

.. automodule:: elasticquery.elasticquery
    :members:
    :undoc-members:


Exceptions
----------

.. automodule:: elasticquery.exceptions
    :members:
    :undoc-members:
