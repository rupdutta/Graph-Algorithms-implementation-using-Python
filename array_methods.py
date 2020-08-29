# Module used to store methods for array handling

def delete_element(array, target_vertex):
    
    for x in range(len(array)):
        
        curr_pair = array[x]
        curr_vertex = curr_pair[0]
        
        if curr_vertex == target_vertex:
            
            del array[x]
            
            return array



def get_element_distance(array, target_vertex):
    
    
    for x in array:
        
        if x[0] == target_vertex:
            
            return x[1]



def get_min_value_node(array):
    
    
    min_value = float('inf')
    min_value_vertex = None
    
    counter = 0
    
    for x in array:
        
        vertex = x[0]
        distance = x[1]
        
        if distance < min_value:
            min_value = distance
            min_value_vertex = vertex
            min_value_counter = counter 
        counter += 1   
        
        
        
    result = min_value_vertex
    
    if distance == float('inf'):
        min_value = distance
        min_value_vertex = vertex
        min_value_counter = counter 
        result = min_value_vertex
    
    return result
	

def initialise_array(graph):
    
    array = []
    
    for node in graph:
        array.append((node, float('inf')))
        
        
    return array
    
	
def insert_value(array, pair):
    
    vertex = pair[0]
    distance = pair[1]
    
    for x in range(len(array)):
        
        curr_vertex = array[x][0]
        curr_distance  = array[x][1]
        
        if curr_vertex == vertex:
            
            del array[x]
            
            array.append((vertex, distance))
            
            return array
    
    array.append((vertex, distance))
            
    return array
    
    
    
def return_path(parents_array, start, end):
    

    parents_dict = convert_to_dictionary(parents_array)    
    next_val = 0
    curr = end    
    path_string = end + " -> "
    start_and_end = 'Shortest path from ' + start + ' to ' + end 
    
    
    while curr != start:
              
        next_val = parents_dict[curr]
        
        path_string += next_val         
        
        if next_val == start:
                 
            return start_and_end, path_string
    
        curr = parents_dict[next_val]
        
        path_string += ' -> '
        
       
        if curr == start:
                
            path_string += curr
            
            return start_and_end, path_string
        
        
        
        path_string += curr  + ' -> ' 
    
    
def convert_to_dictionary(array):
    
    new_dict = {}
    
    for x in array:
        
        key = x[0]
        
        value = x[1]
        
        
        new_dict[key] = value
        
        
    return new_dict