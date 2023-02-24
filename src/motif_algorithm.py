#this file will be used to run each of the python files in the correct order

from .motif_counting import *
from .motif_adjacency_matrix import *
from .k_clusters import *
from .single_cluster import *

def run_single_cluster_algorithm(fp, motif):
    
    edge_counts = motif_counting(fp, motif)
    motif_adjacency_matrix = create_motif_adjacency_matrix(edge_counts)
    optimal_cluster = single_cluster(motif_adjacency_matrix)
    print("The optimal cluster has " + str(optimal_cluster.shape[0]) + " nodes.")
    print(optimal_cluster)
    return optimal_cluster


def run_k_clusters_algorithm(fp, motif, k):
    
    edge_counts = motif_counting(fp, motif)
    motif_adjacency_matrix = create_motif_adjacency_matrix(edge_counts)
    cluster_dict = k_clusters(motif_adjacency_matrix, k)
    print("Here are the clusters generated from k-means\n")
    print(cluster_dict)    
    return cluster_dict

def run_single_cluster_sampling_algorithm(fp, motif, threshold):
    
    edge_counts = sample_motif_counting(fp, motif, threshold)
    motif_adjacency_matrix = create_motif_adjacency_matrix(edge_counts)
    optimal_cluster = single_cluster(motif_adjacency_matrix)
    print("The optimal cluster has " + str(optimal_cluster.shape[0]) + " nodes.")
    print(optimal_cluster)
    return optimal_cluster


def run_k_clusters_sampling_algorithm(fp, motif, k, threshold):
    
    edge_counts = sample_motif_counting(fp, motif, sample_percent)
    motif_adjacency_matrix = create_motif_adjacency_matrix(edge_counts)
    cluster_dict = k_clusters(motif_adjacency_matrix, k)    
    return cluster_dict
    