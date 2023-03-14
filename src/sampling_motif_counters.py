#each of the 13 sampling motif counting functions are stored here

import itertools
import numpy as np
from tqdm import tqdm

def sampling_count_M1(adj_list_away, adj_list_toward, threshold):

    vertices = [] #store vertices
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            
            if len(adj_list_away[vertex2]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex2], threshold)
            
                for vertex3 in sampled_nodes:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 in adj_list_away[vertex3])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex2])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                        
            else: #if the degree is lower than the threshold, sample like normal
                
                for vertex3 in adj_list_away[vertex2]: #checks third vertex
                
                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 in adj_list_away[vertex3])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count += 1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count
    
    final_count = (sample_count+normal_count)/3
    
    return final_count, edge_dict


def sampling_count_M2(adj_list_away, adj_list_toward, threshold):

    vertices = [] #store vertices
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            
            if len(adj_list_away[vertex2]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex2], threshold)
            
                for vertex3 in sampled_nodes:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 in adj_list_away[vertex3]) & (vertex2 in adj_list_toward[vertex1])
                        & (vertex3 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex2])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                        
            else: #if the degree is lower than the threshold, sample like normal
                
                for vertex3 in adj_list_away[vertex2]: #checks third vertex
                
                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 in adj_list_away[vertex3]) & (vertex2 in adj_list_toward[vertex1])
                        & (vertex3 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count += 1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count
     
    final_count = sample_count+normal_count
    
    return final_count, edge_dict


def sampling_count_M3(adj_list_away, adj_list_toward, threshold):

    vertices = [] #store vertices
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            
            if len(adj_list_away[vertex2]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex2], threshold)
            
                for vertex3 in sampled_nodes:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 in adj_list_away[vertex3]) & (vertex3 in adj_list_toward[vertex2]) 
                        & (vertex2 in adj_list_toward[vertex1]) & (vertex3 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex2])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                        
            else: #if the degree is lower than the threshold, sample like normal
                
                for vertex3 in adj_list_away[vertex2]: #checks third vertex
                
                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 in adj_list_away[vertex3]) & (vertex3 in adj_list_toward[vertex2]) 
                        & (vertex2 in adj_list_toward[vertex1]) & (vertex3 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count += 1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count
    
    final_count = sample_count+normal_count
    
    return final_count, edge_dict


def sampling_count_M4(adj_list_away, adj_list_toward, threshold):

    vertices = []
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            
            if len(adj_list_away[vertex2]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex2], threshold)
            
                #randomly sample a third vertex at uniform from all possible nodes
                for vertex3 in sampled_nodes:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 in adj_list_away[vertex3]) & (vertex1 in adj_list_toward[vertex3])
                        & (vertex3 in adj_list_toward[vertex2]) & (vertex2 in adj_list_toward[vertex1])
                        & (vertex1 != vertex2) & (vertex1 != vertex3) & (vertex2 != vertex3)
                        & (vertex3 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex2])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                
                        
            else: #if the degree is lower than the threshold, sample like normal
                
                for vertex3 in adj_list_away[vertex2]: #checks third vertex
                
                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 in adj_list_away[vertex3]) & (vertex1 in adj_list_toward[vertex3])
                        & (vertex3 in adj_list_toward[vertex2]) & (vertex2 in adj_list_toward[vertex1])
                        & (vertex1 != vertex2) & (vertex1 != vertex3) & (vertex2 != vertex3)
                        & (vertex3 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count += 1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count
    
    final_count = (sample_count+normal_count)/6
    
    return final_count, edge_dict



def sampling_count_M5(adj_list_away, adj_list_toward, threshold):
    
    vertices = []
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks each parent node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            
            if len(adj_list_away[vertex2]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex2], threshold)
            
                #randomly sample a third vertex at uniform from all possible nodes
                for vertex3 in sampled_nodes:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 in adj_list_away[vertex1])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex2])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                        
            else: #if the degree is lower than the threshold, sample like normal
                
                for vertex3 in adj_list_away[vertex2]:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 in adj_list_away[vertex1])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count += 1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count
    
    final_count = sample_count+normal_count
    
    return final_count, edge_dict



