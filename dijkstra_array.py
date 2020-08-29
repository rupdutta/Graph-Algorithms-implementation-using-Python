import array_methods


# file that contains the original array version of dijkstra's algorithm

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
                
                
        print(shortest_distances)      
                
    
    return shortest_distances, parent_array


example_graph = {
    '1': {'2': 3, '3': 6, '4': 1},
    '2': {'1': 3, '4': 3, '3': 4},
    '3': {'2': 4, '1': 6, '4': 2, '5': 1, '6': 4},
    '4': {'1': 1, '2': 3, '3': 2, '5': 1},
    '5': {'4': 1, '3': 2, '6': 2},
    '6': {'3': 4, '5': 2},
}

# can be ran in this file
# res_distances, parent_array = dijkstra_array(example_graph, '3')