import numpy as np
import pandas as pd

def create_motif_adjacency_matrix(fp):
    
    #get all unique nodes
    first_half = [x[0] for x in edge_dict.keys()]
    second_half = [x[1] for x in edge_dict.keys()]
    combined = np.concatenate((first_half, second_half))
    
    unique_nodes = np.unique(combined)
    
    #define an empty dataframe to use as the motif adjacency matrix
    motif_adjacency_matrix = pd.DataFrame(index = unique_nodes, columns = unique_nodes)
    
    #populate motif adjacency matrix
    for key, value in edge_dict.items():
        motif_adjacency_matrix[key[0]][key[1]] = value
        motif_adjacency_matrix[key[1]][key[0]] = value

    motif_adjacency_matrix = motif_adjacency_matrix.fillna(0)
    
    return motif_adjacency_matrix.values
