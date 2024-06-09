from vertex import Vertex
from edge import Edge
import heapq


class Graph:
    def __init__(self, vertex=None, edges=None):
        self.__vertex = vertex
        self.__edges = edges
        if self.__edges is None:
            self.__edges = []
        if self.__vertex is None:
            self.__vertex = []

    def getVertex(self, name):
        # Get a vertex with its name
        for vertex in self.__vertex:
            if name == vertex.name:
                return vertex

    def getEdge(self, vertexA, vertexB):
        # Get an edge with the two vertex connected.
        for edges in self.__edges:
            if (edges.A == vertexA and edges.B == vertexB) or (edges.A == vertexB and edges.B == vertexA):
                return edges
        return None

    def getEdgeValue(self, vertexA, vertexB):
        # Returns the value of the edge connecting two vertex
        edge = self.getEdge(vertexA, vertexB)
        if edge is None:
            return 0
        else:
            return edge.value

    def addVertex(self, vertex_name):
        # Create a vertex using the name in the method
        self.__vertex.append(Vertex(vertex_name))

    def deleteVertex(self, vertex_name):
        # First has to get the vertex object with the name in the method.
        # Then check if it's in the graph list. and remove it.
        vertex = self.getVertex(vertex_name)
        if vertex in self.__vertex:
            for edges in self.__edges:
                if edges.A == vertex:
                    self.deleteEdge(edges.A, vertex)
                elif edges.B == vertex:
                    self.deleteEdge(vertex, edges.B)
            self.__vertex.remove(vertex)

    def addEdge(self, vertexA_name, vertexB_name, value):
        # First get the two vertex from the method.
        # Then check if they are both existing and process to create the edge between them.
        # Finally, adding it to the graph edges list
        vertexA = self.getVertex(vertexA_name)
        vertexB = self.getVertex(vertexB_name)
        if vertexB is not None and vertexA is not None:
            self.__edges.append(Edge(vertexA, vertexB, value))

    def deleteEdge(self, vertexA_name, vertexB_name):
        # Checks if the edge from both point creating it, is existing
        # If it is, it removes it from the graph and deletes the vertex in it
        edge = self.getEdge(self.getVertex(vertexA_name), self.getVertex(vertexB_name))
        if edge in self.__edges:
            edge.A = None
            edge.B = None
            self.__edges.remove(edge)

    def checkNeighbor(self, vertex_name):
        # For all the edges in the graph. it checks both points from them.
        # If the point is the edges A, then the neighbor is B
        # If the point is the edges B, then the neighbor is A
        # If none of those are in the edges. The is no neighbor
        vertex = self.getVertex(vertex_name)
        neighbors = []
        for edges in self.__edges:
            if edges.A == vertex:
                neighbors.append(edges.B)
            elif edges.B == vertex:
                neighbors.append(edges.A)
        if not neighbors:
            return None
        else:
            return neighbors

    def adjacencyMatrix(self):
        # Adjacency Matrix is a square array with the save of the number of vertex in the graph
        # If we have self.__vertex = ['A', 'B', 'C']... Then the array would be:
        #       A   B   C
        #   A   x   x   x
        #   B   x   x   x
        #   C   x   x   x
        # With x representing the value of the edge connecting the two vertex.
        row, columns = len(self.__vertex), len(self.__vertex)
        matrix = []
        for n in range(row):
            r = []
            for c in range(columns):
                value = self.getEdgeValue(self.__vertex[n], self.__vertex[c])
                r.append(value)
            matrix.append(r)
        return matrix

    def showMatrix(self, matrix):
        # Representing the Matrix in a beautiful way. Rows and Columns oriented correctly.
        columns_names = [" "]
        for vertex in self.__vertex:
            columns_names.append(vertex.name)
        print(" ".join(columns_names))
        x = 0
        for rows in matrix:
            rows.insert(0, self.__vertex[x].name)
            for element in rows:
                print(element,end=" ")
            print('')
            x += 1

    def dijkstra(self, vertexA_name: str, vertexB_name: str) -> tuple:
        # Gives the shortest path between two vertex A and B
        # Returns a list of vertex as a path from A to B
        vertexA = self.getVertex(vertexA_name)
        vertexB = self.getVertex(vertexB_name)

        distances = {vertex: float('inf') for vertex in self.__vertex}
        previous_vertices = {vertex: None for vertex in self.__vertex}
        distances[vertexA] = 0
        priority_queue = [(0, vertexA)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex == vertexB:
                break

            if current_distance > distances[current_vertex]:
                continue

            for neighbor in self.checkNeighbor(current_vertex.name):
                edge_value = self.getEdgeValue(current_vertex, neighbor)
                distance = current_distance + edge_value

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        path, current_vertex = [], vertexB
        while previous_vertices[current_vertex] is not None:
            path.insert(0, current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.insert(0, current_vertex)
        return tuple(path)

    def floydWarshall(self):
        # Gives all the minimum cost to travel between all the vertex
        matrix = self.adjacencyMatrix()
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i != j and matrix[i][j] == 0:
                    matrix[i][j] = float('inf')
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != float('inf') and matrix[k][j] != float('inf'):
                        if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                            matrix[i][j] = matrix[i][k] + matrix[k][j]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = '∞'
        return matrix

    def Kruskal(self) -> object:
        # Returns the spanning tree of the graph
        spanning_tree = Graph()
        current_tree_edges = self.__edges.copy()
        while spanning_tree.vertex != self.__vertex:
            if current_tree_edges:
                smallest_edge = current_tree_edges[0]
                for edge in current_tree_edges:
                    if edge.value <= smallest_edge.value:
                        smallest_edge = edge
                vertexA = smallest_edge.A
                vertexB = smallest_edge.B
                if vertexA not in spanning_tree.vertex and vertexB not in spanning_tree.vertex:
                    spanning_tree.addVertex(vertexA.name)
                    spanning_tree.addVertex(vertexB.name)
                    spanning_tree.addEdge(vertexA.name, vertexB.name, smallest_edge.value)
                elif vertexA in spanning_tree.vertex and vertexB not in spanning_tree.vertex:
                    spanning_tree.addVertex(vertexB.name)
                    spanning_tree.addEdge(vertexA.name, vertexB.name, smallest_edge.value)
                elif vertexA not in spanning_tree.vertex and vertexB in spanning_tree.vertex:
                    spanning_tree.addVertex(vertexA.name)
                    spanning_tree.addEdge(vertexA.name, vertexB.name, smallest_edge.value)
                current_tree_edges.remove(smallest_edge)
            else:
                return spanning_tree
        return spanning_tree

    @property
    def vertex(self):
        return self.__vertex

    @property
    def edges(self):
        return self.__edges
