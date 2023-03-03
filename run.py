#!/usr/bin/env python3

import sys
import json

from src import motif_algorithm

def main(targets):
    if 'test' in targets:
        with open('config/k-clusters-test-params.json') as fh:
            data_params = json.load(fh)
        print("starting k cluster algorithm on test target\n")
        motif_algorithm.run_k_clusters_algorithm(**data_params)

        with open('config/single-cluster-test-params.json') as fh:
            data_params = json.load(fh)
        print("\n\nstarting single cluster algorithm on test target\n")
        motif_algorithm.run_single_cluster_algorithm(**data_params)

    if 'city_single' in targets:
        with open('config/city-single-cluster-params.json') as fh:
            data_params = json.load(fh)
        motif_algorithm.run_single_cluster_algorithm(**data_params)

    if 'stanford_single' in targets:
        with open('config/stanford-single-cluster-params.json') as fh:
            data_params = json.load(fh)
        motif_algorithm.run_single_cluster_algorithm(**data_params)

    if 'sampling_city_single' in targets:
        with open('config/city-single-cluster-sampling-params.json') as fh:
            data_params = json.load(fh)
        motif_algorithm.run_single_cluster_sampling_algorithm(**data_params)

    if 'sampling_stanford_single' in targets:
        with open('config/stanford-single-cluster-sampling-params.json') as fh:
            data_params = json.load(fh)
        motif_algorithm.run_single_cluster_sampling_algorithm(**data_params)

    if 'sampling_email_single' in targets:
        with open('config/email-single-cluster-sampling-params.json') as fh:
            data_params = json.load(fh)
        motif_algorithm.run_single_cluster_sampling_algorithm(**data_params)

    if 'sampling_email_k' in targets:
        with open('config/email-k-clusters-sampling-params.json') as fh:
            data_params = json.load(fh)
        motif_algorithm.run_k_clusters_sampling_algorithm(**data_params)

    if 'sampling_physics_single' in targets:
        with open('config/physics-single-cluster-sampling-params.json') as fh:
            data_params = json.load(fh)
        motif_algorithm.run_single_cluster_sampling_algorithm(**data_params)

    if 'sampling_physics_k' in targets:
        with open('config/physics-k-clusters-sampling-params.json') as fh:
            data_params = json.load(fh)
        motif_algorithm.run_k_clusters_sampling_algorithm(**data_params)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
