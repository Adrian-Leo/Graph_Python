
class Graph(object):

    def __init__(self, graph_dict=None):

        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    #GET VERTICE
    def getVertice(self):

        return list(self.__graph_dict.keys())
    #GET EDGE
    def getEdges(self):

        return self.__generate_edges()

    #ADD VERTEX
    def add_vertex(self, inputVertex):
        if inputVertex not in self.__graph_dict:
            self.__graph_dict[inputVertex] = []

    #ADD EDGE
    def add_edge(self, inputEdge):
        edge = set(inputEdge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):

        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex
            in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

    #SHORTEST PATH
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def jPenerbangan(graph, src, dest, visited=[], distances={}, predecessors={}):
        # cek keadaan
        if src not in graph:
            raise TypeError('The root of the shortest path tree cannot be found')
        if dest not in graph:
            raise TypeError('The target of the shortest path cannot be found')

        # Kondisi memadai
        if src == dest:
            # Jalur terpendek yang di tempuh
            path = []
            pred = dest
            while pred != None:
                path.append(pred)
                pred = predecessors.get(pred, None)
            # reverses the array, to display the path nicely
            readable = path[0]
            for index in range(1,len(path)):
                readable = path[index] + '--->' + readable
            print('shortest path - array: ' + str(path))
            print("path: " + readable + ",   cost=" + str(distances[dest]))
        else:
            # if it is the initial  run, initializes the cost=
            if not visited:
                distances[src] = 0

            for neighbor in graph[src]:

                if neighbor not in visited:
                    new_distance = distances[src] + graph[src][neighbor]
                    if new_distance < distances.get(neighbor, float('inf')):
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = src

            visited.append(src)

            unvisited = {}
            for k in graph:
                if k not in visited:
                    unvisited[k] = distances.get(k, float('inf'))
            x = min(unvisited, key=unvisited.get)
            Graph.jPenerbangan(graph, x, dest, visited, distances, predecessors)

#INPUT ELEMENT GRAPH
if __name__ == "__main__":
    g = {"a": ["b","c"],
         "b": ["a","d"],
         "c":["a","d"],
         "d":["c","b","e"]

         }
    #OBJECT
    graph = Graph(g)

    #OUTPUT GRAPH


    print("Vertices of graph:")
    print(graph.getVertice())

    print("Edges of graph:")
    print(graph.getEdges())

    # print("Add vertex:")
    # graph.add_vertex("z")
    #
    # print("Vertices of graph:")
    # print(graph.getVertice())
    #
    # print("Add an edge:")
    # graph.add_edge({"a", "z"})
    #
    # print("Vertices of graph:")
    # print(graph.getVertice())
    #
    # print("Edges of graph:")
    # print(graph.getVertice())

    # print('Adding an edge {"x","y"} with new vertices:')
    # graph.add_edge({"x", "y"})
    # print("Vertices of graph:")
    # print(graph.getVertice())
    # print("Edges of graph:")
    # print(graph.getEdges())

    #INPUT FIND PATH
    print("="*20,"FIND PATH","="*20)
    print("the path from a to e ")
    path = graph.find_path("a", "e")
    print(path)

    print("find all path from a to e ")
    path = graph.find_all_paths("a", "e")
    print(path)