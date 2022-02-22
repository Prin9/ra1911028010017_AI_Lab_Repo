graphStat = {
  '1' : ['2','3'],
  '2' : ['4'],
  '3' : ['6'],
  '4' : ['5', '6'],
  '5' : [],
  '6' : ['1']
}

visited = [] 
queue = []   
 
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0) 
        print(s) 
        for neighbour in graph[s]:
              if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
 
bfs(visited, graphStat, '1')
