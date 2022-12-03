import pandas as pd
import numpy as np
import itertools

#import motif counting functions from motif-counters.py
from .motif_counters import *

def motif_counting(fp, motif):
    
    '''
    Input: filepath to transformed data (fp), motif (type of triangular pattern to count)
    Output: a dictionary mapping each node i to its assigned cluster
    '''
    
    #read in file path
    data = pd.read_csv(fp, delimiter = ' ', usecols = ['FromNodeId', 'ToNodeId'])
    
    #initialize adjacency lists
    min_node = min(data['FromNodeId'].min(), data['ToNodeId'].min())
    max_node = max(data['FromNodeId'].max(), data['ToNodeId'].max())

    adj_list_away = {}
    adj_list_toward = {}

    for node in range(min_node, max_node+1):
        adj_list_away[node] = []
        adj_list_toward[node] = []
        
    #add an edge with a given start and end node to a given adjacency list 
    def add_edge(adj_list, node, target):
        adj_list[int(node)].append(int(target))
    
    for idx, row in data.iterrows():
        add_edge(adj_list_away, row.FromNodeId, row.ToNodeId)
        add_edge(adj_list_toward, row.ToNodeId, row.FromNodeId)
    
    #count the given pattern
    if motif == 'M1':
        motif_count, edge_dict = count_M1(adj_list_away, adj_list_toward)
        
    if motif == 'M2':
        motif_count, edge_dict = count_M2(adj_list_away, adj_list_toward)
        
    if motif == 'M3':
        motif_count, edge_dict = count_M3(adj_list_away, adj_list_toward)
        
    if motif == 'M4':
        motif_count, edge_dict = count_M4(adj_list_away, adj_list_toward)
        
    if motif == 'M5':
        motif_count, edge_dict = count_M5(adj_list_away, adj_list_toward)
        
    if motif == 'M6':
        motif_count, edge_dict = count_M6(adj_list_away, adj_list_toward)
    
    if motif == 'M7':
        motif_count, edge_dict = count_M7(adj_list_away, adj_list_toward)
        
    if motif == 'M8':
        motif_count, edge_dict = count_M8(adj_list_away, adj_list_toward)
        
    if motif == 'M9':
        motif_count, edge_dict = count_M9(adj_list_away, adj_list_toward)
    
    if motif == 'M10':
        motif_count, edge_dict = count_M10(adj_list_away, adj_list_toward)
        
    if motif == 'M11':
        motif_count, edge_dict = count_M11(adj_list_away, adj_list_toward)
        
    if motif == 'M12':
        motif_count, edge_dict = count_M12(adj_list_away, adj_list_toward)
        
    if motif == 'M13':
        motif_count, edge_dict = count_M13(adj_list_away, adj_list_toward)
    
    #display motif count
    print("The number of instances of " + motif + " is " + str(motif_count))
    
    #return the edge dictionary
    return edge_dict