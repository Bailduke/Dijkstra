# Dijkstra

Dijkstra is a simple algorithm to find the shortest path in highly connected networks.

## Objects definition

### Graph

Given a dictionary that have tuples as keys:
```python
d = {
    (i,j): d_ij,
    ...
}
```

The `Graph` object stores:
- `d`: the edge weight dictionary
- `i`: list of from nodes (one per edge)
- `j`: list of to nodes (one per edge)
- `n`: number of edges

### Tag

A `Tag` represents the current best-known distance to a node:
- `d_startj`: shortest distance found from the start node to `j`
- `i`: list of predecessor nodes that achieve this same shortest distance (multiple when ties occur)

All tags live in a dictionary called `table` mapping `j -> Tag`.

## Algorithm

### Iteration
A single iteration processes a set of origin nodes `it_i` (the new destination nodes from the previous step):

```python
table, it_i = iteration(table, graph, it_i)
```

For each `i` in `it_i`, consider outgoing edges `(i, j)`. If `d_start_i + d_ij` improves the known distance to `j`, update `table[j]`. If it ties, append `i` to `table[j].i` (alternative path). Newly discovered/improved `j` nodes form the next `it_i`.

### Dijkstra

The main function computes the next iteration only if there is a non empty `it_i` or if the max number of iterations is reached.