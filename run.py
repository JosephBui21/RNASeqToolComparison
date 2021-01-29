#! /usr/bin/env python
import sys
import os
import json
sys.path.insert(0, 'src')
from etl import run_create_data_rscript, run_rscript_test
from analysis import run_diff_exp_rscript, run_comparison_rscript
import logging

logging.basicConfig(filename="log.txt", filemode='a',
 format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
 datefmt='%H:%M:%S',
 level=logging.DEBUG)

def main(targets):
    #Create synthetic data with parameters represents different number of samples per condition, truly differentially expressed genes, etc.
    if 'build' in targets:
        with open('config/build-params.json') as fh:
            data_cfg = json.load(fh)
        
        #All the synthetic data below is created with 12,500 genes and with 5 samples per condition
        
        #Create baseline synthetic data #1 with 0 differentially expressed genes
        baseline0_0 = run_create_data_rscript(data_cfg.get('data1'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file1'))
        
        #Create baseline synthetic data #2 with 1250 differentially expressed genes with 1250 upregulated in condition 1 & 0 downin condition 2
        baseline1250_0 = run_create_data_rscript(data_cfg.get('data2'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file2'))
        
        #Create baseline synthetic data #3 with 1250 differentially expressed genes with 625 upregulated in condition 1 & 625 downregulated in condition 2
        baseline625_625 = run_create_data_rscript(data_cfg.get('data3'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file3'))
        
        #Create baseline synthetic data #4 with 1250 differentially expressed genes with 4000 upregulated in condition 1 & 0 in condition 2
        baseline4000_0 = run_create_data_rscript(data_cfg.get('data4'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file4'))
        
        #Create baseline synthetic data #5 with 4000 differentially expressed genes with 2000 upregulated in condition 1 & 0 in condition 2
        baseline2000_2000 = run_create_data_rscript(data_cfg.get('data5'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp4000'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file5'))
        
        #Create synthetic data #6 whose counts were drawn from poisson distribution with 0 genes differentially expressed
        poisson0_0 = run_create_data_rscript(data_cfg.get('data6'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file6'))
        
        #Create synthetic data #7 whose counts were drawn from poisson distribution with 625 upregulated in condition 1 & 625 in condition 2
        poisson625_625 = run_create_data_rscript(data_cfg.get('data7'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file7'))
        
        #Create synthetic data #8 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 0 differentially expressed genes
        single0_0 = run_create_data_rscript(data_cfg.get('data8'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single0_0'), data_cfg.get('output_file8'))
        
        #Create synthetic data #9 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 625 genes expressed in cond 1 & 625 in cond 2
        single0_0 = run_create_data_rscript(data_cfg.get('data8'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single0_0'), data_cfg.get('output_file9'))
    
    
    
    #Run differential gene expression analysis tools on the synthetic data
    if 'analysis' in targets:
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)
        
        #Run DESeq2 on synthetic_data1 from above
        logging.info("Performing DESeq2 on baseline data with 0 genes differentially expressed...")
        deseq2_baseline0_0 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData1'),
                                            analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'),
                                            analysis_cfg.get('out_dir'))
        logging.info("Finished performing DESeq2 on synthetic dataset 1...")
        
        #Run DESeq2 on synthetic_data2 from above
        logging.info("Performing DESeq2 on baseline data with 1250 genes differentially expressed in condition 2 " + 
                    "& 0 in condition 1...")
        deseq2_baseline1250_0 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData2'),
                                            analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'),
                                            analysis_cfg.get('out_dir'))
        logging.info("Finished performing DESeq2 on synthetic dataset 2...")
        
        #Run DESeq2 on synthetic_data3 from above
        logging.info("Performing DESeq2 on baseline data with 625 genes differentially expressed in condition 2 " + 
                    "& 625 in condition 1...")
        deseq2_baseline625_625 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData3'),
                                            analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'),
                                            analysis_cfg.get('out_dir'))
        logging.info("Finished performing DESeq2 on synthetic dataset 3...")
        
        #Run DESeq2 on synthetic_data4 from above
        logging.info("Performing DESeq2 on baseline data with 4000 genes differentially expressed in condition 2 " + 
                    "& 0 in condition 1...")
        deseq2_baseline4000_0 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData4'),
                                            analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'),
                                            analysis_cfg.get('out_dir'))
        logging.info("Finished performing DESeq2 on synthetic dataset 4...")
        
        #Run edgeR on synthetic_data1 from above
        logging.info("Performing edgeR on baseline data with 0 genes differentially expressed...")
        edgeR_baseline0_0 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData1'), 
                                           analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'),
                                           analysis_cfg.get('out_dir'))
        logging.info("Finished performing edgeR on sythetic dataset 1...")
        
        #Run edgeR on synthetic_data2 from above
        logging.info("Performing edgeR on baseline data with 1250 genes differentially expressed in condition 2 " +
                    "& 0 in condition 1")
        edgeR_baseline1250_0 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData2'), 
                                           analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'),
                                           analysis_cfg.get('out_dir'))
        logging.info("Finished performing edgeR on sythetic dataset 2...")
        
        #Run edgeR on synthetic_data3 from above
        logging.info("Performing edgeR on baseline data with 625 genes differentially expressed in condition 2 " +
                    "& 625 in condition 1")
        edgeR625_625 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData3'), 
                                           analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'),
                                           analysis_cfg.get('out_dir'))
        logging.info("Finished performing edgeR on sythetic dataset 3...")
        
        #Run edgeR on synthetic_data4 from above
        logging.info("Performing edgeR on baseline data with 4000 genes differentially expressed in condition 2 " +
                    "& 0 in condition 1")
        edgeR4000_0 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData4'), 
                                           analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'),
                                           analysis_cfg.get('out_dir'))
        logging.info("Finished performing edgeR on sythetic dataset 4...")
    
    if 'compare' in targets:
        with open('config/comparison-params.json') as fh:
            compare_data_cfg = json.load(fh)
        #comparison of DESeq2 & edgeR on baseline data with 0 differentially expressed
        deseq2_edgeR_b_0_0 = run_comparison_rscript(compare_data_cfg.get('in_dir'), compare_data_cfg.get('deseq2'),
                                                    compare_data_cfg.get('edgeR'))
        
    
    
    if 'test' in targets:
        with open('config/test-params.json') as fh:
            t_data_cfg = json.load(fh)
        testing = run_rscript_test(**t_data_cfg)
    return

if __name__ == '__main__':
    targets = sys.argv[1]
    main(targets)
