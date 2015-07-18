# ElasticQuery Filters API

Note that all Filter calls can also be passed additional keyword arguments not specified here, but no validation of inputs is done on them.

+ [geohash_shell](#method-filtergeohash_shell)
+ [geo_polygon](#method-filtergeo_polygon)
+ [exists](#method-filterexists)
+ [not_](#method-filternot_)
+ [nested](#method-filternested)
+ [prefix](#method-filterprefix)
+ [has_parent](#method-filterhas_parent)
+ [geo_distance_range](#method-filtergeo_distance_range)
+ [script](#method-filterscript)
+ [bool](#method-filterbool)
+ [type](#method-filtertype)
+ [terms](#method-filterterms)
+ [has_child](#method-filterhas_child)
+ [missing](#method-filtermissing)
+ [term](#method-filterterm)
+ [geo_shape](#method-filtergeo_shape)
+ [regexp](#method-filterregexp)
+ [or_](#method-filteror_)
+ [match_all](#method-filtermatch_all)
+ [geo_distance](#method-filtergeo_distance)
+ [geo_bounding_box](#method-filtergeo_bounding_box)
+ [and_](#method-filterand_)
+ [ids](#method-filterids)
+ [range](#method-filterrange)
+ [limit](#method-filterlimit)
+ [indices](#method-filterindices)

### class: Filter

##### method: Filter.geohash_shell

```py
Filter.geohash_shell(
    field,
    lat=None,
    lon=None
)
```

##### method: Filter.geo_polygon

```py
Filter.geo_polygon(
    field,
    [points]
)
```

##### method: Filter.exists

```py
Filter.exists(
    field
)
```

##### method: Filter.not_

```py
Filter.not_(
    filter=Filter,
    query=Query
)
```

##### method: Filter.nested

```py
Filter.nested(
    path,
    Filter
)
```

##### method: Filter.prefix

```py
Filter.prefix(
    field,
    value
)
```

##### method: Filter.has_parent

```py
Filter.has_parent(
    parent_type,
    filter=Filter,
    query=Query
)
```

##### method: Filter.geo_distance_range

```py
Filter.geo_distance_range(
    field,
    lat=None,
    lon=None
)
```

##### method: Filter.script

```py
Filter.script(
    script
)
```

##### method: Filter.bool

```py
Filter.bool(
    must=[Filter],
    must_not=[Filter],
    should=[Filter]
)
```

##### method: Filter.type

```py
Filter.type(
    value
)
```

##### method: Filter.terms

```py
Filter.terms(
    field,
    [value]
)
```

##### method: Filter.has_child

```py
Filter.has_child(
    type,
    filter=Filter,
    query=Query
)
```

##### method: Filter.missing

```py
Filter.missing(
    field
)
```

##### method: Filter.term

```py
Filter.term(
    field,
    value
)
```

##### method: Filter.geo_shape

```py
Filter.geo_shape(
    field,
    type=None,
    coordinates=[]
)
```

##### method: Filter.regexp

```py
Filter.regexp(
    field,
    value,
    flags=None,
    max_determinized_states=None
)
```

##### method: Filter.or_

```py
Filter.or_(
    [Filter]
)
```

##### method: Filter.match_all

```py
Filter.match_all(
    None
)
```

##### method: Filter.geo_distance

```py
Filter.geo_distance(
    field,
    lat=None,
    lon=None
)
```

##### method: Filter.geo_bounding_box

```py
Filter.geo_bounding_box(
    field,
    top_left=None,
    bottom_right=None
)
```

##### method: Filter.and_

```py
Filter.and_(
    [Filter]
)
```

##### method: Filter.ids

```py
Filter.ids(
    [values],
    type=None
)
```

##### method: Filter.range

```py
Filter.range(
    field,
    gte=None,
    gt=None,
    lte=None,
    lt=None
)
```

##### method: Filter.limit

```py
Filter.limit(
    value
)
```

##### method: Filter.indices

```py
Filter.indices(
    [indices],
    filter=Filter,
    no_match_filter=Filter
)
```