def sampling_count_M6(adj_list_away, adj_list_toward, threshold):
    
    vertices = []
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks each parent node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            
            if len(adj_list_away[vertex2]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex2], threshold)
            
                #randomly sample a third vertex at uniform from all possible nodes
                for vertex3 in sampled_nodes:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 in adj_list_away[vertex1]) & (vertex3 in adj_list_toward[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex2])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                        
            else: #if the degree is lower than the threshold, sample like normal
                
                for vertex3 in adj_list_away[vertex2]:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 in adj_list_away[vertex1]) & (vertex3 in adj_list_toward[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count += 1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count
                                
    final_count = (sample_count+normal_count)/2
    
    return final_count, edge_dict



def sampling_count_M7(adj_list_away, adj_list_toward, threshold):
    
    vertices = []
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks each parent node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            
            if len(adj_list_away[vertex2]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex2], threshold)
            
                #randomly sample a third vertex at uniform from all possible nodes
                for vertex3 in sampled_nodes:  

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 in adj_list_away[vertex1]) & (vertex1 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex2])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                        
            else:
                
                for vertex3 in adj_list_away[vertex2]: #checks third vertex
                    
                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 in adj_list_away[vertex1]) & (vertex1 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count += 1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count
      
    final_count = (sample_count+normal_count)/2
    
    return final_count, edge_dict



def sampling_count_M8(adj_list_away, adj_list_toward, threshold):

    vertices = []
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in adj_list_away: #checks each vertex1 node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            
            if len(adj_list_away[vertex1]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex1], threshold)
            
                #randomly sample a third vertex at uniform from all possible nodes
                for vertex3 in sampled_nodes: 

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 not in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                        & (vertex2 not in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])
                        & (vertex2 != vertex3) & (vertex3 in adj_list_away[vertex1])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex1])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                        
            else:
                
                for vertex3 in adj_list_away[vertex1]:
                    
                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 not in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                        & (vertex2 not in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])
                        & (vertex2 != vertex3) & (vertex3 in adj_list_away[vertex1])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count += 1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count
    
    final_count = (sample_count+normal_count)/2
    
    return final_count, edge_dict



def sampling_count_M9(adj_list_away, adj_list_toward, threshold):
    
    vertices = []
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            
            if len(adj_list_away[vertex2]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex2], threshold)
            
                #randomly sample a third vertex at uniform from all possible nodes
                for vertex3 in sampled_nodes: 

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 not in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                        & (vertex3 not in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])
                        & (vertex1 != vertex3) & (vertex3 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex2])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                        
            else:
                
                for vertex3 in adj_list_away[vertex2]:
                    
                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 not in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                        & (vertex3 not in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])
                        & (vertex1 != vertex3) & (vertex3 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count += 1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count
                    
    final_count = (sample_count+normal_count)
    
    return final_count, edge_dict


def sampling_count_M10(adj_list_away, adj_list_toward, threshold):
    
    vertices = []
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks first vertex
        for vertex2 in adj_list_toward[vertex1]: #checks second vertex
            
            if len(adj_list_toward[vertex1]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_toward[vertex1], threshold)
                
                #randomly sample a third vertex at uniform from all possible nodes
                for vertex3 in sampled_nodes:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex2 not in adj_list_away[vertex1]) & (vertex3 not in adj_list_away[vertex1])
                        & (vertex2 not in adj_list_away[vertex3]) & (vertex3 not in adj_list_away[vertex2])
                        & (vertex2 != vertex3) & (vertex3 in adj_list_toward[vertex1])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_toward[vertex1])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
            
            else: #if the degree is lower than the threshold, sample like normal
                
                for vertex3 in adj_list_toward[vertex1]: #checks third vertex

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex2 not in adj_list_away[vertex1]) & (vertex3 not in adj_list_away[vertex1])
                        & (vertex2 not in adj_list_away[vertex3]) & (vertex3 not in adj_list_away[vertex2])
                        & (vertex2 != vertex3) & (vertex2 != vertex1) & (vertex1 != vertex3)):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count += 1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count  
                        
    final_count = (sample_count+normal_count)/2
    
    return final_count, edge_dict



