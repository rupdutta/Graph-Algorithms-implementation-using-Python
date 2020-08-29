import dijkstra_array
#import dijkstra_heap
import array_methods
import networkx as nx
import matplotlib.pyplot as plt
import dijkstras_heap_updated



def starting_function():
    
    input("Welcome to the shortest path problem solver application. To proceed please press enter")
    print("If the user would like to change the input of the graph they must do so by editing the adjacency matrix file \n\nFile format:\n- Please ensure the first line has the letter 'A' for arc matrix.\n- The second line contains the order of the graph.\n- Please also ensure that the graph is in the same folder as this exectable file\n")
    
    file_name = input("""Please enter the filename (for example - test_matrix.txt)""")
    return file_name


#reading file data from input arc-weight matrix     
def read_file_matrix(filename):  
    
    file = open(filename, 'r')    
    file_lines = file.readlines()
    
    matrix = []
    for x in range(len(file_lines)):
        curr = file_lines[x].strip()

        if x == 0:
            tag = curr
        if x == 1:
            order = curr

        if len(curr) > 1:
            curr = curr.split()
            for x in range(len(curr)):
                curr[x] = float(curr[x])

            matrix.append(curr)
                        
    return matrix


def convert_to_dictionary(array):    
    new_dict = {}    
    for x in array:        
        key = x[0]        
        value = x[1]
                
        new_dict[key] = value        
        
    return new_dict


def convert_matrix_to_dict(matrix):    
    graph_dict = {}
    
    
    for x in range(len(matrix)):
        row = matrix[x]
        row_dict = {}
        
        for y in range(len(row)):            
            
            if row[y] != matrix[x]:
                
                key_num = x + 1
                val_num = y + 1
                val_distance = row[y]
                
                
                if str(key_num) != str(val_num) and val_distance > 0:
                    
                    row_dict[str(val_num)] = int(val_distance) 
                    graph_dict[str(key_num)] = row_dict                    
    
    return graph_dict


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
    return 0


def print_paths(shortest_distances, parent_array, start_node):    
    for x in shortest_distances:        
        vertex = x[0]        
        if vertex != start_node:            
            path = return_path(parent_array, start_node, vertex)
            print(path)
	


def show_graph(graph):    
    G = nx.Graph(graph)    
    nx.draw(G, with_labels=True,font_size = 10, node_size=700)   
    plt.show()
    
    
def run_questions(graph, num_edges, num_vertices):    
    shortest_distances_set = None    
    start_node = input("Which node would you like to use as a starting point? Please enter only one node and ensure it is a number!")
        
    if num_edges < num_vertices:        
        print("Based on your graph, the recommended version of the algorithm you should use is the array(Dijkstra's) implementation")        
    else:
        print("Based on your graph, the recommended version of the algorithm you should use is the heap(Tarjan's) implementation")
        
    method = input("Press 1: Dijkstra's version or  Press 2: Tarjan's version")
    
    if method == '1':
      
        shortest_distances, parent_array = dijkstra_array.dijkstra_array(graph, str(start_node))
        print("Solution set in format (a, b) where a is the vertex and b is the distance")
        print(shortest_distances)
        print("")
        print("Parent array, first one is child and second is parent")
        print(parent_array)
        print("")
        shortest_distances_set  = shortest_distances
        
        print_paths(shortest_distances, parent_array, str(start_node))
                                      
    if method == '2':
        
        
        shortest_distances, parent_node = dijkstras_heap_updated.di_heap(graph, start_node)
        print("Solution set in format (a, b) where a is the vertex and b is the distance")
        print(shortest_distances)
        print("")
        print("Parent array, first one is child and second is parent")
        print(parent_node)
        print("")
        shortest_distances_set  = shortest_distances
    
        #print_paths(shortest_distances, parent_node, str(start_node))
        

	
filename = starting_function()

matrix = read_file_matrix(filename)
graph = convert_matrix_to_dict(matrix)

G = nx.Graph(graph)
num_edges = G.number_of_edges()
num_vertices = G.number_of_nodes()

run_questions(graph, num_edges, num_vertices)
show_graph(graph)
