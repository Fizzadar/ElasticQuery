# ElasticQuery

A _simple_ query builder for Elasticsearch.

+ [Examples](#examples)
+ [API](#API)
	- [ElasticQuery](#ElasticQuery)
	- [Filter](#Filter)
	- [Query](#Query)
	- [Aggregate](#aggregate)
+ [Internals](#internals)


## Example

	from elasticquery import ElasticQuery, Filter, Query, Aggregate
	
	query = ElasticQuery()
	
	# Filter
	query.must( Filter.range( 'price', 0, 500 ))
	
	# Query
	query.should( Query.nested( 'nested_key', musts=[
		Query.terms( nested_key_key=['value'] ),
		Query.prefix( another_key='prefixed_with_' )
	]))
	
	# Aggregate
	query.aggregate( 'key_terms', Aggregate.terms( 'key' ))
	
	json = query.compile()


## API

### ElasticQuery

### Filter

### Query

### Aggregate



## Internals

`ElasticQuery` contains `.structure` which represents the final output. `Filter.*`, `Query.*` and `Aggregate.*` functions are essentially structs, each builds from its input and returns a dict representing the relevant json structure Elasticsearch wants.

Although there's multiple ways of doing most query/filter types in ES (ie `query['range'] = { 'to': 500 '}`), `ElasticQuery` stores everything inside a bool query. I have seen any performance degredation as a result and it makes for a far simpler way of managing queries. This way queries, filters and nested queries/filters can have none or more of `must`, `should` and `must_not` matches.