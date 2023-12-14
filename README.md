[![Build & Tests](https://github.com/jmrenier13/DelauneyMesh/actions/workflows/build-tests.yml/badge.svg)](https://github.com/jmrenier13/DelauneyMesh/actions/workflows/build-tests.yml)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/jmrenier13/DelauneyMesh/blob/main/LICENSE)
[![codecov](https://codecov.io/gh/jmrenier13/DelauneyMesh/branch/main/graph/badge.svg?token=THJ84SUYUT)](https://codecov.io/gh/jmrenier13/DelauneyMesh)

A 2D delauney mesh generation algorithm

## Navigation

- [How to install](#how-to-install)
- [Project structure](#project-structure)
- [List of properties](#list-of-properties)
    - [Properties of `Node` instance](#properties-of-node-instance)
    - [Properties of `Edge` instance](#properties-of-edge-instance)
- [List of methods](#list-of-methods)
    - [Methods of `Edge` instance](#methods-of-edge-instance)

## How to install

Run the following command

```shell
to add command later
```

## Project structure

* `Node` class - structure for nodes.
* `Edge` class - structure for edges.

## List of properties

### Properties of `Node` instance

* `x` - coordinate in the x dimension.
* `y` - coordinate in the y dimension.

### Properties of `Edge` instance

* `center` - center of edge.
* `enforced` - if the edge in enforced.
* `length` - length of edge.
* `normal` - normal vector.
* `vector` - edge vector.

## List of methods

### Methods of `Edge` instance

* `split` - split edge via point.
