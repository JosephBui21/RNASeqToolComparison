#! /usr/bin/env python
import sys
import os
import json
sys.path.insert(0, 'src')
from etl import run_create_data_rscript, run_rscript_test
from analysis import run_diff_exp_rscript

def main(targets):
    #Create synthetic data with parameters represents different number of samples per condition, truly differentially expressed genes, etc.
    if 'build' in targets:
        with open('config/build-params.json') as fh:
            data_cfg = json.load(fh)
        
        #All the synthetic data below is created with 12,500 genes and with 5 samples per condition
        #Create baseline synthetic data #1 with 0 differentially expressed genes
        baseline0_0 = run_create_data_rscript(data_cfg.get('data1'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp1'), data_cfg.get('upregulated_ratio1'), data_cfg.get('output_file1'))
        
        #Create baseline synthetic data #2 with 1250 differentially expressed genes with 1250 upregulated in condition 1 & 0 downin condition 2
        baseline1250_0 = run_create_data_rscript(data_cfg.get('data2'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp2'), data_cfg.get('upregulated_ratio1'), data_cfg.get('output_file2'))
        
        #Create baseline synthetic data #3 with 1250 differentially expressed genes with 625 upregulated in condition 1 & 625 downregulated in condition 2
        baseline625_625 = run_create_data_rscript(data_cfg.get('data3'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp2'), data_cfg.get('upregulated_ratio2'), data_cfg.get('output_file3'))
        
        #Create baseline synthetic data #4 with 1250 differentially expressed genes with 4000 upregulated in condition 1 & 0 in condition 2
        baseline4000_0 = run_create_data_rscript(data_cfg.get('data4'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp3'), data_cfg.get('upregulated_ratio1'), data_cfg.get('output_file4'))
    
    #Run differential gene expression analysis tools on the synthetic data
    if 'analysis' in targets:
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)
        
        #Run DESeq2 on synthetic_data1 from above
        deseq2_data1 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData1'),
                                            analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'),
                                            analysis_cfg.get('out_dir'))
        
        #Run edgeR on synthetic_data1 from above
        edgeR_data1 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData1'), 
                                           analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'),
                                           analysis_cfg.get('out_dir'))
        
        #Run DESeq2 on synthetic_data2 from above
        deseq2_data2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData2'),
                                            analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'),
                                            analysis_cfg.get('out_dir'))
        
        #Run edgeR on synthetic_data2 from above
        edgeR_data1 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData2'), 
                                           analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'),
                                           analysis_cfg.get('out_dir'))
        
    
    
    if 'test' in targets:
        with open('config/test-params.json') as fh:
            t_data_cfg = json.load(fh)
        testing = run_rscript_test(**t_data_cfg)
    return

if __name__ == '__main__':
    targets = sys.argv[1]
    main(targets)
