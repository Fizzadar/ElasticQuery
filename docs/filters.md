# ElasticQuery Filters API

Note that all Filter calls can also be passed additional keyword arguments not specified here, but no validation of inputs is done on them.

### geohash_shell

`Filter.geohash_shell(field, lat=None, lon=None)`

### geo_polygon

`Filter.geo_polygon(field, [])`

### exists

`Filter.exists(field)`

### nested

`Filter.nested(path, Filter)`

### geo_shape

`Filter.geo_shape(field, type=None, coordinates=[])`

### prefix

`Filter.prefix(field, value)`

### has_parent

`Filter.has_parent(parent_type, filter=Filter, query=Query)`

### query

`Filter.query(Query)`

### geo_distance_range

`Filter.geo_distance_range(field, lat=None, lon=None)`

### script

`Filter.script(script)`

### bool

`Filter.bool(must=[Filter], must_not=[Filter], should=[Filter])`

### type

`Filter.type(value)`

### terms

`Filter.terms(field, [])`

### has_child

`Filter.has_child(type, filter=Filter, query=Query)`

### missing

`Filter.missing(field)`

### term

`Filter.term(field, value)`

### not

`Filter.not(filter=Filter, query=Query)`

### regexp

`Filter.regexp(field, value, flags=None, max_determinized_states=None)`

### or_

`Filter.or_([Filter])`

### match_all

`Filter.match_all(None)`

### geo_distance

`Filter.geo_distance(field, lat=None, lon=None)`

### geo_bounding_box

`Filter.geo_bounding_box(field, top_left=None, bottom_right=None)`

### and_

`Filter.and_([Filter])`

### ids

`Filter.ids([], type=None)`

### range

`Filter.range(field, gte=None, gt=None, lte=None, lt=None)`

### limit

`Filter.limit(value)`

### indices

`Filter.indices([], filter=Filter, no_match_filter=Filter)`
