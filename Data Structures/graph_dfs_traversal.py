def dfs_traversal(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end='->')
    for next_node in graph[start] - visited:
        dfs_traversal(graph, next_node, visited)


if __name__ == '__main__':
    gdict = {"a": set(["b", "c"]),
             "b": set(["a", "d"]),
             "c": set(["a", "d"]),
             "d": set(["e"]),
             "e": set(["a"])
             }
    dfs_traversal(gdict, start='a')