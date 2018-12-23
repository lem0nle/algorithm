# algorithm
[![Build Status](https://travis-ci.org/doggoesroof/algorithm.svg?branch=master)](https://travis-ci.org/doggoesroof/algorithm) [![Coverage Status](https://coveralls.io/repos/github/doggoesroof/algorithm/badge.svg)](https://coveralls.io/github/doggoesroof/algorithm)

Woof, coding learning!

## Stack
### attribute 
- push(self, e)
- pop(self), return lastobj
- top(self), return firstobj
### property
- len

## LinkedList
### attribute
- insert(self, obj, index=0)
- remove(self, index)
- find(self, obj), return index
- reverse(self)
### property
- len
- iter

## Heap
### attribute
- top(self), return firstobj
- pop(self), return lastobj
### property
- len

## PQ(Heap)
### attribute
- insert(self, ind, item)
- edit(self, ind, item)
- pop(self), return index and obj
### property
- len
- in

## Graph
Represent a graph with adjacency list
### attribute
- add_edge(self, s, t, w=1)
### property
- print with graphviz

## DenseGraph
Represent a graph with matrix
### attribute
- add_edge(self, s, t, w=1)
### property
- print with graphviz

## FloydAllPairsSP
### attribute
- dist(self, s, t)

## DijkstraSP
Initiate with a source vertex
### attribute
- dist(self, t)
