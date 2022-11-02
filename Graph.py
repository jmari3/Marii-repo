lass Graph:
    def __init__(self, g_dict=None):
        if g_dict is None:
            g_dict = {}
        self.g_dict = g_dict

    def get_vertex(self):
        return list(self.g_dict.keys())


    def get_edges(self):
        a = []
        for i in list(self.g_dict.items()):
            for j in i[1]:
                if tuple(reversed((i[0],j))) not in a:
                    a.append((i[0],j))
        
        # a = [(i,j) for i in self.g_dict.items() for j in self.g_dict.values()]
        return a 
    
    
    def add_vertex(self,vertex):
        self.g_dict[vertex] = []
        
    def add_edge(self, new_edge):
        if new_edge[0] in self.g_dict:
            if new_edge[1] not in self.g_dict[new_edge[0]]:
                self.g_dict[new_edge[0]].extend(new_edge[1])
            else:
                self.g_dict[new_edge[0]] = new_edge[1]
                
g1 = Graph({
    "a": ["b", "c", "f"],
    "b": ["a", "c"],
    "c": ["b", "d"],
    "d": ["c","e"],
    "e": ["d"],
    "f": ["a"]
})