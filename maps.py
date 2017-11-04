import networkx as nx
import json

G = nx.MultiDiGraph()

G.add_nodes_from(range(1,77))
G.add_nodes_from([101,102,104,105,107,108,109])
G.add_nodes_from([201,202,203,204,206,207,208,209,210,211,212])
G.add_nodes_from([301,304,305,306])
G.add_nodes_from([401,402,403,405,406,407,408,409,4101,4102])
G.add_nodes_from([501,504,505,506,507,508])
G.add_nodes_from([604,605,606,618])
G.add_nodes_from([701,703,705,706,707])
G.add_nodes_from([801,803])

with open('.\\data\\edge_weights.json', 'r') as f:
    edges = json.load(f)

G.add_weighted_edges_from([tuple(elem) for elem in edges])

def path_search(source, target, stopover=None):
    if stopover == None: stopover = []
    path = []

    if stopover != [] :
        for i in range(len(stopover)):
            if i == 0: 
                path += nx.dijkstra_path(G, source, stopover[i])
            else: 
                path += nx.dijkstra_path(G, stopover[i-1], stopover[i])
        path += nx.dijkstra_path(G, stopover[len(stopover)-1], target) 
    else: 
        path = nx.dijkstra_path(G, source, target)

    tips = set()
    for id in path:
        if id in {12, 21, 105}:
            tips.add(1)
        elif id in {12, 19, 20, 107}:
            tips.add(2)
        elif id in {60, 61, 62, 706, 707}:
            tips.add(3)
        elif id in {29, 32, 204}:
            tips.add(4)
            tips.add(6)
            tips.add(10)
        elif id in {48, 56, 401}:
            tips.add(5)
        elif id in {23, 24, 31, 33, 37, 38, 209}:
            tips.add(7)
        elif id in {15, 16, 17, 18, 508}:
            tips.add(8)
        elif id in {42, 56, 212}:
            tips.add(9)

    ret = {
        "path": path,
        "tips": list(tips)
    }

    return ret;


if __name__ == '__main__':
    print(path_search(305, 507, [104, 604]))