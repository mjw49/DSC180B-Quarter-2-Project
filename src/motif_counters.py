#each of the 13 naive motif counting functions are stored here

import itertools
from tqdm import tqdm
import numpy as np

def count_M1(adj_list_away, adj_list_toward):

    vertices = [] #store vertices
    
    print("count vertices")
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]:
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 not in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}

    print("count edges")
    for tri in tqdm(triangles):
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict



def count_M2(adj_list_away, adj_list_toward):

    vertices = []
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]: #access all possible nodes (vertex 3) from vertex 2
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 not in adj_list_toward[vertex2]) & (vertex2 in adj_list_toward[vertex1])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle

    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict



def count_M3(adj_list_away, adj_list_toward):

    vertices = []
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]: #access all possible nodes (vertex 3) from vertex 2
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 in adj_list_toward[vertex2]) & (vertex2 in adj_list_toward[vertex1])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict



def count_M4(adj_list_away, adj_list_toward):

    vertices = []
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]: #access all possible nodes (vertex 3) from vertex 2
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 in adj_list_toward[vertex3])
                    & (vertex3 in adj_list_toward[vertex2]) & (vertex2 in adj_list_toward[vertex1])
                    & (vertex1 != vertex2) & (vertex1 != vertex3) & (vertex2 != vertex3)):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict




def count_M5(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for vertex1 in tqdm(adj_list_away): #checks each parent node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            for vertex3 in adj_list_away[vertex1]:
                
                if ((vertex3 in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                    & (vertex2 not in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict



def count_M6(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for vertex1 in tqdm(adj_list_away): #checks each parent node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            for vertex3 in adj_list_away[vertex1]:
                
                if ((vertex3 in adj_list_away[vertex2]) & (vertex3 in adj_list_toward[vertex2])
                    & (vertex2 not in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict



def count_M7(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for vertex1 in tqdm(adj_list_away): #checks each parent node
        for vertex2 in adj_list_toward[vertex1]: #checks first child node
            for vertex3 in adj_list_toward[vertex1]: #checks second child node
                
                if ((vertex2 not in adj_list_away[vertex1]) & (vertex3 not in adj_list_away[vertex1])
                   & (vertex2 in adj_list_away[vertex3]) & (vertex3 in adj_list_away[vertex2])):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict





def count_M8(adj_list_away, adj_list_toward):

    vertices = []
    
    for vertex1 in tqdm(adj_list_away): #checks each vertex1 node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            for vertex3 in adj_list_away[vertex1]: 

                if ((vertex3 not in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                    & (vertex2 not in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])
                    & (vertex2 != vertex3)):

                    vertices.append([vertex1, vertex2, vertex3])

    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle

    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):

        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else: #if edge does exist
                edge_dict[edge] += 1 #add to edge count

    return len(triangles), edge_dict



def count_M9(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]: #access all possible nodes (vertex 3) from vertex 2
                
                if ((vertex1 not in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 not in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])
                    & (vertex1 != vertex3)):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict



def count_M10(adj_list_away, adj_list_toward):
    
    vertices = []
    print("start motif counting")
    for vertex1 in tqdm(adj_list_away): #checks first vertex
        for vertex2 in adj_list_toward[vertex1]: #checks second vertex
            for vertex3 in adj_list_toward[vertex1]: #checks third vertex
                
                #if any of the adjacency lists are empty (nan used for placeholder) SKIP thia iteration
                if ( (np.isnan(vertex1)) | (np.isnan(vertex2)) | (np.isnan(vertex3)) ):
                    #print("EMPTINESS DETECTED")
                    break
                
                if ((vertex2 not in adj_list_away[vertex1]) & (vertex3 not in adj_list_away[vertex1])
                    & (vertex2 not in adj_list_away[vertex3]) & (vertex3 not in adj_list_away[vertex2])
                    & (vertex2 != vertex3)):

                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict



def count_M11(adj_list_away, adj_list_toward):

    vertices = []
    
    for vertex1 in tqdm(adj_list_away): #checks each vertex1 node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            for vertex3 in adj_list_away[vertex1]:

                if ((vertex3 not in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                    & (vertex2 in adj_list_toward[vertex1]) & (vertex3 not in adj_list_toward[vertex1])
                    & (vertex2 != vertex3)):

                    vertices.append([vertex1, vertex2, vertex3])

    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle

    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):

        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else: #if edge does exist
                edge_dict[edge] += 1 #add to edge count

    return len(triangles), edge_dict






def count_M12(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for vertex1 in tqdm(adj_list_away): #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]:
                
                if ((vertex1 not in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])
                    & (vertex1 != vertex3)):
                    
                    vertices.append([vertex1, vertex2, vertex3])
                    
    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle
    
    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):
        
        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else:                            #if edge does exist
                edge_dict[edge] += 1 #add to edge count
    
    return len(triangles), edge_dict






def count_M13(adj_list_away, adj_list_toward):

    vertices = []
    
    for vertex1 in tqdm(adj_list_away): #checks each vertex1 node
        for vertex2 in adj_list_away[vertex1]: #checks first child node
            for vertex3 in adj_list_away[vertex1]:

                if ((vertex3 not in adj_list_away[vertex2]) & (vertex3 not in adj_list_toward[vertex2])
                    & (vertex2 in adj_list_toward[vertex1]) & (vertex3 in adj_list_toward[vertex1])
                    & (vertex2 != vertex3)):

                    vertices.append([vertex1, vertex2, vertex3])

    triangles = set(tuple(sorted(l)) for l in vertices) #get rid of permutations of the same triangle

    edge_dict = {}
    print("count edges")
    for tri in tqdm(triangles):

        combos = list(itertools.combinations(tri, 2))

        for edge in combos:

            if edge not in edge_dict.keys(): #if edge doesn't exist yet
                edge_dict[edge] = 1
            else: #if edge does exist
                edge_dict[edge] += 1 #add to edge count

    return len(triangles), edge_dict