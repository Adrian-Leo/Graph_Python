import collections
import heapq



# def find_path(self, start_vertex, end_vertex, path=None):
#     """ find a path from start_vertex to end_vertex
#         in graph """
#     if path == None:
#         path = []
#     graph = self.__graph_dict
#     path = path + [start_vertex]
#     if start_vertex == end_vertex:
#         return path
#     if start_vertex not in graph:
#         return None
#     for vertex in graph[start_vertex]:
#         if vertex not in path:
#             extended_path = self.find_path(vertex,
#                                            end_vertex,
#                                            path)
#             if extended_path:
#                 return extended_path
#     return None
#
# def find_all_paths(self, start_vertex, end_vertex, path=[]):
#     """ find all paths from start_vertex to
#     end_vertex in graph """
#     graph = self.__graph_dict
#     path = path + [start_vertex]
#     if start_vertex == end_vertex:
#         return [path]
#     if start_vertex not in graph:
#         return []
#     paths = []
#     for vertex in graph[start_vertex]:
#         if vertex not in path:
#             extended_paths = self.find_all_paths(vertex,end_vertex,path)
#                 for p in extended_paths:
#                     paths.append(p)
#         return paths



def shortestPath(edges, source, sink):
    # create a weighted DAG - {node:[(cost,neighbour), ...]}
    graph = collections.defaultdict(list)
    for l, r, c in edges:
        graph[l].append((c, r))
    # create a priority queue and hash set to store visited nodes
    queue, visited = [(0, source, [])], set()
    heapq.heapify(queue)
    # traverse graph with BFS
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        # visit the node if it was not visited before
        if node not in visited:
            visited.add(node)
            path = path + [node]
            # hit the sink
            if node == sink:
                return (" the cost is = ", cost ,"the path is =", path)
            # visit neighbours
            for c, neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(queue, (cost + c, neighbour, path))
    return float("inf")



if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

#OBJECT
print ("Find the shortest path  ")
print("the element of graph : ")
print (edges)
print("="*40)
print("the path from A to B")
print ("A -> B:")
print (shortestPath(edges, "A", "B"))
print("="*40)
print ("B -> F:")
print("the path from B to F")
print (shortestPath(edges, "B", "F"))