class Graph:

    def __init__(self, graph_dict=None):

        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict


    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


    def jBerangkat(graph, src, dest, visited=[], distances={}, predecessors={}):
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
            print("path: " + readable)
            print("cost perjalanan: " + str(distances[dest]))

            # mencari cost singgah
            cost_singgah = 0
            for i in path:
                new_cost_singgah = vertex[i]
                cost_singgah += new_cost_singgah

            # mencari cost jalan
            cost_jalan = distances[dest]

            # mencari cost akhir
            cost_akhir = cost_singgah + cost_jalan
            print("cost singgah : ",cost_singgah)
            print("Total cost= " + str(cost_akhir))

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
            Graph.jBerangkat(graph, x, dest, visited, distances, predecessors)

    def jKembali(graph_baru, src, dest, visited=[], distances={}, predecessors={}):
        # cek keadaan
        if src not in graph_baru:
            raise TypeError('The root of the shortest path tree cannot be found')
        if dest not in graph_baru:
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

            for index in range(1, len(path)):
                readable = path[index] + '--->' + readable
            print('shortest path - array: ' + str(path))
            print("path: " + readable)
            print("cost perjalanan: " + str(distances[dest]))

            # mencari cost singgah
            cost_singgah = 0
            for i in path:
                new_cost_singgah = vertex[i]
                cost_singgah += new_cost_singgah

            # mencari cost jalan
            cost_jalan = distances[dest]

            # mencari cost akhir
            cost_akhir = cost_singgah + cost_jalan
            print("cost singgah : ", cost_singgah)
            print("Total cost= " + str(cost_akhir))

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
            Graph.jKembali(graph_baru, x, dest, visited, distances, predecessors)

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


#EDGE WEIGHT
graph = {'a': {'b': 7, 'c': 7, 'h':6},
         'b': {'a': 7, 'c': 3, 'd':4,'g':1,'f':5},
         'c': {'a':7,'b':3,'h':9,'i':10},
         'd': {'b':4,'e':3,'f':7,'g':11,},
         'e': {'d':3,'f':3,'g':6,'k':8,'l':7,'i':8,'j':4},
         'f': {'b':5,'d':7,'e':3,'k':9},
         'g': {'b':1,'d':11,'e':6,'i':5},
         'h': {'a':5,'c':9,'i':8},
         'i': {'h':8,'c':10,'g':5,'e':8,'j':11,'n':2},
         'j': {'n':4,'i':11,'e':4,'l':5,'m':1},
         'k': {'f':9,'e':8,'l':3,'o':2},
         'l': {'m':2,'o':5,'k':3,'e':7,'j':5},
         'm': {'n':8,'j':1,'l':2,'o':3},
         'n': {'i':2,'j':4,'m':8},
         'o': {'k':2,'l':5,'m':3}
         }

#VERTEX WEIGHT
vertex = {'a':5,'b':7,'c':4,'d': 8,'e':5,'f':4,'g':4,
          'h':3,'i':6,'j': 7,'k':6,'l':9,'m' :5, 'n': 7,'o':6}

#PATH


print("="*50)
print("vertex weight")
print(vertex)
print("="*50)
print("edge weight")
print(graph)
print("="*50)
#FIND SHORTEST PATH
print("shortest path from i to j ")
print("="*50)
Graph.jBerangkat(graph,'a','j')
#OBJECT
print("="*50)
graph1 = Graph(graph)
print("all the path from i to j")
print("="*50)
#FIND ALL PATH
path = graph1.find_all_paths("i","j")
print(path)
#way back path
print("="*50)
print("way back path ")

print("="*50)

path = ['j','n','i']

for i in path:
    if i not in path[::len(path)-2]:
        del graph[i]

print(graph)
graph_pulang=graph
Graph.jKembali(graph_pulang,"j","a")



