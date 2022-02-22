from queue import PriorityQueue
v =int(input("Enter Number of Vertices - "))
e = int(input("Enter Number of Edges - "))
graph = [[] for i in range(v)]
def best_first_search(source, target, n):
  visited = [0] * n
  visited[0] = True
  pq = PriorityQueue()
  pq.put((0, source))
  while pq.empty() == False:
    u = pq.get()[1]
    print(u, end=" ")
    if u == target:
      break
    for v, c in graph[u]:
      if visited[v] == False:
        visited[v] = True
        pq.put((c, v))
#  print()
def addedge(x, y, cost):
  graph[x].append((y, cost))
  graph[y].append((x, cost))
  
print("\nEnter Edge Parameters - \n")
for i in range(v):
    a=int(input("Edge source - "))
    b=int(input("Edge destination - "))
    c=int(input("Edge cost - "))
    addedge(a,b,c)
    print("\n")


source = int(input("Source Vertex - "))
target = int(input("Target Vartex - "))
print("\n\nPath = ")
best_first_search(source, target, v)

