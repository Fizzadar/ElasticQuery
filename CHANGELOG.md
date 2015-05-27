# v2.0

+ Complete rewrite, see docs/v1_to_v2.md for breaking changes, summary:
    * Full support for ES 1.5.2 queries, filters and aggregates
    * Extensible DSL builder replaces manually handled methods
    * Proper testing for each query/filter/aggregate and combined queries


# v1.9.7

+ Add boost support to filtered query

# v1.9.6

+ Add `precision_threshold` to `Aggregate.cardinality`

# v1.9.5

+ Add `min_doc_count=1` to `Aggregate.date_histogram`

# v1.9.4

+ Add support for `Aggregate.cardinality`

# v1.9.3

+ Add support for `Filter.multi_match`

# v1.9.2

+ Add support for `Filter.bool`

# v1.9.1

+ Add `Filter.fuzzy_like_this`
+ Add `Filter.filtered`

# v1.9.0

+ **Breaking change**: rename `ElasticQuery.limit` -> `ElasticQuery.size` to be more inline with Elasticsearch
+ Add `cache=False` to `Filter.raw_string` and `Filter.string`

# v1.8.2

+ Stupid bugfix

# v1.8.1

+ Fix for timeout: append 's' on the end (changable via `time_type` kwarg)

# v1.8

+ Add `Query.constant_score`
+ Add `ElasticQuery.filter` and `ElasticQuery.query` as options instead of using `.must`, `.should` & `.must_not`
+ Add `ElasticQuery.timeout`
+ Tidy up `ElasticQuery.offset` and `ElasticQuery.limit`
+ Creates query structure on demand (empty query is now properly empty)

# v1.7

+ Add `execution` to terms filter

# v1.6

+ Remove field checking with `ElasticMapping` (incompatible with nested fields, needs rethink)

# v1.5

+ Add `match` filter + query
+ Add `range` aggregation

# v1.4

+ Add `reverse_nested` aggregation

# v1.3

+ Much improved method for creating sub-aggregates

# v1.2

+ Convert datetimes -> isoformat in range

# v1.1

+ Fix bug with field count on Aggregate

# v1.0

Major reshuffle.

+ Can be passed ES client, index & doc_type to execute queries
+ Supports working with `ElasticMapping`
+ Add example, much improved docs
+ Fix bug with `default=[]`
