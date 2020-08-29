import array_methods
import networkx as nx
import matplotlib.pyplot as plt

marriages = {
        "PERUZZI" : {"BISCHERI":1,"STROZZI":1,"CASTELLAN":1},
        "BISCHERI" : {"PERUZZI":1,"STROZZI":1,"GUADAGNI":1,},
        "STROZZI" : {"PERUZZI":1,"BISCHERI":1,"RIDOLFI":1,"CASTELLAN":1},
        "RIDOLFI" : {"STROZZI":1,"TORNABUON":1,"MEDICI":1},
        "TORNABUON" : {"RIDOLFI":1,"GUADAGNI":1,"MEDICI":1},
        "GUADAGNI" : {"BISCHERI":1,"LAMBERTES":1,"TORNABUON":1,"ALBIZZI":1},
        "LAMBERTES" : {"GUADAGNI":1},
        "ALBIZZI" : {"GUADAGNI":1,"GINORI":1,"MEDICI":1},
        "GINORI" : {"ALBIZZI":1},
        "MEDICI" : {"RIDOLFI":1,"TORNABUON":1,"ALBIZZI":1,"ACCIAUOL":1,"BARBADORI":1,"SALVIATI":1},
        "ACCIAUOL" : {"MEDICI":1},
        "PUCCI" : {},
        "CASTELLAN" : {"PERUZZI":1,"STROZZI":1,"BARBADORI":1},
        "BARBADORI" : {"MEDICI":1,"CASTELLAN":1},
        "SALVIATI" : {"MEDICI":1,"PAZZI":1},
        "PAZZI" : {"SALVIATI":1},
}



G = nx.Graph(marriages)
nx.draw(G,with_labels=True, font_size=10, node_size =700)
plt.show()


def dijkstra_array(graph, start_node):
    
    shortest_distances = array_methods.initialise_array(graph)
    unvisited_nodes = array_methods.initialise_array(graph)
    
    parent_array = []
    
    shortest_distances = array_methods.insert_value(shortest_distances, (start_node, 0))
    unvisited_nodes = array_methods.insert_value(unvisited_nodes, (start_node, 0))
    
    while len(unvisited_nodes) > 0:
        
        curr_node = array_methods.get_min_value_node(unvisited_nodes)
        curr_dist = array_methods.get_element_distance(shortest_distances, curr_node)
        
        unvisited_nodes = array_methods.delete_element(unvisited_nodes, curr_node)
        
        
        for neighbour, neighbour_dist in graph[curr_node].items():
       
            distance = curr_dist + neighbour_dist
            shortest_distance_neighbour = array_methods.get_element_distance(shortest_distances, neighbour)
    
            if distance < shortest_distance_neighbour:
                array_methods.insert_value(shortest_distances, (neighbour, distance))
                array_methods.insert_value(unvisited_nodes, (neighbour, distance))
                array_methods.insert_value(parent_array, (neighbour, curr_node))
        
                
#        print(shortest_distances, parent_array)      
                
    
    return shortest_distances, parent_array


#NODES OF THE GRAPH
nodes = []
for node in marriages:
    nodes.append(node)
    print(node, 'is connected to ', marriages[node])
print('\nThe graph contains', len(nodes), ' nodes: ', nodes)

# DEGREE CENTRALITY
print("\nDegree centrality for vertex: ") 
for node in nodes:    
    print(node, " : ",len(marriages[node])/(len(nodes)-1))
      
# CLOSENESS CENTRALITY
print("\nCloseness centrality for vertex: ")  

for start_node in nodes:
    short_path = []   
    dict_path, dict_parent = dijkstra_array(marriages, start_node)    
    dict_path = array_methods.convert_to_dictionary(dict_path)
    for end_node in nodes:
        if dict_path[end_node] != float('inf'):                             
            short_path.append(dict_path[end_node])
    try:
        clos_centrality = ((len(short_path))-1) / sum(short_path)   
        print(start_node, " : ",clos_centrality)
    except ZeroDivisionError:
        print(start_node, " : 0.00 - node is not connected")



# BETWEENNESS CENTRALITY 
print("\nBetweenness centrality for vertex: ")
subgraph_dictionary={} #creating a new subgrath 
for key in marriages.keys():
    if marriages[key]:
        subgraph_dictionary[key]=marriages[key]
    else:
        print(key, ' : 0.0')

subgraph = nx.Graph(subgraph_dictionary)
between_centrality = nx.betweenness_centrality(subgraph)
 
for vertex in between_centrality:
    print(vertex, ' : ', between_centrality[vertex])

# EIGENVECTOR CENTRALITY 
print("\nEigenvector centrality for vertex: ")
eigenvectr_centrality = nx.eigenvector_centrality(G)
for vertex in between_centrality:
    print(vertex, ' : ', eigenvectr_centrality[vertex])