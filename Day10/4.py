#Graph

# graph consists of a finite set of vertices(or nodes) and a set of edges which connects a pair of nodes


# if  a graph is complete or almost complete we should use Adjency Matrix
# if the NUmber of edges are few then we should use Adjacency List


#    A  B  C  D  E
# A  0  1  1  1  0                               
# B  1  0  0  0  1
# C  1  0  0  1  0
# D  1  0  1  0  1
# E  0  1  0  1  0


class  Graph:
    def __init__(self):
        self.adjecency_list={}

    def add_vertex(self,vertex):
        if vertex not in self.adjecency_list.keys():
            self.adjecency_list[vertex]=[]
            return True
        return False
    
    def add_edge(self,vertex1,vertex2):
        if vertex1  in self.adjecency_list.keys() and vertex2 in self.adjecency_list:
            self.adjecency_list[vertex1].append(vertex2)
            # self.adjecency_list[vertex2].append(vertex1)
            return True
        return False

    def print_graph(self):
        for vertex  in self.adjecency_list.keys():
            print(vertex,":",self.adjecency_list[vertex])
    

my_graph=Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("A","D")
my_graph.add_edge("B","A")
my_graph.add_edge("B","E")
my_graph.add_edge("C","A")
my_graph.add_edge("C","D")
my_graph.add_edge("D","A")
my_graph.add_edge("D","C")
my_graph.add_edge("D","E")
my_graph.add_edge("E","B")
my_graph.add_edge("E","D")

my_graph.print_graph()





