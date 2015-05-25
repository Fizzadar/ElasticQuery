# ElasticQuery Filters API

### `Filter.geohash_shell(lat=None, lon=None)`

### `Filter.geo_polygon(field, [])`

### `Filter.exists(field)`

### `Filter.nested(path, Filter)`

### `Filter.geo_shape(type=None, coordinates=[])`

### `Filter.prefix(field, value)`

### `Filter.has_parent(parent_type, filter=Filter, query=Query)`

### `Filter.query(Query)`

### `Filter.geo_distance_range(lat=None, lon=None)`

### `Filter.script(script)`

### `Filter.bool(must=[Filter], must_not=[Filter], should=[Filter])`

### `Filter.type(value)`

### `Filter.terms(field, [])`

### `Filter.has_child(type, filter=Filter, query=Query)`

### `Filter.missing(field)`

### `Filter.term(field, value)`

### `Filter.not(filter=Filter, query=Query)`

### `Filter.regexp(field, value, flags=None, max_determinized_states=None)`

### `Filter.or_([Filter])`

### `Filter.match_all(None)`

### `Filter.geo_distance(lat=None, lon=None)`

### `Filter.geo_bounding_box(top_left=None, bottom_right=None)`

### `Filter.and_([Filter])`

### `Filter.ids([], type=None)`

### `Filter.range(gte=None, gt=None, lte=None, lt=None)`

### `Filter.limit(value)`

### `Filter.indices([], filter=Filter, no_match_filter=Filter)`
