import numpy as np
import pandas as pd

def create_motif_adjacency_matrix(edge_dict):
    
    #get all unique nodes
    first_half = [x[0] for x in edge_dict.keys()]
    second_half = [x[1] for x in edge_dict.keys()]
    combined = np.concatenate((first_half, second_half))
    
    unique_nodes = np.unique(combined)
    #unique_nodes = np.unique(data['FromNodeId'].tolist() + data['ToNodeId'].tolist())
    #max_node = unique_nodes.max()
    encoded_unique_nodes = [x for x in range(unique_nodes.shape[0])]
    print("encoding done")
    print(len(encoded_unique_nodes))
    #define an empty dataframe to use as the motif adjacency matrix
    #motif_adjacency_matrix = pd.DataFrame(index = unique_nodes, columns = unique_nodes)
    
    motif_adjacency_matrix = np.zeros((len(encoded_unique_nodes), len(encoded_unique_nodes)))
    
    #populate motif adjacency matrix
    for key, value in tqdm(edge_dict.items()):
        
        encoded_from = np.where(unique_nodes == key[0])[0][0]
        encoded_to = np.where(unique_nodes == key[1])[0][0]
        
        motif_adjacency_matrix[encoded_from][encoded_to] = value
        motif_adjacency_matrix[encoded_to][encoded_from] = value

    return motif_adjacency_matrix    
