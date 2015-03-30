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
