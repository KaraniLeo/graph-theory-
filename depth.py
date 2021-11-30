from collections import defaultdict
  
class Graph:
   
    def __init__(x):
       
        x.graph=defaultdict(list)
      
   
    def addEdge(x,u,v):
        x.graph[u].append(v)
   
    def DFSUtil(x,v,visited):
       
        visited.add(v)
        print(v)
          
   
        for neighbour in x.graph[v]:
            if neighbour not in visited:
                x.DFSUtil(neighbour,visited)
        
    def DFS(x):
        
        visited=set()
       
        for vertex in x.graph:
            if vertex not in visited:
                x.DFSUtil(vertex,visited)

  
g=Graph()
g.addEdge(5,6)
g.addEdge(5,7)
g.addEdge(6,7)
g.addEdge(7,5)
g.addEdge(7,8)
g.addEdge(8,8)
print("Following is DFS from (starting from vertex 0)")
g.DFS()



