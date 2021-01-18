#! /usr/bin/env python
import sys
import os
import json
sys.path.insert(0, 'src')
from etl import run_rscript, run_rscript_test


def main(targets):
    if 'build' in targets:
        with open('config/build-params.json') as fh:
            data_cfg = json.load(fh)
        
        #Create synthetic data #1 with 5 samples per conditon & 200 differentially expressed genes
        synthetic_data1 = run_rscript(data_cfg.get('data1'), data_cfg.get('n_vars1'), data_cfg.get('samples_per_cond1'), 
                                      data_cfg.get('n_diffexp1'), data_cfg.get('output_file1'))
        #Create synthetic data #2 with 5 samples per conditon & 500 differentially expressed genes
        synthetic_data2 = run_rscript(data_cfg.get('data2'), data_cfg.get('n_vars1'), data_cfg.get('samples_per_cond1'), 
                                      data_cfg.get('n_diffexp2'), data_cfg.get('output_file2'))
    
    if 'test' in targets:
        with open('config/test-params.json') as fh:
            t_data_cfg = json.load(fh)
        testing = run_rscript_test(**t_data_cfg)
    return

if __name__ == '__main__':
    targets = sys.argv[1]
    main(targets)
