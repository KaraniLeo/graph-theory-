from collections import defaultdict
 

class Graph:
 
 
    def __init__(breath):
 
       
        breath.graph = defaultdict(list)
 
    
    def addEdge(breath,u,v):
        breath.graph[u].append(v)
 
  
    def BFS(breath, s):
 
       
        visited = [False] * (max(breath.graph) + 1)
 
    
        queue = []
 
        queue.append(s)
        visited[s] = True
 
        while queue:
 
           
            s = queue.pop(0)
            print (s, end = ",")
 
            for i in breath.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 1)")
g.BFS(1)
 
