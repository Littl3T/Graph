from graph import Graph


"""
You can create an empy graph using Graph()

Add a vertex by using .addVertex(name) => it creates a new vertex "name" in your graph.
Delete a vertex by using .deleteVertex(name) => it deletes the vertex "name" from your graph

Add an edge connecting two vertex "A" and "B" with a travel cost "value" by using .addEdge(A,B,value) => creates an edge

Delete an edge by using .deleteEdge(A,B) =>It deletes the edge connecting the vertex "A" and "B"

Get the neighbors of a vertex "A" using .checkNeighbor(A)

Get the Adjacency Matrix between all vertex using .adjacencyMatrix() => Returns a Matrix

Get the shortest path between A and B using .dijkstra(A,B) => Returns the path of vertex from A to B

Get the shortest path Matrix between all vertex using .floydWarshall() => Returns a Matrix

Visualize a Matrix using .showMatrix(matrix) => "matrix" will be printed correctly on your terminal

Get the Spanning Tree of a graph using .Kruskal() => Returns a Graph
"""


graph = Graph()

graph.addVertex('A')
graph.addVertex('B')
graph.addVertex('C')
graph.addVertex('D')

graph.addEdge('A','B',5)
graph.addEdge('A','C',1)
graph.addEdge('C','B',2)
graph.addEdge('A','D',2)

print("Edges of the graph:", graph.edges)
print("Vertex of the graph:", graph.vertex)

print("-"*20)
print("Adjency Matrix")
adjency_matrix = graph.adjacencyMatrix()
graph.showMatrix(adjency_matrix)

print("-"*20)
print("Floyd Warshall Matrix")
floyd_warshall = graph.floydWarshall()
graph.showMatrix(floyd_warshall)

print("-"*20)
print("Shortest path between C and D")
print(graph.dijkstra('C', 'D'))

print("-"*20)
print("Edges of the spanning tree : ", graph.Kruskal().edges)
print("Vertex of the spanning tree: ", graph.Kruskal().vertex)