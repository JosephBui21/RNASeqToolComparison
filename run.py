#! /usr/bin/env python
import sys
import os
import json
sys.path.insert(0, 'src')
from etl import create_synthetic_data


def main(targets):
    if 'build' in targets:
        with open('config/build-params.json') as fh:
            data_cfg = json.load(fh)

        synthetic_data = create_synthetic_data(**data_cfg)
    return

if __name__ == '__main__':
    targets = sys.argv[1]
    main(targets)