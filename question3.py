import array_methods
import networkx as nx
import matplotlib.pyplot as plt



#Shortest path program developed in q1 used to solve this problem
def dijkstra_array(graph, start_node):
    
    # initialise arrays 
    shortest_distances = array_methods.initialise_array(graph)
    unvisited_nodes = array_methods.initialise_array(graph)
    
    parent_array = []
    
    
    # adjust value of starting vertex
    shortest_distances = array_methods.insert_value(shortest_distances, (start_node, 0))
    unvisited_nodes = array_methods.insert_value(unvisited_nodes, (start_node, 0))
    
    
    while len(unvisited_nodes) > 0:
        
        # obtain vertex with lowest distance value
        curr_node = array_methods.get_min_value_node(unvisited_nodes)
        curr_dist = array_methods.get_element_distance(shortest_distances, curr_node)
        
        unvisited_nodes = array_methods.delete_element(unvisited_nodes, curr_node)
        
        # for every neighbour of the current vertex
        for neighbour, neighbour_dist in graph[curr_node].items():
            
            distance = curr_dist + neighbour_dist
            shortest_distance_neighbour = array_methods.get_element_distance(shortest_distances, neighbour)
            
            # if the distance is shorter than that already recorded
            if distance < shortest_distance_neighbour:
                array_methods.insert_value(shortest_distances, (neighbour, distance))
                array_methods.insert_value(unvisited_nodes, (neighbour, distance))
                array_methods.insert_value(parent_array, (neighbour, curr_node))
                
                
    
                
    
    return shortest_distances, parent_array


question_three_graph = {
    '1': {'3': 10, '4': 11, '2': 6},
    '2': {'1': 6, '7': 12, '4': 3, '6': 6},
    '3': {'1': 10, '4': 5, '5': 8, '9': 9},
    '4': {'1': 11, '3': 5, '6': 2, '9': 12, '5': 7},
    '5': {'9': 3, '8': 2, '6': 4, '4': 7, '3': 8},
    '6': {'4': 2, '2': 6, '7': 7, '8': 9, '5': 4},
    '7': {'p': 11, '8': 4, '6': 7, '2': 12},
    '8': {'p': 7, '5': 2, '7': 4, '6': 9},
    '9': {'p': 10, '5': 3, '3': 9, '4': 12},
    'p': {'p': 10, '8': 7, '7': 11}
    
}


#plotting the graph
G = nx.Graph(question_three_graph)
nx.draw(G,with_labels=True, font_size=10, node_size =700)
plt.show()

start = input('Please enter the start vertex: 1,2,3,4,5,6,7,8,9,p\n')
end = input('Please enter the end vertex: 1,2,3,4,5,6,7,8,9,p\n')




distances, parent_dict = dijkstra_array(question_three_graph, start)

print("\nThe shortest distances from the start vertex to the each vertex of the graph ('vertex', shortest distance value):\n", distances)
print("\nParent array ('vertex', 'parent vertex'):\n",parent_dict)

short_dist = array_methods.return_path(parent_dict, start, end)
print("\n", short_dist)
