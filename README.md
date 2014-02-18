# ElasticQuery

A _simple_ query builder for Elasticsearch.

+ [Example](#example)
+ [API](#api)
	- [ElasticQuery](#elasticquery-1)
	- [Filter](#filter)
	- [Query](#query)
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

#### query.must( Query/Filter )

#### query.should( Query/Filter )

#### query.must_not( Query/Filter )

#### query.sort( field, order )

#### query.aggregate( name, Aggregate )


### Filter

#### Filter.nested( path, musts, shoulds, must_nots )

#### Filter.range( field, range_from, range_to )

#### Filter.prefix( **kwargs )

#### Filter.term( **kwargs )

#### Filter.terms( **kwargs )


### Query

The `Query` class inherits from `Filter`, see above for API details.

#### Query.raw_string( string, default_operator='AND' )

#### Query.string( default_operator='AND', **kwargs )


### Aggregate

#### Aggregate.stats( field )

#### Aggregate.extended_stats( field )

#### Aggregate.histogram( field, interval )

#### Aggregate.date_histogram( field, interval='day' )

#### Aggregate.terms( field )

#### Aggregate.nested( path, **kwargs )



## Internals

`ElasticQuery` contains `.structure` which represents the final output. `Filter.*`, `Query.*` and `Aggregate.*` functions are essentially structs, each builds from its input and returns a dict representing the relevant json structure Elasticsearch wants.

Although there's multiple ways of doing most query/filter types in ES (ie `query['range'] = { 'to': 500 '}`), `ElasticQuery` stores everything inside a bool query. I have seen any performance degredation as a result and it makes for a far simpler way of managing queries. This way queries, filters and nested queries/filters can have none or more of `must`, `should` and `must_not` matches.