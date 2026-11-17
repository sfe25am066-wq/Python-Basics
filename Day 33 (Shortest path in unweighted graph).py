from collections import deque
graph={
    'A':['B','C'],
    'B':['D'],
    'C':['D'],
    'D':[]
}
def shortest_path(start,end):
    queue=deque([[start]])
    while queue:
        path=queue.popleft()
        node=path[-1]
        if node==end:
            return path
        for neighbour in graph[node]:
            new_path=list(path)
            new_path.append(neighbour)
            queue.append(new_path)
print(shortest_path('A','D'))