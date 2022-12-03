#each of the 13 motif counting functions are stored here

def count_M1(adj_list_away, adj_list_toward):

    vertices = [] #store vertices
    
    for vertex1 in adj_list_away: #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]: #access all possible nodes (vertex 3) from vertex 2
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 not in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])):
                    
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



def count_M2(adj_list_away, adj_list_toward):

    vertices = []
    
    for vertex1 in adj_list_away: #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]: #access all possible nodes (vertex 3) from vertex 2
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 not in adj_list_toward[vertex2]) & (vertex2 in adj_list_toward[vertex1])):
                    
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



def count_M3(adj_list_away, adj_list_toward):

    vertices = []
    
    for vertex1 in adj_list_away: #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]: #access all possible nodes (vertex 3) from vertex 2
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 in adj_list_toward[vertex2]) & (vertex2 in adj_list_toward[vertex1])):
                    
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



def count_M4(adj_list_away, adj_list_toward):

    vertices = []
    
    for vertex1 in adj_list_away: #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]: #access all possible nodes (vertex 3) from vertex 2
                
                if ((vertex1 in adj_list_away[vertex3]) & (vertex1 in adj_list_toward[vertex3])
                    & (vertex3 in adj_list_toward[vertex2]) & (vertex2 in adj_list_toward[vertex1])
                    & (vertex1 != vertex2) & (vertex1 != vertex3) & (vertex2 != vertex3)):
                    
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




def count_M5(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for parent in adj_list_away: #checks each parent node
        for child1 in adj_list_away[parent]: #checks first child node
            for child2 in adj_list_away[parent]: #checks second child node
                
                if ((child2 in adj_list_away[child1]) & (child2 not in adj_list_toward[child1])
                    & (child1 not in adj_list_toward[parent]) & (child2 not in adj_list_toward[parent])):
                    vertices.append([parent, child1, child2])
                    
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




def count_M6(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for parent in adj_list_away: #checks each parent node
        for child1 in adj_list_away[parent]: #checks first child node
            for child2 in adj_list_away[parent]: #checks second child node
                
                if ((child2 in adj_list_away[child1]) & (child2 in adj_list_toward[child1])
                    & (child1 not in adj_list_toward[parent]) & (child2 not in adj_list_toward[parent])):
                    vertices.append([parent, child1, child2])
                    
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




def count_M7(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for parent1 in adj_list_away: #checks each parent node
        for parent2 in adj_list_away: #checks first child node
            for child in adj_list_away[parent1]: #checks second child node
                
                if ((child in adj_list_away[parent2]) & (parent1 in adj_list_away[parent2])
                    & (parent2 in adj_list_away[parent1]) & (child not in adj_list_toward[parent1])
                    & (child not in adj_list_toward[parent2])):
                    
                    vertices.append([parent1, parent2, child])
                    
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





def count_M8(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for parent in adj_list_away: #checks each parent node
        for child1 in adj_list_away[parent]: #checks first child node
            for child2 in adj_list_away[parent]: #checks second child node
                
                if ((child2 not in adj_list_away[child1]) & (child2 not in adj_list_toward[child1])
                    & (child1 not in adj_list_toward[parent]) & (child2 not in adj_list_toward[parent])
                    & (child1 != child2)):
                    
                    vertices.append([parent, child1, child2])
                    
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




def count_M9(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for vertex1 in adj_list_away: #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]: #access all possible nodes (vertex 3) from vertex 2
                
                if ((vertex1 not in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 not in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])
                    & (vertex1 != vertex3)):
                    
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





def count_M10(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for parent1 in adj_list_away: #checks each parent node
        for parent2 in adj_list_away: #checks first child node
            for child in adj_list_away[parent1]: #checks second child node
                
                if ((child in adj_list_away[parent2]) & (parent1 not in adj_list_away[parent2])
                    & (parent2 not in adj_list_away[parent1]) & (child not in adj_list_toward[parent1])
                    & (child not in adj_list_toward[parent2]) & (parent1 != parent2)):
                    
                    vertices.append([parent1, parent2, child])
                    
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





def count_M11(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for parent in adj_list_away: #checks each parent node
        for child1 in adj_list_away[parent]: #checks first child node
            for child2 in adj_list_away[parent]: #checks second child node
                
                if ((child2 not in adj_list_away[child1]) & (child2 not in adj_list_toward[child1])
                    & (child1 in adj_list_toward[parent]) & (child2 not in adj_list_toward[parent])
                    & (child1 != child2)):
                    
                    vertices.append([parent, child1, child2])
                    
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






def count_M12(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for vertex1 in adj_list_away: #checks each starting vertex
        for vertex2 in adj_list_away[vertex1]: #access all possible nodes (vertex 2) from vertex 1
            for vertex3 in adj_list_away[vertex2]: #access all possible nodes (vertex 3) from vertex 2
                
                if ((vertex1 not in adj_list_away[vertex3]) & (vertex1 not in adj_list_toward[vertex3])
                    & (vertex3 in adj_list_toward[vertex2]) & (vertex2 not in adj_list_toward[vertex1])
                    & (vertex1 != vertex3)):
                    
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






def count_M13(adj_list_away, adj_list_toward):
    
    vertices = []
    
    for parent in adj_list_away: #checks each parent node
        for child1 in adj_list_away[parent]: #checks first child node
            for child2 in adj_list_away[parent]: #checks second child node
                
                if ((child2 not in adj_list_away[child1]) & (child2 not in adj_list_toward[child1])
                    & (child1 in adj_list_toward[parent]) & (child2 in adj_list_toward[parent])
                    & (child1 != child2)):
                    
                    vertices.append([parent, child1, child2])
                    
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