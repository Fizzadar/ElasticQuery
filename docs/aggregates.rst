Aggregates
==========

Note that all Aggregate calls can also be passed additional keyword arguments not specified here, but no validation of inputs is done on them.




Aggregate.bucket_script
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.bucket_script(name, {})


Aggregate.extended_stats_bucket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.extended_stats_bucket(name, buckets_path)


Aggregate.global
~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.global(name)


Aggregate.nested
~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.nested(name, path)


Aggregate.ip_range
~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.ip_range(name, field, [ranges])


Aggregate.filters
~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.filters(name, [Query])


Aggregate.children
~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.children(name, type)


Aggregate.scripted_metric
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.scripted_metric(name)


Aggregate.top_hits
~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.top_hits(name)


Aggregate.extended_stats
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.extended_stats(name, field)


Aggregate.value_count
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.value_count(name, field)


Aggregate.date_histogram
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.date_histogram(name, field, interval)


Aggregate.sampler
~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.sampler(name, field)


Aggregate.derivative
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.derivative(name, buckets_path)


Aggregate.sum_bucket
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.sum_bucket(name, buckets_path)


Aggregate.max_bucket
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.max_bucket(name, buckets_path)


Aggregate.histogram
~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.histogram(name, field, interval)


Aggregate.date_range
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.date_range(name, field, [ranges])


Aggregate.cardinality
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.cardinality(name, field)


Aggregate.geohash_grid
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.geohash_grid(name, field)


Aggregate.geo_distance
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.geo_distance(name, field, origin, [ranges])


Aggregate.bucket_selector
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.bucket_selector(name, {})


Aggregate.percentiles_bucket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.percentiles_bucket(name, buckets_path)


Aggregate.percentile_ranks
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.percentile_ranks(name, field)


Aggregate.cumulative_sum
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.cumulative_sum(name, buckets_path)


Aggregate.moving_avg
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.moving_avg(name, buckets_path)


Aggregate.geo_bounds
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.geo_bounds(name, field)


Aggregate.stats_bucket
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.stats_bucket(name, buckets_path)


Aggregate.avg_bucket
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.avg_bucket(name, buckets_path)


Aggregate.avg
~~~~~~~~~~~~~

.. code:: python

    Aggregate.avg(name, field)


Aggregate.stats
~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.stats(name, field)


Aggregate.min
~~~~~~~~~~~~~

.. code:: python

    Aggregate.min(name, field)


Aggregate.sum
~~~~~~~~~~~~~

.. code:: python

    Aggregate.sum(name, field)


Aggregate.percentiles
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.percentiles(name, field)


Aggregate.min_bucket
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.min_bucket(name, buckets_path)


Aggregate.terms
~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.terms(name, field)


Aggregate.missing
~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.missing(name, field)


Aggregate.max
~~~~~~~~~~~~~

.. code:: python

    Aggregate.max(name, field)


Aggregate.geo_centroid
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.geo_centroid(name, field)


Aggregate.serial_diff
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.serial_diff(name, buckets_path)


Aggregate.filter
~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.filter(name, Query)


Aggregate.range
~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.range(name, field, [ranges])


Aggregate.significant_terms
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.significant_terms(name, field)


Aggregate.reverse_nested
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    Aggregate.reverse_nested(name)