def sampling_count_M11(adj_list_away, adj_list_toward, threshold):

    vertices = []
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks each vertex1 node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            
            if len(adj_list_away[vertex1]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex1], threshold)
            
                #randomly sample a third vertex at uniform from all possible nodes
                for vertex3 in sampled_nodes:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 not in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                        & (vertex2 in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])
                        & (vertex2 != vertex3) & (vertex3 in adj_list_away[vertex1])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex1])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                        
            else:
                
                for vertex3 in adj_list_away[vertex1]:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 not in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                        & (vertex2 in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])
                        & (vertex2 != vertex3) & (vertex3 in adj_list_away[vertex1])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count+=1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count

    final_count = (sample_count+normal_count)
    
    return final_count, edge_dict



def sampling_count_M12(adj_list_away, adj_list_toward, threshold):
    
    vertices = []
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            
            if len(adj_list_away[vertex2]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex2], threshold)
            
                #randomly sample a third vertex at uniform from all possible nodes
                for vertex3 in sampled_nodes:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 not in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                        & (vertex3 in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])
                        & (vertex1 != vertex3) & (vertex3 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex2])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                        
            else:
                
                for vertex3 in adj_list_away[vertex2]:
                    
                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex1 not in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                        & (vertex3 in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])
                        & (vertex1 != vertex3) & (vertex3 in adj_list_away[vertex2])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count+=1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count
    
    final_count = (sample_count+normal_count)
    
    return final_count, edge_dict


def sampling_count_M13(adj_list_away, adj_list_toward, threshold):

    vertices = []
    
    sample_count = 0
    normal_count = 0
    edge_dict = {}
    
    for vertex1 in tqdm(adj_list_away): #checks each vertex1 node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            
            if len(adj_list_away[vertex2]) > threshold: #if the third vertex has a high enough degree, sample
                sampled_nodes = np.random.choice(adj_list_away[vertex2], threshold)
            
                #randomly sample a third vertex at uniform from all possible nodes
                for vertex3 in sampled_nodes:

                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 not in adj_list_away[vertex1]) & (vertex3 not in adj_list_toward[vertex1])
                        & (vertex2 in adj_list_toward[vertex1]) & (vertex3 in adj_list_toward[vertex2])
                        & (vertex1 != vertex3)):

                        vertices.append([vertex1, vertex2, vertex3])
                        temp_count = (1/(threshold/len(adj_list_away[vertex1])))
                        sample_count += temp_count
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = temp_count
                            else:                            #if edge does exist
                                edge_dict[edge] += temp_count #add to edge count
                        
            else:
                
                for vertex3 in adj_list_away[vertex1]:
                    #if any of the adjacency lists are empty (nan used for placeholder) SKIP this iteration
                    if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                        break

                    if ((vertex3 not in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                        & (vertex2 in adj_list_toward[vertex1]) & (vertex3 in adj_list_toward[vertex1])
                        & (vertex2 != vertex3) & (vertex3 in adj_list_away[vertex1])):

                        vertices.append([vertex1, vertex2, vertex3])
                        normal_count+=1
                        
                        combos = list(itertools.combinations([vertex1, vertex2, vertex3], 2))

                        for edge in combos:

                            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                                edge_dict[edge] = 1
                            else:                            #if edge does exist
                                edge_dict[edge] += 1 #add to edge count
    
    final_count = (sample_count+normal_count)/2
    
    return final_count, edge_dict