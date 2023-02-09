#each of the 13 sampling motif counting functions are stored here

import itertools
import numpy as np
from tqdm import tqdm

def sampling_count_M1(all_nodes, adj_list_away, adj_list_toward, sample_percent):

    vertices = [] #store vertices
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in sampled_nodes:
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 not in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])
                    & (vertex3 in adj_list_away[vertex2])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    #return triangles
    
    edge_dict = {}
    for tri in triangles:
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict


def sampling_count_M2(all_nodes, adj_list_away, adj_list_toward, sample_percent):

    vertices = [] #store vertices
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes:
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 not in adj_list_toward[vertex2]) & (vertex2 in adj_list_toward[vertex1])
                    & (vertex3 in adj_list_away[vertex2])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    for tri in triangles:
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict


def sampling_count_M3(all_nodes, adj_list_away, adj_list_toward, sample_percent):

    vertices = [] #store vertices
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes:
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 in adj_list_toward[vertex2]) & (vertex2 in adj_list_toward[vertex1])
                    & (vertex3 in adj_list_away[vertex2])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    for tri in triangles:
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict


def sampling_count_M4(all_nodes, adj_list_away, adj_list_toward, sample_percent):

    vertices = []

    num_sample = int(all_nodes.shape[0]*sample_percent)
    
    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes:
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 in adj_list_toward[vertex3])
                    & (vertex3 in adj_list_toward[vertex2]) & (vertex2 in adj_list_toward[vertex1])
                    & (vertex1 != vertex2) & (vertex1 != vertex3) & (vertex2 != vertex3)
                    & (vertex3 in adj_list_away[vertex2])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    for tri in triangles:
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict


def sampling_count_M5(all_nodes, adj_list_away, adj_list_toward, sample_percent):
    
    vertices = []
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each parent node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes:
                
                if ((vertex3 in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                    & (vertex2 not in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])
                    & (vertex3 in adj_list_away[vertex1])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    for tri in triangles:
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict


def sampling_count_M6(all_nodes, adj_list_away, adj_list_toward, sample_percent):
    
    vertices = []
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each parent node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes:
                
                if ((vertex3 in adj_list_away[vertex2]) & (vertex3 in adj_list_toward[vertex2])
                    & (vertex2 not in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])
                    & (vertex3 in adj_list_away[vertex1])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    for tri in triangles:
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict


def sampling_count_M7(all_nodes, adj_list_away, adj_list_toward, sample_percent):
    
    vertices = []
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each parent node
        for vertex2 in adj_list_toward[vertex1]: #checks first child node
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes:  
                
                if ((vertex2 not in adj_list_away[vertex1]) & (vertex3 not in adj_list_away[vertex1])
                   & (vertex2 in adj_list_away[vertex3]) & (vertex3 in adj_list_away[vertex2])
                   & (vertex3 in adj_list_toward[vertex1])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    for tri in triangles:
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict


def sampling_count_M8(all_nodes, adj_list_away, adj_list_toward, sample_percent):

    vertices = []
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each vertex1 node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes: 

                if ((vertex3 not in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                    & (vertex2 not in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])
                    & (vertex2 != vertex3) & (vertex3 in adj_list_away[vertex1])):

                    vertices.append([vertex1, vertex2, vertex3])

    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle

    edge_dict = {}
    for tri in triangles:

        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else: #if edge does exist
                edge_dict[edge] += 1 #add to edge count

    return len(triangles), edge_dict


def sampling_count_M9(all_nodes, adj_list_away, adj_list_toward, sample_percent):
    
    vertices = []
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes: 
                
                if ((vertex1 not in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 not in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])
                    & (vertex1 != vertex3) & (vertex3 in adj_list_away[vertex2])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    for tri in triangles:
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict


def sampling_count_M10(all_nodes, adj_list_away, adj_list_toward, sample_percent):
    
    vertices = []
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks first vertex
        for vertex2 in adj_list_toward[vertex1]: #checks second vertex
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes:
                
                if ((vertex2 not in adj_list_away[vertex1]) & (vertex3 not in adj_list_away[vertex1])
                    & (vertex2 not in adj_list_away[vertex3]) & (vertex3 not in adj_list_away[vertex2])
                    & (vertex2 != vertex3) & (vertex3 in adj_list_toward[vertex1])):

                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    for tri in triangles:
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict


def sampling_count_M11(all_nodes, adj_list_away, adj_list_toward, sample_percent):

    vertices = []
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each vertex1 node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes:

                if ((vertex3 not in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                    & (vertex2 in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])
                    & (vertex2 != vertex3) & (vertex3 in adj_list_away[vertex1])):

                    vertices.append([vertex1, vertex2, vertex3])

    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle

    edge_dict = {}
    for tri in triangles:

        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else: #if edge does exist
                edge_dict[edge] += 1 #add to edge count

    return len(triangles), edge_dict


def sampling_count_M12(all_nodes, adj_list_away, adj_list_toward, sample_percent):
    
    vertices = []
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes:
                
                if ((vertex1 not in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])
                    & (vertex1 != vertex3) & (vertex3 in adj_list_away[vertex2])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    for tri in triangles:
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict


def sampling_count_M13(all_nodes, adj_list_away, adj_list_toward, sample_percent):

    vertices = []
    
    num_sample = int(all_nodes.shape[0]*sample_percent)

    #randomly sample third vertices at uniform from all possible nodes
    sampled_nodes = np.random.choice(all_nodes, num_sample)
    
    for vertex1 in tqdm(adj_list_away): #checks each vertex1 node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            
            #randomly sample a third vertex at uniform from all possible nodes
            for vertex3 in sampled_nodes:

                if ((vertex3 not in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                    & (vertex2 in adj_list_toward[vertex1]) & (vertex3 in adj_list_toward[vertex1])
                    & (vertex2 != vertex3) & (vertex3 in adj_list_away[vertex1])):

                    vertices.append([vertex1, vertex2, vertex3])

    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle

    edge_dict = {}
    for tri in triangles:

        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else: #if edge does exist
                edge_dict[edge] += 1 #add to edge count

    return len(triangles), edge_dict