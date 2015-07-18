# ElasticQuery Aggregates API

Note that all Aggregate calls can also be passed additional keyword arguments not specified here, but no validation of inputs is done on them.

+ [geo_bounds](#method-aggregategeo_bounds)
+ [date_histogram](#method-aggregatedate_histogram)
+ [global](#method-aggregateglobal)
+ [nested](#method-aggregatenested)
+ [ip_range](#method-aggregateip_range)
+ [filters](#method-aggregatefilters)
+ [avg](#method-aggregateavg)
+ [children](#method-aggregatechildren)
+ [stats](#method-aggregatestats)
+ [scripted_metric](#method-aggregatescripted_metric)
+ [min](#method-aggregatemin)
+ [sum](#method-aggregatesum)
+ [extended_stats](#method-aggregateextended_stats)
+ [value_count](#method-aggregatevalue_count)
+ [percentiles](#method-aggregatepercentiles)
+ [terms](#method-aggregateterms)
+ [missing](#method-aggregatemissing)
+ [max](#method-aggregatemax)
+ [histogram](#method-aggregatehistogram)
+ [date_range](#method-aggregatedate_range)
+ [cardinality](#method-aggregatecardinality)
+ [geohash_grid](#method-aggregategeohash_grid)
+ [geo_distance](#method-aggregategeo_distance)
+ [filter](#method-aggregatefilter)
+ [percentile_ranks](#method-aggregatepercentile_ranks)
+ [range](#method-aggregaterange)
+ [significant_terms](#method-aggregatesignificant_terms)
+ [top_hits](#method-aggregatetop_hits)
+ [reverse_nested](#method-aggregatereverse_nested)

### class: Aggregate

##### method: Aggregate.geo_bounds

```py
Aggregate.geo_bounds(
    name,
    field
)
```

##### method: Aggregate.date_histogram

```py
Aggregate.date_histogram(
    name,
    field,
    interval
)
```

##### method: Aggregate.global

```py
Aggregate.global(
    name
)
```

##### method: Aggregate.nested

```py
Aggregate.nested(
    name,
    path
)
```

##### method: Aggregate.ip_range

```py
Aggregate.ip_range(
    name,
    field,
    [ranges]
)
```

##### method: Aggregate.filters

```py
Aggregate.filters(
    name,
    [Filter]
)
```

##### method: Aggregate.avg

```py
Aggregate.avg(
    name,
    field
)
```

##### method: Aggregate.children

```py
Aggregate.children(
    name,
    type
)
```

##### method: Aggregate.stats

```py
Aggregate.stats(
    name,
    field
)
```

##### method: Aggregate.scripted_metric

```py
Aggregate.scripted_metric(
    name
)
```

##### method: Aggregate.min

```py
Aggregate.min(
    name,
    field
)
```

##### method: Aggregate.sum

```py
Aggregate.sum(
    name,
    field
)
```

##### method: Aggregate.extended_stats

```py
Aggregate.extended_stats(
    name,
    field
)
```

##### method: Aggregate.value_count

```py
Aggregate.value_count(
    name,
    field
)
```

##### method: Aggregate.percentiles

```py
Aggregate.percentiles(
    name,
    field
)
```

##### method: Aggregate.terms

```py
Aggregate.terms(
    name,
    field
)
```

##### method: Aggregate.missing

```py
Aggregate.missing(
    name,
    field
)
```

##### method: Aggregate.max

```py
Aggregate.max(
    name,
    field
)
```

##### method: Aggregate.histogram

```py
Aggregate.histogram(
    name,
    field,
    interval
)
```

##### method: Aggregate.date_range

```py
Aggregate.date_range(
    name,
    field,
    [ranges]
)
```

##### method: Aggregate.cardinality

```py
Aggregate.cardinality(
    name,
    field
)
```

##### method: Aggregate.geohash_grid

```py
Aggregate.geohash_grid(
    name,
    field
)
```

##### method: Aggregate.geo_distance

```py
Aggregate.geo_distance(
    name,
    field,
    origin,
    [ranges]
)
```

##### method: Aggregate.filter

```py
Aggregate.filter(
    name,
    Filter
)
```

##### method: Aggregate.percentile_ranks

```py
Aggregate.percentile_ranks(
    name,
    field
)
```

##### method: Aggregate.range

```py
Aggregate.range(
    name,
    field,
    [ranges]
)
```

##### method: Aggregate.significant_terms

```py
Aggregate.significant_terms(
    name,
    field
)
```

##### method: Aggregate.top_hits

```py
Aggregate.top_hits(
    name
)
```

##### method: Aggregate.reverse_nested

```py
Aggregate.reverse_nested(
    name
)
```
