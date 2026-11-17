def dfs(graph,vertex,visited=None):
    if visited is None:
        visited=set()
    visited.add(vertex)
    print(vertex,end="")
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
    }
print("DFS Traversal:")
dfs(graph,'A')