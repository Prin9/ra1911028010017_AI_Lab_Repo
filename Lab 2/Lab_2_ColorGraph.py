class Graph:
    def __init__(self, edges, N):
        self.adj = [[] for _ in range(N)]
        for (src, dest) in edges:
            self.adj[src].append(dest)      #Assign and distribute undirected source/destination info int this as list of tuples within initialization
            self.adj[dest].append(src)

def colorGraph(graph):
    result = {}
    for u in range(N):
        assigned = set([result.get(i) for i in graph.adj[u] if i in result])  #set of colors assigned to adjacent vertices 
        color = 0
        for c in assigned:
            if color != c:              #Check if color doesn't match and return
                break
            color = color + 1           #Else move forward one index in color and then check
        result[u] = color
    for v in range(N):
        print("Color at vertex", v, " = ", colors[result[v]])

colors = ["BLUE","GREEN","RED","YELLOW","ORANGE","PINK","BLACK","BROWN","WHITE","PURPLE","VIOLET"]      #Color info
edges = [(0,1), (0,3), (1,4), (2,4), (3,4), (1,3), (2,3)]    #Edge info
N = 5                       #Number of Vertices
graph = Graph(edges, N)     #Initializa a Graph object
colorGraph(graph)           #Call driver color function
