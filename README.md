# algorithm
[![Build Status](https://travis-ci.org/lem0nle/algorithm.svg?branch=master)](https://travis-ci.org/lem0nle/algorithm) [![Coverage Status](https://coveralls.io/repos/github/lem0nle/algorithm/badge.svg)](https://coveralls.io/github/lem0nle/algorithm)

Woof, coding learning!

## Stack
### method
- push(self, e)
- pop(self), return lastobj
- top(self), return firstobj
### magic method
- len

## LinkedList
### method
- insert(self, obj, index=0)
- remove(self, index)
- find(self, obj), return index
- reverse(self)
### magic method
- len
- iter

## Heap
### method
- top(self), return firstobj
- pop(self), return lastobj
### magic method
- len

## PQ(Heap)
### method
- insert(self, ind, item)
- edit(self, ind, item)
- pop(self), return index and obj
### magic method
- len
- in

## Graph
Represent a graph with adjacency list
### method
- add_edge(self, s, t, w=1)
### other
- print with graphviz

## DenseGraph
Represent a graph with matrix
### method
- add_edge(self, s, t, w=1)
### other
- print with graphviz

## FloydAllPairsSP
### method
- dist(self, s, t)

## DijkstraSP
Initiate with a source vertex
### method
- dist(self, t)
