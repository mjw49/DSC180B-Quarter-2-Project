#!/usr/bin/env python3

import sys
import json

from src import motif_algorithm
from motif_algorithm import run_algorithm

def main(targets):
    if 'test' in targets:
        with open('config/motif-algorithm-params.json') as fh:
            data_params = json.load(fh)
        run_algorithm(**data_params)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
