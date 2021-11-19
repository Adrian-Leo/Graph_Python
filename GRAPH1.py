class Graph:
    def __init__(self,gdict=None):
        if gdict is None :
            gdict=[]
        self.gdict=gdict

    #get vertex
    def getVertex(self):
        return list(self.gdict.keys())

    #get edge
    def getEdge(self):
        edges = []
        for v in self.gdict:
            for e in self.gdict[v]:
                # if {v,e} not in edges :
                    edges.append({e,v})
        return edges

    #add vertex
    def addVertex(self,v):
        if v not in self.gdict:
            self.gdict[v]=[]

    #add edges

    def addEdge(self,e):
        (v1,v2)=e
        if v1 in self.gdict:
            self.gdict[v1].append(v2)
        else:
            self.gdict[v1]=[v2]

        if v2 in self.gdict:
            self.gdict[v2].append(v1)
        else:
            self.gdict[v2]=[v1]

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex
            in graph """
        if path == None:
            path = []
        graph = self.gdict
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
        graph = self.gdict
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





# input element graph berdasarkan adjacent
# a -> b dan c
# b -> a dan c
#dst
graphElement = {"a":["c"],"b":["a"],"c":["b","d","e"],"d":[],"e":["a"]}

#object
g=Graph(graphElement)

print("vertex : ")
print(g.getVertex())
print("=" * 40)
print("edges : ")
print(g.getEdge())
print("=" * 40)
print("after add vertex : ")
# g.addVertex("e")
# g.addVertex("c") # -> test
# print(g.getVertex())
print("=" * 40)
print("after add edges : ")
# g.addEdge({"e","d"})
# g.addEdge({"f","d"})
# print(g.getEdge())