#! /usr/bin/env python
import sys
import os
import json
sys.path.insert(0, 'src')
from etl import run_create_data_rscript
from analysis import run_diff_exp_rscript, run_comparison_rscript
from test import run_test_rscript
import logging
from datetime import datetime

logging.basicConfig(filename="log.txt", filemode='a',
 datefmt='%H:%M:%S',
 level=logging.INFO)

def main(targets):
    #Create synthetic data with parameters represents different number of samples per condition, truly differentially expressed genes, etc.
    if 'build' in targets:
        with open('config/build-params.json') as fh:
            data_cfg = json.load(fh)

        #All the synthetic data below is created with 12,500 genes
        for i in range(1, 11):
            
            #Create baseline synthetic data #1 with 0 differentially expressed genes for 2 samples per condition 10x
            print("Generating baseline synthetic data v" + str(i) + " with 0 differentially expressed genes for 2 samples per condition")
            baseline0_0_2 = run_create_data_rscript(data_cfg.get("b0_0_2_v" + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond2'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get("output_fileB0_0_2_v" + str(i)), data_cfg.get('seqdepth'))
            
            #Create baseline synthetic data #1 with 0 differentially expressed genes for 5 samples per condition 10x
#             print("Generating baseline synthetic data v" + str(i) + " with 0 differentially expressed genes for 5 samples per condition")
#             baseline0_0_5 = run_create_data_rscript(data_cfg.get("b0_0_5_v" + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get("output_fileB0_0_5_v" + str(i)), data_cfg.get('seqdepth'))

            #Create baseline synthetic data #1 with 0 differentially expressed genes for 10 samples per condition 10x
            print("Generating baseline synthetic data v" + str(i) + " with 0 differentially expressed genes for 10 samples per condition")
            baseline0_0_10 = run_create_data_rscript(data_cfg.get("b0_0_10_v" + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond10'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get("output_fileB0_0_10_v" + str(i)), data_cfg.get('seqdepth'))
            
            #Create baseline synthetic data #2 with 1250 differentially expressed genes with 1250 upregulated in condition 1 and 0 downregulated in condition 2 for 2 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 1250 upregulated in condition 1 and 0 downregulated in condition 2 for 2 samples per condition")
            baseline1250_0_2 = run_create_data_rscript(data_cfg.get('b1250_0_2_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond2'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB1250_0_2_v' + str(i)), data_cfg.get('seqdepth'))
            
            #Create baseline synthetic data #2 with 1250 differentially expressed genes with 1250 upregulated in condition 1 and 0 downregulated in condition 2 for 5 samples per condition
#             print("Generating baseline synthetic data v" + str(i) + " with 1250 upregulated in condition 1 and 0 downregulated in condition 2 for 5 samples per condition")
#             baseline1250_0_5 = run_create_data_rscript(data_cfg.get('b1250_0_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB1250_0_5_v' + str(i)), data_cfg.get('seqdepth'))
            
            #Create baseline synthetic data #2 with 1250 differentially expressed genes with 1250 upregulated in condition 1 and 0 downregulated in condition 2 for 10 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 1250 upregulated in condition 1 and 0 downregulated in condition 2 for 10 samples per condition")
            baseline1250_0_10 = run_create_data_rscript(data_cfg.get('b1250_0_10_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond10'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB1250_0_10_v' + str(i)), data_cfg.get('seqdepth'))

            #Create baseline synthetic data #3 with 1250 differentially expressed genes with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 2 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 625 upregulated in condition 1 and 625 downregulated in condition 2 for 2 samples per condition")
            baseline625_625_2 = run_create_data_rscript(data_cfg.get('b625_625_2_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond2'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB625_625_2_v' + str(i)), data_cfg.get('seqdepth'))
            
            #Create baseline synthetic data #3 with 1250 differentially expressed genes with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 5 samples per condition
#             print("Generating baseline synthetic data v" + str(i) + " with 625 upregulated in condition 1 and 625 downregulated in condition 2 for 5 samples per condition")
#             baseline625_625_5 = run_create_data_rscript(data_cfg.get('b625_625_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB625_625_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create baseline synthetic data #3 with 1250 differentially expressed genes with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 10 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 625 upregulated in condition 1 and 625 downregulated in condition 2 for 10 samples per condition")
            baseline625_625_10 = run_create_data_rscript(data_cfg.get('b625_625_10_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond10'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB625_625_10_v' + str(i)), data_cfg.get('seqdepth'))

            #Create baseline synthetic data #4 with 4000 differentially expressed genes with 4000 upregulated in condition 1 & 0 in condition 2 for 2 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 4000 upregulated in condition 1 and 0 downregulated in condition 2 for 2 samples per condition")
            baseline4000_0_2 = run_create_data_rscript(data_cfg.get('b4000_0_2_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond2'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp4000'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB4000_0_2_v' + str(i)), data_cfg.get('seqdepth'))            
            
            #Create baseline synthetic data #4 with 4000 differentially expressed genes with 4000 upregulated in condition 1 & 0 in condition 2 for 5 samples per condition
#             print("Generating baseline synthetic data v" + str(i) + " with 4000 upregulated in condition 1 and 0 downregulated in condition 2 for 5 samples per condition")
#             baseline4000_0_5 = run_create_data_rscript(data_cfg.get('b4000_0_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp4000'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB4000_0_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create baseline synthetic data #4 with 4000 differentially expressed genes with 4000 upregulated in condition 1 & 0 in condition 2 for 10 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 4000 upregulated in condition 1 and 0 downregulated in condition 2 for 10 samples per condition")
            baseline4000_0_10 = run_create_data_rscript(data_cfg.get('b4000_0_10_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond10'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp4000'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB4000_0_10_v' + str(i)), data_cfg.get('seqdepth'))

            #Create baseline synthetic data #5 with 4000 differentially expressed genes with 2000 upregulated in condition 1 & 2000 in condition 2 for 2 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 2000 upregulated in condition 1 & 2000 in condition 2 for 2 samples per condition")
            baseline2000_2000_2 = run_create_data_rscript(data_cfg.get('b2000_2000_2_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond2'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp4000'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB2000_2000_2_v' + str(i)), data_cfg.get('seqdepth'))
            
            #Create baseline synthetic data #5 with 4000 differentially expressed genes with 2000 upregulated in condition 1 & 2000 in condition 2 for 5 samples per condition
#             print("Generating baseline synthetic data v" + str(i) + " with 2000 upregulated in condition 1 & 2000 in condition 2 for 5 samples per condition")
#             baseline2000_2000_5 = run_create_data_rscript(data_cfg.get('b2000_2000_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp4000'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB2000_2000_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create baseline synthetic data #5 with 4000 differentially expressed genes with 2000 upregulated in condition 1 & 2000 in condition 2 for 10 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 2000 upregulated in condition 1 & 2000 in condition 2 for 10 samples per condition")
            baseline2000_2000_10 = run_create_data_rscript(data_cfg.get('b2000_2000_10_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond10'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp4000'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB2000_2000_10_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #6 whose counts were drawn from poisson distribution with 0 genes differentially expressed for 2 samples per condition
            print("Generating poisson synthetic data v" + str(i) + " with 0 differentially expressed for 2 samples per condition")
            poisson0_0_2 = run_create_data_rscript(data_cfg.get('p0_0_2_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond2'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileP0_0_2_v' + str(i)), data_cfg.get('seqdepth'))
            
            #Create synthetic data #6 whose counts were drawn from poisson distribution with 0 genes differentially expressed for 5 samples per condition
#             print("Generating poisson synthetic data v" + str(i) + " with 0 differentially expressed for 5 samples per condition")
#             poisson0_0_5 = run_create_data_rscript(data_cfg.get('p0_0_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileP0_0_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #6 whose counts were drawn from poisson distribution with 0 genes differentially expressed for 10 samples per condition
            print("Generating poisson synthetic data v" + str(i) + " with 0 differentially expressed for 10 samples per condition")
            poisson0_0_10 = run_create_data_rscript(data_cfg.get('p0_0_10_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond10'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileP0_0_10_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #7 whose counts were drawn from poisson distribution with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 2 samples per condition
            print("Generating poisson synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 2 samples per condition")
            poisson625_625_2 = run_create_data_rscript(data_cfg.get('p625_625_2_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond2'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileP625_625_2_v' + str(i)), data_cfg.get('seqdepth'))
            
            #Create synthetic data #7 whose counts were drawn from poisson distribution with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 5 samples per condition
#             print("Generating poisson synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 5 samples per condition")
#             poisson625_625_5 = run_create_data_rscript(data_cfg.get('p625_625_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileP625_625_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #7 whose counts were drawn from poisson distribution with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 10 samples per condition
            print("Generating poisson synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 10 samples per condition")
            poisson625_625_10 = run_create_data_rscript(data_cfg.get('p625_625_10_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond10'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileP625_625_10_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #8 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 0 differentially expressed genes
            print("Generating single synthetic data v" + str(i) + " with 0 upregulated in condition 1 & 0 downregulated in condition 2 for 2 samples per condition")
            single0_0_2 = run_create_data_rscript(data_cfg.get('s0_0_2_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond2'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single_count'), data_cfg.get('output_fileS0_0_2_v' + str(i)), data_cfg.get('seqdepth'))
            
            #Create synthetic data #8 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 0 differentially expressed genes
#             print("Generating single synthetic data v" + str(i) + " with 0 upregulated in condition 1 & 0 downregulated in condition 2 for 5 samples per condition")
#             single0_0_5 = run_create_data_rscript(data_cfg.get('s0_0_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single_count'), data_cfg.get('output_fileS0_0_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #8 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 0 differentially expressed genes
            print("Generating single synthetic data v" + str(i) + " with 0 upregulated in condition 1 & 0 downregulated in condition 2 for 10 samples per condition")
            single0_0_10 = run_create_data_rscript(data_cfg.get('s0_0_10_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond10'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single_count'), data_cfg.get('output_fileS0_0_10_v' + str(i)), data_cfg.get('seqdepth'))

                #Create synthetic data #9 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 625 genes expressed in cond 1 & 625 in cond 2
            print("Generating single synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 2 samples per condition")
            single625_625_2 = run_create_data_rscript(data_cfg.get('s625_625_2_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond2'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single_count'), data_cfg.get('output_fileS625_625_2_v' + str(i)), data_cfg.get('seqdepth'))
            
                #Create synthetic data #9 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 625 genes expressed in cond 1 & 625 in cond 2
#             print("Generating single synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 5 samples per condition")
#             single625_625_5 = run_create_data_rscript(data_cfg.get('s625_625_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single_count'), data_cfg.get('output_fileS625_625_5_v' + str(i)), data_cfg.get('seqdepth'))

                #Create synthetic data #9 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 625 genes expressed in cond 1 & 625 in cond 2
            print("Generating single synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 10 samples per condition")
            single625_625_10 = run_create_data_rscript(data_cfg.get('s625_625_10_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond10'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single_count'), data_cfg.get('output_fileS625_625_10_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #10 where fraction of genes for which we selected a random sample and multiplied the corresponding count with a factor between 5 and 10 with 0 differentially expressed genes
            print("Generating random synthetic data v" + str(i) + " with 0 upregulated in condition 1 & 0 downregulated in condition 2 for 2 samples per condition")
            random0_0_2 = run_create_data_rscript(data_cfg.get('r0_0_2_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond2'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type3'), data_cfg.get('random_outlier'), data_cfg.get('output_fileR0_0_2_v' + str(i)), data_cfg.get('seqdepth'))            
            
            #Create synthetic data #10 where fraction of genes for which we selected a random sample and multiplied the corresponding count with a factor between 5 and 10 with 0 differentially expressed genes
#             print("Generating random synthetic data v" + str(i) + " with 0 upregulated in condition 1 & 0 downregulated in condition 2 for 5 samples per condition")
#             random0_0_5 = run_create_data_rscript(data_cfg.get('r0_0_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type3'), data_cfg.get('random_outlier'), data_cfg.get('output_fileR0_0_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #10 where fraction of genes for which we selected a random sample and multiplied the corresponding count with a factor between 5 and 10 with 0 differentially expressed genes
            print("Generating random synthetic data v" + str(i) + " with 0 upregulated in condition 1 & 0 downregulated in condition 2 for 10 samples per condition")
            random0_0_10 = run_create_data_rscript(data_cfg.get('r0_0_10_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond10'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type3'), data_cfg.get('random_outlier'), data_cfg.get('output_fileR0_0_10_v' + str(i)), data_cfg.get('seqdepth'))

             #Create synthetic data #11 where fraction of genes for which we selected a random sample and multiplied the corresponding count with a factor between 5 and 10 with 625 genes expressed in cond 1 & 625 in cond 2
            print("Generating random synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 2 samples per condition")
            random625_625_2 = run_create_data_rscript(data_cfg.get('r625_625_2_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond2'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type3'), data_cfg.get('random_outlier'), data_cfg.get('output_fileR625_625_2_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #11 where fraction of genes for which we selected a random sample and multiplied the corresponding count with a factor between 5 and 10 with 625 genes expressed in cond 1 & 625 in cond 2
#             print("Generating random synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 5 samples per condition")
#             random625_625_5 = run_create_data_rscript(data_cfg.get('r625_625_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type3'), data_cfg.get('random_outlier'), data_cfg.get('output_fileR625_625_5_v' + str(i)), data_cfg.get('seqdepth'))

             #Create synthetic data #11 where fraction of genes for which we selected a random sample and multiplied the corresponding count with a factor between 5 and 10 with 625 genes expressed in cond 1 & 625 in cond 2
            print("Generating random synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 10 samples per condition")
            random625_625_10 = run_create_data_rscript(data_cfg.get('r625_625_10_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond10'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type3'), data_cfg.get('random_outlier'), data_cfg.get('output_fileR625_625_10_v' + str(i)), data_cfg.get('seqdepth'))



    #Run differential gene expression analysis tools on the synthetic data
    if 'analysis' in targets:
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)

        for i in range(1, 11):

            #Run DESeq2 on the synthetic datasets above
            
            #Run DESeq2 on baseline0_0 with 2 samples per cond
            deseq2_b0_0_2_start = datetime.now()
            deseq2_b0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_2_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_b0_0_2_dir'))
            deseq2_b0_0_2_end = datetime.now()
            logging.info("Elapsed time for DESeq2 for baseline0_0_2_v" + str(i) + " " + str(deseq2_b0_0_2_end - deseq2_b0_0_2_start))
            
            #Run DESeq2 on baseline1250_0 with 2 samples per cond
            deseq2_b1250_0_2_start = datetime.now()
            deseq2_b1250_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_2_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_b1250_0_2_dir'))
            deseq2_b1250_0_2_end = datetime.now()
            logging.info("Elapsed time for DESeq2 for baseline1250_0_2_v" + str(i) + " " + str(deseq2_b1250_0_2_end - deseq2_b1250_0_2_start))
            
            #Run DESeq2 on baseline625_625 with 2 samples per cond
            deseq2_b625_625_2_start = datetime.now()
            deseq2_b625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_2_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_b625_625_2_dir'))
            deseq2_b625_625_2end = datetime.now()
            logging.info("Elapsed time for DESeq2 for baseline625_625_2_v" + str(i) + " " + str(deseq2_b625_625_2end - deseq2_b625_625_2_start))
            
            #Run DESeq2 on baseline4000_0 with 2 samples per cond
            deseq2_b4000_0_2_start = datetime.now()
            deseq2_b4000_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_2_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_b4000_0_2_dir'))
            deseq2_b4000_0_2end = datetime.now()
            logging.info("Elapsed time for DESeq2 for baseline4000_0_2_v" + str(i) + " " + str(deseq2_b4000_0_2end - deseq2_b4000_0_2_start))
            
            #Run DESeq2 on baseline2000_2000 with 2 samples per cond
            deseq2_b2000_2000_2_start = datetime.now()
            deseq2_b2000_2000_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_2_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_b2000_2000_2_dir'))
            deseq2_b2000_2000_2end = datetime.now()
            logging.info("Elapsed time for DESeq2 for baseline2000_2000_2_v" + str(i) + " " + str(deseq2_b2000_2000_2end - deseq2_b2000_2000_2_start))
            
            #Run DESeq2 on poisson0_0 with 2 samples per cond
            deseq2_p0_0_2_start = datetime.now()
            deseq2_p0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_2_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_p0_0_2_dir'))
            deseq2_p0_0_2_end = datetime.now()
            logging.info("Elapsed time for DESeq2 for poisson0_0_2_v" + str(i) + " " + str(deseq2_p0_0_2_end - deseq2_p0_0_2_start))
            
            #Run DESeq2 on poisson625_625 with 2 samples per cond
            deseq2_p625_625_2_start = datetime.now()
            deseq2_p625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_2_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_p625_625_2_dir'))
            deseq2_p625_625_2_end = datetime.now()
            logging.info("Elapsed time for DESeq2 for poisson625_625_2_v" + str(i) + " " + str(deseq2_p625_625_2_end - deseq2_p625_625_2_start))
            
            #Run DESeq2 on single0_0 with 2 samples per cond
            deseq2_s0_0_2_start = datetime.now()
            deseq2_s0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_2_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_s0_0_2_dir'))
            deseq2_s0_0_2_end = datetime.now()
            logging.info("Elapsed time for DESeq2 for single0_0_2_v" + str(i) + " " + str(deseq2_s0_0_2_end - deseq2_s0_0_2_start))
            
            #Run DESeq2 on single625_625 with 2 samples per cond
            deseq2_s625_625_2_start = datetime.now()
            deseq2_s625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_2_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_s625_625_2_dir'))
            deseq2_s625_625_2_end = datetime.now()
            logging.info("Elapsed time for DESeq2 for single625_625_2_v" + str(i) + " " + str(deseq2_s625_625_2_end - deseq2_s625_625_2_start))
            
            #Run DESeq2 on random0_0 with 2 samples per cond
            deseq2_r0_0_2_start = datetime.now()
            deseq2_r0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_2_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_r0_0_2_dir'))
            deseq2_r0_0_2_end = datetime.now()
            logging.info("Elapsed time for DESeq2 for random0_0_2_v" + str(i) + " " + str(deseq2_r0_0_2_end - deseq2_r0_0_2_start))
            
            #Run DESeq2 on random625_625 with 2 samples per cond
            deseq2_r625_625_2_start = datetime.now()
            deseq2_r625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_2_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_r625_625_2_dir'))
            deseq2_r625_625_2_end = datetime.now()
            logging.info("Elapsed time for DESeq2 for random625_625_2_v" + str(i) + " " + str(deseq2_r625_625_2_end - deseq2_r625_625_2_start))
            
            #Run edgeR on the synthetic datasets above
            
            #Run edgeR on baseline0_0 with 2 samples per cond
            edgeR_b0_0_2_start = datetime.now()
            edgeR_b0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_2_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_b0_0_2_dir'))
            edgeR_b0_0_2_end = datetime.now()
            logging.info("Elapsed time for edgeR for baseline0_0_2_v" + str(i) + " " + str(edgeR_b0_0_2_end - edgeR_b0_0_2_start))
            
#             #Run edgeR on baseline1250_0 with 2 samples per cond
            edgeR_b1250_0_2_start = datetime.now()
            edgeR_b1250_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_2_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_b1250_0_2_dir'))
            edgeR_b1250_0_2end = datetime.now()
            logging.info("Elapsed time for edgeR for baseline1250_0_2_v" + str(i) + " " + str(edgeR_b1250_0_2end - edgeR_b1250_0_2_start))
            
#             #Run edgeR on baseline625_625 with 2 samples per cond
            edgeR_b625_625_2_start = datetime.now()
            edgeR_b625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_2_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_b625_625_2_dir'))
            edgeR_b625_625_2end = datetime.now()
            logging.info("Elapsed time for edgeR for baseline625_625_2_v" + str(i) + " " + str(edgeR_b625_625_2end - edgeR_b625_625_2_start))
            
#             #Run edgeR on baseline4000_0 with 2 samples per cond
            edgeR_b4000_0_2_start = datetime.now()
            edgeR_b4000_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_2_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_b4000_0_2_dir'))
            edgeR_b4000_0_2end = datetime.now()
            logging.info("Elapsed time for edgeR for baseline4000_0_2_v" + str(i) + " " + str(edgeR_b4000_0_2end - edgeR_b4000_0_2_start))
            
#             #Run edgeR on baseline2000_2000 with 2 samples per cond
            edgeR_b2000_2000_2_start = datetime.now()
            edgeR_b2000_2000_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_2_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_b2000_2000_2_dir'))
            edgeR_b2000_2000_2end = datetime.now()
            logging.info("Elapsed time for edgeR for baseline2000_2000_2_v" + str(i) + " " + str(edgeR_b2000_2000_2end - edgeR_b2000_2000_2_start))
            
#             #Run edgeR on poisson0_0 with 2 samples per cond
            edgeR_p0_0_2_start = datetime.now()
            edgeR_p0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_2_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_p0_0_2_dir'))
            edgeR_p0_0_2_end = datetime.now()
            logging.info("Elapsed time for edgeR for poisson0_0_2_v" + str(i) + " " + str(edgeR_p0_0_2_end - edgeR_p0_0_2_start))
            
#             #Run edgeR on poisson625_625 with 2 samples per cond
            edgeR_p625_625_2_start = datetime.now()
            edgeR_p625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_2_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_p625_625_2_dir'))
            edgeR_p625_625_2_end = datetime.now()
            logging.info("Elapsed time for edgeR for poisson625_625_2_v" + str(i) + " " + str(edgeR_p625_625_2_end - edgeR_p625_625_2_start))
            
#             #Run edgeR on single0_0 with 2 samples per cond
            edgeR_s0_0_2_start = datetime.now()
            edgeR_s0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_2_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_s0_0_2_dir'))
            edgeR_s0_0_2_end = datetime.now()
            logging.info("Elapsed time for edgeR for single0_0_2_v" + str(i) + " " + str(edgeR_s0_0_2_end - edgeR_s0_0_2_start))
            
#             #Run edgeR on single625_625 with 2 samples per cond
            edgeR_s625_625_2_start = datetime.now()
            edgeR_s625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_2_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_s625_625_2_dir'))
            edgeR_s625_625_2_end = datetime.now()
            logging.info("Elapsed time for edgeR for single625_625_2_v" + str(i) + " " + str(edgeR_s625_625_2_end - edgeR_s625_625_2_start))
            
#             #Run edgeR on random0_0 with 2 samples per cond
            edgeR_r0_0_2_start = datetime.now()
            edgeR_r0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_2_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_r0_0_2_dir'))
            edgeR_r0_0_2_end = datetime.now()
            logging.info("Elapsed time for edgeR for random0_0_2_v" + str(i) + " " + str(edgeR_r0_0_2_end - edgeR_r0_0_2_start))
            
#             #Run edgeR on random625_625 with 2 samples per cond
            edgeR_r625_625_2_start = datetime.now()
            edgeR_r625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_2_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_r625_625_2_dir'))
            edgeR_r625_625_2_end = datetime.now()
            logging.info("Elapsed time for edgeR for random625_625_2_v" + str(i) + " " + str(edgeR_r625_625_2_end - edgeR_r625_625_2_start))


            #Run voom.limma on the synthetic datasets above
            
            #Run voom.limma on baseline0_0 with 2 samples per cond
            voom_b0_0_2_start = datetime.now()
            voom_b0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_2_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_b0_0_2_dir'))
            voom_b0_0_2_end = datetime.now()
            logging.info("Elapsed time for voom.limma for baseline0_0_2_v" + str(i) + " " + str(voom_b0_0_2_end - voom_b0_0_2_start))
            
#             #Run voom.limma on baseline1250_0 with 2 samples per cond
            voom_b1250_0_2_start = datetime.now()
            voom_b1250_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_2_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_b1250_0_2_dir'))
            voom_b1250_0_2end = datetime.now()
            logging.info("Elapsed time for voom.limma for baseline1250_0_2_v" + str(i) + " " + str(voom_b1250_0_2end - voom_b1250_0_2_start))
            
#             #Run voom.limma on baseline625_625 with 2 samples per cond
            voom_b625_625_2_start = datetime.now()
            voom_b625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_2_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_b625_625_2_dir'))
            voom_b625_625_2end = datetime.now()
            logging.info("Elapsed time for voom.limma for baseline625_625_2_v" + str(i) + " " + str(voom_b625_625_2end - voom_b625_625_2_start))
            
#             #Run voom.limma on baseline4000_0 with 2 samples per cond
            voom_b4000_0_2_start = datetime.now()
            voom_b4000_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_2_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_b4000_0_2_dir'))
            voom_b4000_0_2end = datetime.now()
            logging.info("Elapsed time for voom.limma for baseline4000_0_2_v" + str(i) + " " + str(voom_b4000_0_2end - voom_b4000_0_2_start))
            
#             #Run voom.limma on baseline2000_2000 with 2 samples per cond
            voom_b2000_2000_2_start = datetime.now()
            voom_b2000_2000_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_2_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_b2000_2000_2_dir'))
            voom_b2000_2000_2end = datetime.now()
            logging.info("Elapsed time for voom.limma for baseline2000_2000_2_v" + str(i) + " " + str(voom_b2000_2000_2end - voom_b2000_2000_2_start))
            
#             #Run voom.limma on poisson0_0 with 2 samples per cond
            voom_p0_0_2_start = datetime.now()
            voom_p0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_2_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_p0_0_2_dir'))
            voom_p0_0_2_end = datetime.now()
            logging.info("Elapsed time for voom.limma for poisson0_0_2_v" + str(i) + " " + str(voom_p0_0_2_end - voom_p0_0_2_start))
            
#             #Run voom.limma on poisson625_625 with 2 samples per cond
            voom_p625_625_2_start = datetime.now()
            voom_p625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_2_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_p625_625_2_dir'))
            voom_p625_625_2_end = datetime.now()
            logging.info("Elapsed time for voom.limma for poisson625_625_2_v" + str(i) + " " + str(voom_p625_625_2_end - voom_p625_625_2_start))
            
#             #Run voom.limma on single0_0 with 2 samples per cond
            voom_s0_0_2_start = datetime.now()
            voom_s0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_2_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_s0_0_2_dir'))
            voom_s0_0_2_end = datetime.now()
            logging.info("Elapsed time for voom.limma for single0_0_2_v" + str(i) + " " + str(voom_s0_0_2_end - voom_s0_0_2_start))
            
#             #Run voom.limma on single625_625 with 2 samples per cond
            voom_s625_625_2_start = datetime.now()
            voom_s625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_2_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_s625_625_2_dir'))
            voom_s625_625_2_end = datetime.now()
            logging.info("Elapsed time for voom.limma for single625_625_2_v" + str(i) + " " + str(voom_s625_625_2_end - voom_s625_625_2_start))
            
#             #Run voom.limma on random0_0 with 2 samples per cond
            voom_r0_0_2_start = datetime.now()
            voom_r0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_2_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_r0_0_2_dir'))
            voom_r0_0_2_end = datetime.now()
            logging.info("Elapsed time for voom.limma for random0_0_2_v" + str(i) + " " + str(voom_r0_0_2_end - voom_r0_0_2_start))
            
#             #Run voom.limma on random625_625 with 2 samples per cond
            voom_r625_625_2_start = datetime.now()
            voom_r625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_2_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_r625_625_2_dir'))
            voom_r625_625_2_end = datetime.now()
            logging.info("Elapsed time for voom.limma for random625_625_2_v" + str(i) + " " + str(voom_r625_625_2_end - voom_r625_625_2_start))


            #Run NOISeq on the synthetic datasets above
            
            #Run NOISeq on baseline0_0 with 2 samples per cond
            NOISeq_b0_0_2_start = datetime.now()
            NOISeq_b0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_2_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_b0_0_2_dir'))
            NOISeq_b0_0_2_end = datetime.now()
            logging.info("Elapsed time for NOISeq for baseline0_0_2_v" + str(i) + " " + str(NOISeq_b0_0_2_end - NOISeq_b0_0_2_start))
            
            #Run NOISeq on baseline1250_0 with 2 samples per cond
            NOISeq_b1250_0_2_start = datetime.now()
            NOISeq_b1250_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_2_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_b1250_0_2_dir'))
            NOISeq_b1250_0_2end = datetime.now()
            logging.info("Elapsed time for NOISeq for baseline1250_0_2_v" + str(i) + " " + str(NOISeq_b1250_0_2end - NOISeq_b1250_0_2_start))
            
            #Run NOISeq on baseline625_625 with 2 samples per cond
            NOISeq_b625_625_2_start = datetime.now()
            NOISeq_b625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_2_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_b625_625_2_dir'))
            NOISeq_b625_625_2end = datetime.now()
            logging.info("Elapsed time for NOISeq for baseline625_625_2_v" + str(i) + " " + str(NOISeq_b625_625_2end - NOISeq_b625_625_2_start))
            
            #Run NOISeq on baseline4000_0 with 2 samples per cond
            NOISeq_b4000_0_2_start = datetime.now()
            NOISeq_b4000_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_2_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_b4000_0_2_dir'))
            NOISeq_b4000_0_2end = datetime.now()
            logging.info("Elapsed time for NOISeq for baseline4000_0_2_v" + str(i) + " " + str(NOISeq_b4000_0_2end - NOISeq_b4000_0_2_start))
            
            #Run NOISeq on baseline2000_2000 with 2 samples per cond
            NOISeq_b2000_2000_2_start = datetime.now()
            NOISeq_b2000_2000_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_2_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_b2000_2000_2_dir'))
            NOISeq_b2000_2000_2end = datetime.now()
            logging.info("Elapsed time for NOISeq for baseline2000_2000_2_v" + str(i) + " " + str(NOISeq_b2000_2000_2end - NOISeq_b2000_2000_2_start))
            
            #Run NOISeq on poisson0_0 with 2 samples per cond
            NOISeq_p0_0_2_start = datetime.now()
            NOISeq_p0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_2_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_p0_0_2_dir'))
            NOISeq_p0_0_2_end = datetime.now()
            logging.info("Elapsed time for NOISeq for poisson0_0_2_v" + str(i) + " " + str(NOISeq_p0_0_2_end - NOISeq_p0_0_2_start))
            
            #Run NOISeq on poisson625_625 with 2 samples per cond
            NOISeq_p625_625_2_start = datetime.now()
            NOISeq_p625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_2_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_p625_625_2_dir'))
            NOISeq_p625_625_2_end = datetime.now()
            logging.info("Elapsed time for NOISeq for poisson625_625_2_v" + str(i) + " " + str(NOISeq_p625_625_2_end - NOISeq_p625_625_2_start))
            
            #Run NOISeq on single0_0 with 2 samples per cond
            NOISeq_s0_0_2_start = datetime.now()
            NOISeq_s0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_2_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_s0_0_2_dir'))
            NOISeq_s0_0_2_end = datetime.now()
            logging.info("Elapsed time for NOISeq for single0_0_2_v" + str(i) + " " + str(NOISeq_s0_0_2_end - NOISeq_s0_0_2_start))
            
            #Run NOISeq on single625_625 with 2 samples per cond
            NOISeq_s625_625_2_start = datetime.now()
            NOISeq_s625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_2_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_s625_625_2_dir'))
            NOISeq_s625_625_2_end = datetime.now()
            logging.info("Elapsed time for NOISeq for single625_625_2_v" + str(i) + " " + str(NOISeq_s625_625_2_end - NOISeq_s625_625_2_start))
            
            #Run NOISeq on random0_0 with 2 samples per cond
            NOISeq_r0_0_2_start = datetime.now()
            NOISeq_r0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_2_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_r0_0_2_dir'))
            NOISeq_r0_0_2_end = datetime.now()
            logging.info("Elapsed time for NOISeq for random0_0_2_v" + str(i) + " " + str(NOISeq_r0_0_2_end - NOISeq_r0_0_2_start))
            
            #Run NOISeq on random625_625 with 2 samples per cond
            NOISeq_r625_625_2_start = datetime.now()
            NOISeq_r625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_2_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_r625_625_2_dir'))
            NOISeq_r625_625_2_end = datetime.now()
            logging.info("Elapsed time for NOISeq for random625_625_2_v" + str(i) + " " + str(NOISeq_r625_625_2_end - NOISeq_r625_625_2_start))


            #Run ttest on the synthetic datasets above
            
            #Run ttest on baseline0_0 with 2 samples per cond
            ttest_b0_0_2_start = datetime.now()
            ttest_b0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_2_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_b0_0_2_dir'))
            ttest_b0_0_2_end = datetime.now()
            logging.info("Elapsed time for ttest for baseline0_0_2_v" + str(i) + " " + str(ttest_b0_0_2_end - ttest_b0_0_2_start))
            
            #Run ttest on baseline1250_0 with 2 samples per cond
            ttest_b1250_0_2_start = datetime.now()
            ttest_b1250_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_2_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_b1250_0_2_dir'))
            ttest_b1250_0_2end = datetime.now()
            logging.info("Elapsed time for ttest for baseline1250_0_2_v" + str(i) + " " + str(ttest_b1250_0_2end - ttest_b1250_0_2_start))
            
            #Run ttest on baseline625_625 with 2 samples per cond
            ttest_b625_625_2_start = datetime.now()
            ttest_b625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_2_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_b625_625_2_dir'))
            ttest_b625_625_2end = datetime.now()
            logging.info("Elapsed time for ttest for baseline625_625_2_v" + str(i) + " " + str(ttest_b625_625_2end - ttest_b625_625_2_start))
            
            #Run ttest on baseline4000_0 with 2 samples per cond
            ttest_b4000_0_2_start = datetime.now()
            ttest_b4000_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_2_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_b4000_0_2_dir'))
            ttest_b4000_0_2end = datetime.now()
            logging.info("Elapsed time for ttest for baseline4000_0_2_v" + str(i) + " " + str(ttest_b4000_0_2end - ttest_b4000_0_2_start))
            
            #Run ttest on baseline2000_2000 with 2 samples per cond
            ttest_b2000_2000_2_start = datetime.now()
            ttest_b2000_2000_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_2_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_b2000_2000_2_dir'))
            ttest_b2000_2000_2end = datetime.now()
            logging.info("Elapsed time for ttest for baseline2000_2000_2_v" + str(i) + " " + str(ttest_b2000_2000_2end - ttest_b2000_2000_2_start))
            
            #Run ttest on poisson0_0 with 2 samples per cond
            ttest_p0_0_2_start = datetime.now()
            ttest_p0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_2_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_p0_0_2_dir'))
            ttest_p0_0_2_end = datetime.now()
            logging.info("Elapsed time for ttest for poisson0_0_2_v" + str(i) + " " + str(ttest_p0_0_2_end - ttest_p0_0_2_start))
            
            #Run ttest on poisson625_625 with 2 samples per cond
            ttest_p625_625_2_start = datetime.now()
            ttest_p625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_2_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_p625_625_2_dir'))
            ttest_p625_625_2_end = datetime.now()
            logging.info("Elapsed time for ttest for poisson625_625_2_v" + str(i) + " " + str(ttest_p625_625_2_end - ttest_p625_625_2_start))
            
            #Run ttest on single0_0 with 2 samples per cond
            ttest_s0_0_2_start = datetime.now()
            ttest_s0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_2_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_s0_0_2_dir'))
            ttest_s0_0_2_end = datetime.now()
            logging.info("Elapsed time for ttest for single0_0_2_v" + str(i) + " " + str(ttest_s0_0_2_end - ttest_s0_0_2_start))
            
            #Run ttest on single625_625 with 2 samples per cond
            ttest_s625_625_2_start = datetime.now()
            ttest_s625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_2_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_s625_625_2_dir'))
            ttest_s625_625_2_end = datetime.now()
            logging.info("Elapsed time for ttest for single625_625_2_v" + str(i) + " " + str(ttest_s625_625_2_end - ttest_s625_625_2_start))
            
            #Run ttest on random0_0 with 2 samples per cond
            ttest_r0_0_2_start = datetime.now()
            ttest_r0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_2_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_r0_0_2_dir'))
            ttest_r0_0_2_end = datetime.now()
            logging.info("Elapsed time for ttest for random0_0_2_v" + str(i) + " " + str(ttest_r0_0_2_end - ttest_r0_0_2_start))
            
            #Run ttest on random625_625 with 2 samples per cond
            ttest_r625_625_2_start = datetime.now()
            ttest_r625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_2_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_r625_625_2_dir'))
            ttest_r625_625_2_end = datetime.now()
            logging.info("Elapsed time for ttest for random625_625_2_v" + str(i) + " " + str(ttest_r625_625_2_end - ttest_r625_625_2_start))


            #Run PoissonSeq on the synthetic datasets above
            
            #Run PoissonSeq on baseline0_0 with 2 samples per cond
#             PoissonSeq_b0_0_2_start = datetime.now()
#             PoissonSeq_b0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_2_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_b0_0_2_dir'))
#             PoissonSeq_b0_0_2_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for baseline0_0_2_v" + str(i) + " " + str(PoissonSeq_b0_0_2_end - PoissonSeq_b0_0_2_start))
            
#             #Run PoissonSeq on baseline1250_0 with 2 samples per cond
#             PoissonSeq_b1250_0_2_start = datetime.now()
#             PoissonSeq_b1250_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_2_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_b1250_0_2_dir'))
#             PoissonSeq_b1250_0_2end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for baseline1250_0_2_v" + str(i) + " " + str(PoissonSeq_b1250_0_2end - PoissonSeq_b1250_0_2_start))
            
#             #Run PoissonSeq on baseline625_625 with 2 samples per cond
#             PoissonSeq_b625_625_2_start = datetime.now()
#             PoissonSeq_b625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_2_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_b625_625_2_dir'))
#             PoissonSeq_b625_625_2end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for baseline625_625_2_v" + str(i) + " " + str(PoissonSeq_b625_625_2end - PoissonSeq_b625_625_2_start))
            
#             #Run PoissonSeq on baseline4000_0 with 2 samples per cond
#             PoissonSeq_b4000_0_2_start = datetime.now()
#             PoissonSeq_b4000_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_2_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_b4000_0_2_dir'))
#             PoissonSeq_b4000_0_2end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for baseline4000_0_2_v" + str(i) + " " + str(PoissonSeq_b4000_0_2end - PoissonSeq_b4000_0_2_start))
            
#             #Run PoissonSeq on baseline2000_2000 with 2 samples per cond
#             PoissonSeq_b2000_2000_2_start = datetime.now()
#             PoissonSeq_b2000_2000_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_2_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_b2000_2000_5_dir'))
#             PoissonSeq_b2000_2000_2end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for baseline2000_2000_2_v" + str(i) + " " + str(PoissonSeq_b2000_2000_2end - PoissonSeq_b2000_2000_2_start))
            
#             #Run PoissonSeq on poisson0_0 with 2 samples per cond
#             PoissonSeq_p0_0_2_start = datetime.now()
#             PoissonSeq_p0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_2_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_p0_0_2_dir'))
#             PoissonSeq_p0_0_2_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for poisson0_0_2_v" + str(i) + " " + str(PoissonSeq_p0_0_2_end - PoissonSeq_p0_0_2_start))
            
#             #Run PoissonSeq on poisson625_625 with 2 samples per cond
#             PoissonSeq_p625_625_2_start = datetime.now()
#             PoissonSeq_p625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_2_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_p625_625_2_dir'))
#             PoissonSeq_p625_625_2_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for poisson625_625_2_v" + str(i) + " " + str(PoissonSeq_p625_625_2_end - PoissonSeq_p625_625_2_start))
            
#             #Run PoissonSeq on single0_0 with 2 samples per cond
#             PoissonSeq_s0_0_2_start = datetime.now()
#             PoissonSeq_s0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_2_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_s0_0_2_dir'))
#             PoissonSeq_s0_0_2_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for single0_0_2_v" + str(i) + " " + str(PoissonSeq_s0_0_2_end - PoissonSeq_s0_0_2_start))
            
#             #Run PoissonSeq on single625_625 with 2 samples per cond
#             PoissonSeq_s625_625_2_start = datetime.now()
#             PoissonSeq_s625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_2_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_s625_625_2_dir'))
#             PoissonSeq_s625_625_2_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for single625_625_2_v" + str(i) + " " + str(PoissonSeq_s625_625_2_end - PoissonSeq_s625_625_2_start))
            
#             #Run PoissonSeq on random0_0 with 2 samples per cond
#             PoissonSeq_r0_0_2_start = datetime.now()
#             PoissonSeq_r0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_2_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_r0_0_2_dir'))
#             PoissonSeq_r0_0_2_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for random0_0_2_v" + str(i) + " " + str(PoissonSeq_r0_0_2_end - PoissonSeq_r0_0_2_start))
            
#             #Run PoissonSeq on random625_625 with 2 samples per cond
#             PoissonSeq_r625_625_2_start = datetime.now()
#             PoissonSeq_r625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_2_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_r625_625_2_dir'))
#             PoissonSeq_r625_625_2_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for random625_625_2_v" + str(i) + " " + str(PoissonSeq_r625_625_2_end - PoissonSeq_r625_625_2_start))



#             #Run ABSSeq on the synthetic datasets above
            
#             #Run ABSSeq on baseline0_0 with 2 samples per cond
#             ABSSeq_b0_0_2_start = datetime.now()
#             ABSSeq_b0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_2_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_b0_0_2_dir'))
#             ABSSeq_b0_0_2_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for baseline0_0_2_v" + str(i) + " " + str(ABSSeq_b0_0_2_end - ABSSeq_b0_0_2_start))
            
#             #Run ABSSeq on baseline1250_0 with 2 samples per cond
#             ABSSeq_b1250_0_2_start = datetime.now()
#             ABSSeq_b1250_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_2_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_b1250_0_2_dir'))
#             ABSSeq_b1250_0_2end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for baseline1250_0_2_v" + str(i) + " " + str(ABSSeq_b1250_0_2end - ABSSeq_b1250_0_2_start))
            
#             #Run ABSSeq on baseline625_625 with 2 samples per cond
#             ABSSeq_b625_625_2_start = datetime.now()
#             ABSSeq_b625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_2_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_b625_625_2_dir'))
#             ABSSeq_b625_625_2end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for baseline625_625_2_v" + str(i) + " " + str(ABSSeq_b625_625_2end - ABSSeq_b625_625_2_start))
            
#             #Run ABSSeq on baseline4000_0 with 2 samples per cond
#             ABSSeq_b4000_0_2_start = datetime.now()
#             ABSSeq_b4000_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_2_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_b4000_0_2_dir'))
#             ABSSeq_b4000_0_2end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for baseline4000_0_2_v" + str(i) + " " + str(ABSSeq_b4000_0_2end - ABSSeq_b4000_0_2_start))
            
#             #Run ABSSeq on baseline2000_2000 with 2 samples per cond
#             ABSSeq_b2000_2000_2_start = datetime.now()
#             ABSSeq_b2000_2000_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_2_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_b2000_2000_2_dir'))
#             ABSSeq_b2000_2000_2end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for baseline2000_2000_2_v" + str(i) + " " + str(ABSSeq_b2000_2000_2end - ABSSeq_b2000_2000_2_start))
            
#             #Run ABSSeq on poisson0_0 with 2 samples per cond
#             ABSSeq_p0_0_2_start = datetime.now()
#             ABSSeq_p0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_2_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_p0_0_2_dir'))
#             ABSSeq_p0_0_2_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for poisson0_0_2_v" + str(i) + " " + str(ABSSeq_p0_0_2_end - ABSSeq_p0_0_2_start))
            
#             #Run ABSSeq on poisson625_625 with 2 samples per cond
#             ABSSeq_p625_625_2_start = datetime.now()
#             ABSSeq_p625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_2_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_p625_625_2_dir'))
#             ABSSeq_p625_625_2_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for poisson625_625_2_v" + str(i) + " " + str(ABSSeq_p625_625_2_end - ABSSeq_p625_625_2_start))
            
#             #Run ABSSeq on single0_0 with 2 samples per cond
#             ABSSeq_s0_0_2_start = datetime.now()
#             ABSSeq_s0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_2_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_s0_0_2_dir'))
#             ABSSeq_s0_0_2_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for single0_0_2_v" + str(i) + " " + str(ABSSeq_s0_0_2_end - ABSSeq_s0_0_2_start))
            
#             #Run ABSSeq on single625_625 with 2 samples per cond
#             ABSSeq_s625_625_2_start = datetime.now()
#             ABSSeq_s625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_2_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_s625_625_2_dir'))
#             ABSSeq_s625_625_2_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for single625_625_2_v" + str(i) + " " + str(ABSSeq_s625_625_2_end - ABSSeq_s625_625_2_start))
            
#             #Run ABSSeq on random0_0 with 2 samples per cond
#             ABSSeq_r0_0_2_start = datetime.now()
#             ABSSeq_r0_0_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_2_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_r0_0_2_dir'))
#             ABSSeq_r0_0_2_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for random0_0_2_v" + str(i) + " " + str(ABSSeq_r0_0_2_end - ABSSeq_r0_0_2_start))
            
#             #Run ABSSeq on random625_625 with 2 samples per cond
#             ABSSeq_r625_625_2_start = datetime.now()
#             ABSSeq_r625_625_2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_2_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_r625_625_2_dir'))
#             ABSSeq_r625_625_2_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for random625_625_2_v" + str(i) + " " + str(ABSSeq_r625_625_2_end - ABSSeq_r625_625_2_start))
            

            #Run DESeq2 on the synthetic datasets above
            
            #Run DESeq2 on baseline0_0 with 5 samples per cond
#             deseq2_b0_0_5_start = datetime.now()
#             deseq2_b0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_5_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_b0_0_5_dir'))
#             deseq2_b0_0_5_end = datetime.now()
#             logging.info("Elapsed time for DESeq2 for baseline0_0_5_v" + str(i) + " " + str(deseq2_b0_0_5_end - deseq2_b0_0_5_start))
            
            #Run DESeq2 on baseline1250_0 with 5 samples per cond
#             deseq2_b1250_0_5_start = datetime.now()
#             deseq2_b1250_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_5_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_b1250_0_5_dir'))
#             deseq2_b1250_0_5end = datetime.now()
#             logging.info("Elapsed time for DESeq2 for baseline1250_0_5_v" + str(i) + " " + str(deseq2_b1250_0_5end - deseq2_b1250_0_5_start))
            
            #Run DESeq2 on baseline625_625 with 5 samples per cond
#             deseq2_b625_625_5_start = datetime.now()
#             deseq2_b625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_5_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_b625_625_5_dir'))
#             deseq2_b625_625_5end = datetime.now()
#             logging.info("Elapsed time for DESeq2 for baseline625_625_5_v" + str(i) + " " + str(deseq2_b625_625_5end - deseq2_b625_625_5_start))
            
            #Run DESeq2 on baseline4000_0 with 5 samples per cond
#             deseq2_b4000_0_5_start = datetime.now()
#             deseq2_b4000_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_5_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_b4000_0_5_dir'))
#             deseq2_b4000_0_5end = datetime.now()
#             logging.info("Elapsed time for DESeq2 for baseline4000_0_5_v" + str(i) + " " + str(deseq2_b4000_0_5end - deseq2_b4000_0_5_start))
            
            #Run DESeq2 on baseline2000_2000 with 5 samples per cond
#             deseq2_b2000_2000_5_start = datetime.now()
#             deseq2_b2000_2000_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_5_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_b2000_2000_5_dir'))
#             deseq2_b2000_2000_5end = datetime.now()
#             logging.info("Elapsed time for DESeq2 for baseline2000_2000_5_v" + str(i) + " " + str(deseq2_b2000_2000_5end - deseq2_b2000_2000_5_start))
            
            #Run DESeq2 on poisson0_0 with 5 samples per cond
#             deseq2_p0_0_5_start = datetime.now()
#             deseq2_p0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_5_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_p0_0_5_dir'))
#             deseq2_p0_0_5_end = datetime.now()
#             logging.info("Elapsed time for DESeq2 for poisson0_0_5_v" + str(i) + " " + str(deseq2_p0_0_5_end - deseq2_p0_0_5_start))
            
            #Run DESeq2 on poisson625_625 with 5 samples per cond
#             deseq2_p625_625_5_start = datetime.now()
#             deseq2_p625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_5_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_p625_625_5_dir'))
#             deseq2_p625_625_5_end = datetime.now()
#             logging.info("Elapsed time for DESeq2 for poisson625_625_5_v" + str(i) + " " + str(deseq2_p625_625_5_end - deseq2_p625_625_5_start))
            
            #Run DESeq2 on single0_0 with 5 samples per cond
#             deseq2_s0_0_5_start = datetime.now()
#             deseq2_s0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_5_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_s0_0_5_dir'))
#             deseq2_s0_0_5_end = datetime.now()
#             logging.info("Elapsed time for DESeq2 for single0_0_5_v" + str(i) + " " + str(deseq2_s0_0_5_end - deseq2_s0_0_5_start))
            
            #Run DESeq2 on single625_625 with 5 samples per cond
#             deseq2_s625_625_5_start = datetime.now()
#             deseq2_s625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_5_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_s625_625_5_dir'))
#             deseq2_s625_625_5_end = datetime.now()
#             logging.info("Elapsed time for DESeq2 for single625_625_5_v" + str(i) + " " + str(deseq2_s625_625_5_end - deseq2_s625_625_5_start))
            
            #Run DESeq2 on random0_0 with 5 samples per cond
#             deseq2_r0_0_5_start = datetime.now()
#             deseq2_r0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_5_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_r0_0_5_dir'))
#             deseq2_r0_0_5_end = datetime.now()
#             logging.info("Elapsed time for DESeq2 for random0_0_5_v" + str(i) + " " + str(deseq2_r0_0_5_end - deseq2_r0_0_5_start))
            
            #Run DESeq2 on random625_625 with 5 samples per cond
#             deseq2_r625_625_5_start = datetime.now()
#             deseq2_r625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_5_v' + str(i)), analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'), analysis_cfg.get('DESeq2_r625_625_5_dir'))
#             deseq2_r625_625_5_end = datetime.now()
#             logging.info("Elapsed time for DESeq2 for random625_625_5_v" + str(i) + " " + str(deseq2_r625_625_5_end - deseq2_r625_625_5_start))
            
            #Run edgeR on the synthetic datasets above
            
            #Run edgeR on baseline0_0 with 5 samples per cond
#             edgeR_b0_0_5_start = datetime.now()
#             edgeR_b0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_5_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_b0_0_5_dir'))
#             edgeR_b0_0_5_end = datetime.now()
#             logging.info("Elapsed time for edgeR for baseline0_0_5_v" + str(i) + " " + str(edgeR_b0_0_5_end - edgeR_b0_0_5_start))
            
#             #Run edgeR on baseline1250_0 with 5 samples per cond
#             edgeR_b1250_0_5_start = datetime.now()
#             edgeR_b1250_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_5_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_b1250_0_5_dir'))
#             edgeR_b1250_0_5end = datetime.now()
#             logging.info("Elapsed time for edgeR for baseline1250_0_5_v" + str(i) + " " + str(edgeR_b1250_0_5end - edgeR_b1250_0_5_start))
            
#             #Run edgeR on baseline625_625 with 5 samples per cond
#             edgeR_b625_625_5_start = datetime.now()
#             edgeR_b625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_5_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_b625_625_5_dir'))
#             edgeR_b625_625_5end = datetime.now()
#             logging.info("Elapsed time for edgeR for baseline625_625_5_v" + str(i) + " " + str(edgeR_b625_625_5end - edgeR_b625_625_5_start))
            
#             #Run edgeR on baseline4000_0 with 5 samples per cond
#             edgeR_b4000_0_5_start = datetime.now()
#             edgeR_b4000_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_5_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_b4000_0_5_dir'))
#             edgeR_b4000_0_5end = datetime.now()
#             logging.info("Elapsed time for edgeR for baseline4000_0_5_v" + str(i) + " " + str(edgeR_b4000_0_5end - edgeR_b4000_0_5_start))
            
#             #Run edgeR on baseline2000_2000 with 5 samples per cond
#             edgeR_b2000_2000_5_start = datetime.now()
#             edgeR_b2000_2000_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_5_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_b2000_2000_5_dir'))
#             edgeR_b2000_2000_5end = datetime.now()
#             logging.info("Elapsed time for edgeR for baseline2000_2000_5_v" + str(i) + " " + str(edgeR_b2000_2000_5end - edgeR_b2000_2000_5_start))
            
#             #Run edgeR on poisson0_0 with 5 samples per cond
#             edgeR_p0_0_5_start = datetime.now()
#             edgeR_p0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_5_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_p0_0_5_dir'))
#             edgeR_p0_0_5_end = datetime.now()
#             logging.info("Elapsed time for edgeR for poisson0_0_5_v" + str(i) + " " + str(edgeR_p0_0_5_end - edgeR_p0_0_5_start))
            
#             #Run edgeR on poisson625_625 with 5 samples per cond
#             edgeR_p625_625_5_start = datetime.now()
#             edgeR_p625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_5_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_p625_625_5_dir'))
#             edgeR_p625_625_5_end = datetime.now()
#             logging.info("Elapsed time for edgeR for poisson625_625_5_v" + str(i) + " " + str(edgeR_p625_625_5_end - edgeR_p625_625_5_start))
            
#             #Run edgeR on single0_0 with 5 samples per cond
#             edgeR_s0_0_5_start = datetime.now()
#             edgeR_s0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_5_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_s0_0_5_dir'))
#             edgeR_s0_0_5_end = datetime.now()
#             logging.info("Elapsed time for edgeR for single0_0_5_v" + str(i) + " " + str(edgeR_s0_0_5_end - edgeR_s0_0_5_start))
            
#             #Run edgeR on single625_625 with 5 samples per cond
#             edgeR_s625_625_5_start = datetime.now()
#             edgeR_s625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_5_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_s625_625_5_dir'))
#             edgeR_s625_625_5_end = datetime.now()
#             logging.info("Elapsed time for edgeR for single625_625_5_v" + str(i) + " " + str(edgeR_s625_625_5_end - edgeR_s625_625_5_start))
            
#             #Run edgeR on random0_0 with 5 samples per cond
#             edgeR_r0_0_5_start = datetime.now()
#             edgeR_r0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_5_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_r0_0_5_dir'))
#             edgeR_r0_0_5_end = datetime.now()
#             logging.info("Elapsed time for edgeR for random0_0_5_v" + str(i) + " " + str(edgeR_r0_0_5_end - edgeR_r0_0_5_start))
            
#             #Run edgeR on random625_625 with 5 samples per cond
#             edgeR_r625_625_5_start = datetime.now()
#             edgeR_r625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_5_v' + str(i)), analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'), analysis_cfg.get('edgeR_r625_625_5_dir'))
#             edgeR_r625_625_5_end = datetime.now()
#             logging.info("Elapsed time for edgeR for random625_625_5_v" + str(i) + " " + str(edgeR_r625_625_5_end - edgeR_r625_625_5_start))


            #Run voom.limma on the synthetic datasets above
            
            #Run voom.limma on baseline0_0 with 5 samples per cond
#             voom_b0_0_5_start = datetime.now()
#             voom_b0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_5_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_b0_0_5_dir'))
#             voom_b0_0_5_end = datetime.now()
#             logging.info("Elapsed time for voom.limma for baseline0_0_5_v" + str(i) + " " + str(voom_b0_0_5_end - voom_b0_0_5_start))
            
#             #Run voom.limma on baseline1250_0 with 5 samples per cond
#             voom_b1250_0_5_start = datetime.now()
#             voom_b1250_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_5_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_b1250_0_5_dir'))
#             voom_b1250_0_5end = datetime.now()
#             logging.info("Elapsed time for voom.limma for baseline1250_0_5_v" + str(i) + " " + str(voom_b1250_0_5end - voom_b1250_0_5_start))
            
#             #Run voom.limma on baseline625_625 with 5 samples per cond
#             voom_b625_625_5_start = datetime.now()
#             voom_b625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_5_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_b625_625_5_dir'))
#             voom_b625_625_5end = datetime.now()
#             logging.info("Elapsed time for voom.limma for baseline625_625_5_v" + str(i) + " " + str(voom_b625_625_5end - voom_b625_625_5_start))
            
#             #Run voom.limma on baseline4000_0 with 5 samples per cond
#             voom_b4000_0_5_start = datetime.now()
#             voom_b4000_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_5_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_b4000_0_5_dir'))
#             voom_b4000_0_5end = datetime.now()
#             logging.info("Elapsed time for voom.limma for baseline4000_0_5_v" + str(i) + " " + str(voom_b4000_0_5end - voom_b4000_0_5_start))
            
#             #Run voom.limma on baseline2000_2000 with 5 samples per cond
#             voom_b2000_2000_5_start = datetime.now()
#             voom_b2000_2000_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_5_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_b2000_2000_5_dir'))
#             voom_b2000_2000_5end = datetime.now()
#             logging.info("Elapsed time for voom.limma for baseline2000_2000_5_v" + str(i) + " " + str(voom_b2000_2000_5end - voom_b2000_2000_5_start))
            
#             #Run voom.limma on poisson0_0 with 5 samples per cond
#             voom_p0_0_5_start = datetime.now()
#             voom_p0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_5_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_p0_0_5_dir'))
#             voom_p0_0_5_end = datetime.now()
#             logging.info("Elapsed time for voom.limma for poisson0_0_5_v" + str(i) + " " + str(voom_p0_0_5_end - voom_p0_0_5_start))
            
#             #Run voom.limma on poisson625_625 with 5 samples per cond
#             voom_p625_625_5_start = datetime.now()
#             voom_p625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_5_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_p625_625_5_dir'))
#             voom_p625_625_5_end = datetime.now()
#             logging.info("Elapsed time for voom.limma for poisson625_625_5_v" + str(i) + " " + str(voom_p625_625_5_end - voom_p625_625_5_start))
            
#             #Run voom.limma on single0_0 with 5 samples per cond
#             voom_s0_0_5_start = datetime.now()
#             voom_s0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_5_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_s0_0_5_dir'))
#             voom_s0_0_5_end = datetime.now()
#             logging.info("Elapsed time for voom.limma for single0_0_5_v" + str(i) + " " + str(voom_s0_0_5_end - voom_s0_0_5_start))
            
#             #Run voom.limma on single625_625 with 5 samples per cond
#             voom_s625_625_5_start = datetime.now()
#             voom_s625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_5_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_s625_625_5_dir'))
#             voom_s625_625_5_end = datetime.now()
#             logging.info("Elapsed time for voom.limma for single625_625_5_v" + str(i) + " " + str(voom_s625_625_5_end - voom_s625_625_5_start))
            
#             #Run voom.limma on random0_0 with 5 samples per cond
#             voom_r0_0_5_start = datetime.now()
#             voom_r0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_5_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_r0_0_5_dir'))
#             voom_r0_0_5_end = datetime.now()
#             logging.info("Elapsed time for voom.limma for random0_0_5_v" + str(i) + " " + str(voom_r0_0_5_end - voom_r0_0_5_start))
            
#             #Run voom.limma on random625_625 with 5 samples per cond
#             voom_r625_625_5_start = datetime.now()
#             voom_r625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_5_v' + str(i)), analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'), analysis_cfg.get('voom.limma_r625_625_5_dir'))
#             voom_r625_625_5_end = datetime.now()
#             logging.info("Elapsed time for voom.limma for random625_625_5_v" + str(i) + " " + str(voom_r625_625_5_end - voom_r625_625_5_start))


            #Run NOISeq on the synthetic datasets above
            
            #Run NOISeq on baseline0_0 with 5 samples per cond
#             NOISeq_b0_0_5_start = datetime.now()
#             NOISeq_b0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_5_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_b0_0_5_dir'))
#             NOISeq_b0_0_5_end = datetime.now()
#             logging.info("Elapsed time for NOISeq for baseline0_0_5_v" + str(i) + " " + str(NOISeq_b0_0_5_end - NOISeq_b0_0_5_start))
            
#             #Run NOISeq on baseline1250_0 with 5 samples per cond
#             NOISeq_b1250_0_5_start = datetime.now()
#             NOISeq_b1250_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_5_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_b1250_0_5_dir'))
#             NOISeq_b1250_0_5end = datetime.now()
#             logging.info("Elapsed time for NOISeq for baseline1250_0_5_v" + str(i) + " " + str(NOISeq_b1250_0_5end - NOISeq_b1250_0_5_start))
            
#             #Run NOISeq on baseline625_625 with 5 samples per cond
#             NOISeq_b625_625_5_start = datetime.now()
#             NOISeq_b625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_5_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_b625_625_5_dir'))
#             NOISeq_b625_625_5end = datetime.now()
#             logging.info("Elapsed time for NOISeq for baseline625_625_5_v" + str(i) + " " + str(NOISeq_b625_625_5end - NOISeq_b625_625_5_start))
            
#             #Run NOISeq on baseline4000_0 with 5 samples per cond
#             NOISeq_b4000_0_5_start = datetime.now()
#             NOISeq_b4000_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_5_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_b4000_0_5_dir'))
#             NOISeq_b4000_0_5end = datetime.now()
#             logging.info("Elapsed time for NOISeq for baseline4000_0_5_v" + str(i) + " " + str(NOISeq_b4000_0_5end - NOISeq_b4000_0_5_start))
            
#             #Run NOISeq on baseline2000_2000 with 5 samples per cond
#             NOISeq_b2000_2000_5_start = datetime.now()
#             NOISeq_b2000_2000_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_5_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_b2000_2000_5_dir'))
#             NOISeq_b2000_2000_5end = datetime.now()
#             logging.info("Elapsed time for NOISeq for baseline2000_2000_5_v" + str(i) + " " + str(NOISeq_b2000_2000_5end - NOISeq_b2000_2000_5_start))
            
#             #Run NOISeq on poisson0_0 with 5 samples per cond
#             NOISeq_p0_0_5_start = datetime.now()
#             NOISeq_p0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_5_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_p0_0_5_dir'))
#             NOISeq_p0_0_5_end = datetime.now()
#             logging.info("Elapsed time for NOISeq for poisson0_0_5_v" + str(i) + " " + str(NOISeq_p0_0_5_end - NOISeq_p0_0_5_start))
            
#             #Run NOISeq on poisson625_625 with 5 samples per cond
#             NOISeq_p625_625_5_start = datetime.now()
#             NOISeq_p625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_5_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_p625_625_5_dir'))
#             NOISeq_p625_625_5_end = datetime.now()
#             logging.info("Elapsed time for NOISeq for poisson625_625_5_v" + str(i) + " " + str(NOISeq_p625_625_5_end - NOISeq_p625_625_5_start))
            
#             #Run NOISeq on single0_0 with 5 samples per cond
#             NOISeq_s0_0_5_start = datetime.now()
#             NOISeq_s0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_5_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_s0_0_5_dir'))
#             NOISeq_s0_0_5_end = datetime.now()
#             logging.info("Elapsed time for NOISeq for single0_0_5_v" + str(i) + " " + str(NOISeq_s0_0_5_end - NOISeq_s0_0_5_start))
            
#             #Run NOISeq on single625_625 with 5 samples per cond
#             NOISeq_s625_625_5_start = datetime.now()
#             NOISeq_s625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_5_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_s625_625_5_dir'))
#             NOISeq_s625_625_5_end = datetime.now()
#             logging.info("Elapsed time for NOISeq for single625_625_5_v" + str(i) + " " + str(NOISeq_s625_625_5_end - NOISeq_s625_625_5_start))
            
#             #Run NOISeq on random0_0 with 5 samples per cond
#             NOISeq_r0_0_5_start = datetime.now()
#             NOISeq_r0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_5_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_r0_0_5_dir'))
#             NOISeq_r0_0_5_end = datetime.now()
#             logging.info("Elapsed time for NOISeq for random0_0_5_v" + str(i) + " " + str(NOISeq_r0_0_5_end - NOISeq_r0_0_5_start))
            
#             #Run NOISeq on random625_625 with 5 samples per cond
#             NOISeq_r625_625_5_start = datetime.now()
#             NOISeq_r625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_5_v' + str(i)), analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'), analysis_cfg.get('NOISeq_r625_625_5_dir'))
#             NOISeq_r625_625_5_end = datetime.now()
#             logging.info("Elapsed time for NOISeq for random625_625_5_v" + str(i) + " " + str(NOISeq_r625_625_5_end - NOISeq_r625_625_5_start))


            #Run ttest on the synthetic datasets above
            
            #Run ttest on baseline0_0 with 5 samples per cond
#             ttest_b0_0_5_start = datetime.now()
#             ttest_b0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_5_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_b0_0_5_dir'))
#             ttest_b0_0_5_end = datetime.now()
#             logging.info("Elapsed time for ttest for baseline0_0_5_v" + str(i) + " " + str(ttest_b0_0_5_end - ttest_b0_0_5_start))
            
#             #Run ttest on baseline1250_0 with 5 samples per cond
#             ttest_b1250_0_5_start = datetime.now()
#             ttest_b1250_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_5_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_b1250_0_5_dir'))
#             ttest_b1250_0_5end = datetime.now()
#             logging.info("Elapsed time for ttest for baseline1250_0_5_v" + str(i) + " " + str(ttest_b1250_0_5end - ttest_b1250_0_5_start))
            
#             #Run ttest on baseline625_625 with 5 samples per cond
#             ttest_b625_625_5_start = datetime.now()
#             ttest_b625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_5_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_b625_625_5_dir'))
#             ttest_b625_625_5end = datetime.now()
#             logging.info("Elapsed time for ttest for baseline625_625_5_v" + str(i) + " " + str(ttest_b625_625_5end - ttest_b625_625_5_start))
            
#             #Run ttest on baseline4000_0 with 5 samples per cond
#             ttest_b4000_0_5_start = datetime.now()
#             ttest_b4000_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_5_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_b4000_0_5_dir'))
#             ttest_b4000_0_5end = datetime.now()
#             logging.info("Elapsed time for ttest for baseline4000_0_5_v" + str(i) + " " + str(ttest_b4000_0_5end - ttest_b4000_0_5_start))
            
#             #Run ttest on baseline2000_2000 with 5 samples per cond
#             ttest_b2000_2000_5_start = datetime.now()
#             ttest_b2000_2000_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_5_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_b2000_2000_5_dir'))
#             ttest_b2000_2000_5end = datetime.now()
#             logging.info("Elapsed time for ttest for baseline2000_2000_5_v" + str(i) + " " + str(ttest_b2000_2000_5end - ttest_b2000_2000_5_start))
            
#             #Run ttest on poisson0_0 with 5 samples per cond
#             ttest_p0_0_5_start = datetime.now()
#             ttest_p0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_5_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_p0_0_5_dir'))
#             ttest_p0_0_5_end = datetime.now()
#             logging.info("Elapsed time for ttest for poisson0_0_5_v" + str(i) + " " + str(ttest_p0_0_5_end - ttest_p0_0_5_start))
            
#             #Run ttest on poisson625_625 with 5 samples per cond
#             ttest_p625_625_5_start = datetime.now()
#             ttest_p625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_5_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_p625_625_5_dir'))
#             ttest_p625_625_5_end = datetime.now()
#             logging.info("Elapsed time for ttest for poisson625_625_5_v" + str(i) + " " + str(ttest_p625_625_5_end - ttest_p625_625_5_start))
            
#             #Run ttest on single0_0 with 5 samples per cond
#             ttest_s0_0_5_start = datetime.now()
#             ttest_s0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_5_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_s0_0_5_dir'))
#             ttest_s0_0_5_end = datetime.now()
#             logging.info("Elapsed time for ttest for single0_0_5_v" + str(i) + " " + str(ttest_s0_0_5_end - ttest_s0_0_5_start))
            
#             #Run ttest on single625_625 with 5 samples per cond
#             ttest_s625_625_5_start = datetime.now()
#             ttest_s625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_5_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_s625_625_5_dir'))
#             ttest_s625_625_5_end = datetime.now()
#             logging.info("Elapsed time for ttest for single625_625_5_v" + str(i) + " " + str(ttest_s625_625_5_end - ttest_s625_625_5_start))
            
#             #Run ttest on random0_0 with 5 samples per cond
#             ttest_r0_0_5_start = datetime.now()
#             ttest_r0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_5_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_r0_0_5_dir'))
#             ttest_r0_0_5_end = datetime.now()
#             logging.info("Elapsed time for ttest for random0_0_5_v" + str(i) + " " + str(ttest_r0_0_5_end - ttest_r0_0_5_start))
            
#             #Run ttest on random625_625 with 5 samples per cond
#             ttest_r625_625_5_start = datetime.now()
#             ttest_r625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_5_v' + str(i)), analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'), analysis_cfg.get('ttest_r625_625_5_dir'))
#             ttest_r625_625_5_end = datetime.now()
#             logging.info("Elapsed time for ttest for random625_625_5_v" + str(i) + " " + str(ttest_r625_625_5_end - ttest_r625_625_5_start))


            #Run PoissonSeq on the synthetic datasets above
            
            #Run PoissonSeq on baseline0_0 with 5 samples per cond
#             PoissonSeq_b0_0_5_start = datetime.now()
#             PoissonSeq_b0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_5_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_b0_0_5_dir'))
#             PoissonSeq_b0_0_5_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for baseline0_0_5_v" + str(i) + " " + str(PoissonSeq_b0_0_5_end - PoissonSeq_b0_0_5_start))
            
#             #Run PoissonSeq on baseline1250_0 with 5 samples per cond
#             PoissonSeq_b1250_0_5_start = datetime.now()
#             PoissonSeq_b1250_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_5_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_b1250_0_5_dir'))
#             PoissonSeq_b1250_0_5end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for baseline1250_0_5_v" + str(i) + " " + str(PoissonSeq_b1250_0_5end - PoissonSeq_b1250_0_5_start))
            
#             #Run PoissonSeq on baseline625_625 with 5 samples per cond
#             PoissonSeq_b625_625_5_start = datetime.now()
#             PoissonSeq_b625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_5_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_b625_625_5_dir'))
#             PoissonSeq_b625_625_5end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for baseline625_625_5_v" + str(i) + " " + str(PoissonSeq_b625_625_5end - PoissonSeq_b625_625_5_start))
            
#             #Run PoissonSeq on baseline4000_0 with 5 samples per cond
#             PoissonSeq_b4000_0_5_start = datetime.now()
#             PoissonSeq_b4000_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_5_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_b4000_0_5_dir'))
#             PoissonSeq_b4000_0_5end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for baseline4000_0_5_v" + str(i) + " " + str(PoissonSeq_b4000_0_5end - PoissonSeq_b4000_0_5_start))
            
#             #Run PoissonSeq on baseline2000_2000 with 5 samples per cond
#             PoissonSeq_b2000_2000_5_start = datetime.now()
#             PoissonSeq_b2000_2000_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_5_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_b2000_2000_5_dir'))
#             PoissonSeq_b2000_2000_5end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for baseline2000_2000_5_v" + str(i) + " " + str(PoissonSeq_b2000_2000_5end - PoissonSeq_b2000_2000_5_start))
            
#             #Run PoissonSeq on poisson0_0 with 5 samples per cond
#             PoissonSeq_p0_0_5_start = datetime.now()
#             PoissonSeq_p0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_5_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_p0_0_5_dir'))
#             PoissonSeq_p0_0_5_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for poisson0_0_5_v" + str(i) + " " + str(PoissonSeq_p0_0_5_end - PoissonSeq_p0_0_5_start))
            
#             #Run PoissonSeq on poisson625_625 with 5 samples per cond
#             PoissonSeq_p625_625_5_start = datetime.now()
#             PoissonSeq_p625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_5_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_p625_625_5_dir'))
#             PoissonSeq_p625_625_5_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for poisson625_625_5_v" + str(i) + " " + str(PoissonSeq_p625_625_5_end - PoissonSeq_p625_625_5_start))
            
#             #Run PoissonSeq on single0_0 with 5 samples per cond
#             PoissonSeq_s0_0_5_start = datetime.now()
#             PoissonSeq_s0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_5_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_s0_0_5_dir'))
#             PoissonSeq_s0_0_5_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for single0_0_5_v" + str(i) + " " + str(PoissonSeq_s0_0_5_end - PoissonSeq_s0_0_5_start))
            
#             #Run PoissonSeq on single625_625 with 5 samples per cond
#             PoissonSeq_s625_625_5_start = datetime.now()
#             PoissonSeq_s625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_5_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_s625_625_5_dir'))
#             PoissonSeq_s625_625_5_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for single625_625_5_v" + str(i) + " " + str(PoissonSeq_s625_625_5_end - PoissonSeq_s625_625_5_start))
            
#             #Run PoissonSeq on random0_0 with 5 samples per cond
#             PoissonSeq_r0_0_5_start = datetime.now()
#             PoissonSeq_r0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_5_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_r0_0_5_dir'))
#             PoissonSeq_r0_0_5_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for random0_0_5_v" + str(i) + " " + str(PoissonSeq_r0_0_5_end - PoissonSeq_r0_0_5_start))
            
#             #Run PoissonSeq on random625_625 with 5 samples per cond
#             PoissonSeq_r625_625_5_start = datetime.now()
#             PoissonSeq_r625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_5_v' + str(i)), analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'), analysis_cfg.get('PoissonSeq_r625_625_5_dir'))
#             PoissonSeq_r625_625_5_end = datetime.now()
#             logging.info("Elapsed time for PoissonSeq for random625_625_5_v" + str(i) + " " + str(PoissonSeq_r625_625_5_end - PoissonSeq_r625_625_5_start))



#             #Run ABSSeq on the synthetic datasets above
            
#             #Run ABSSeq on baseline0_0 with 5 samples per cond
#             ABSSeq_b0_0_5_start = datetime.now()
#             ABSSeq_b0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b0_0_5_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_b0_0_5_dir'))
#             ABSSeq_b0_0_5_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for baseline0_0_5_v" + str(i) + " " + str(ABSSeq_b0_0_5_end - ABSSeq_b0_0_5_start))
            
#             #Run ABSSeq on baseline1250_0 with 5 samples per cond
#             ABSSeq_b1250_0_5_start = datetime.now()
#             ABSSeq_b1250_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b1250_0_5_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_b1250_0_5_dir'))
#             ABSSeq_b1250_0_5end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for baseline1250_0_5_v" + str(i) + " " + str(ABSSeq_b1250_0_5end - ABSSeq_b1250_0_5_start))
            
#             #Run ABSSeq on baseline625_625 with 5 samples per cond
#             ABSSeq_b625_625_5_start = datetime.now()
#             ABSSeq_b625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b625_625_5_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_b625_625_5_dir'))
#             ABSSeq_b625_625_5end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for baseline625_625_5_v" + str(i) + " " + str(ABSSeq_b625_625_5end - ABSSeq_b625_625_5_start))
            
#             #Run ABSSeq on baseline4000_0 with 5 samples per cond
#             ABSSeq_b4000_0_5_start = datetime.now()
#             ABSSeq_b4000_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b4000_0_5_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_b4000_0_5_dir'))
#             ABSSeq_b4000_0_5end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for baseline4000_0_5_v" + str(i) + " " + str(ABSSeq_b4000_0_5end - ABSSeq_b4000_0_5_start))
            
#             #Run ABSSeq on baseline2000_2000 with 5 samples per cond
#             ABSSeq_b2000_2000_5_start = datetime.now()
#             ABSSeq_b2000_2000_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('b2000_2000_5_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_b2000_2000_5_dir'))
#             ABSSeq_b2000_2000_5end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for baseline2000_2000_5_v" + str(i) + " " + str(ABSSeq_b2000_2000_5end - ABSSeq_b2000_2000_5_start))
            
#             #Run ABSSeq on poisson0_0 with 5 samples per cond
#             ABSSeq_p0_0_5_start = datetime.now()
#             ABSSeq_p0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p0_0_5_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_p0_0_5_dir'))
#             ABSSeq_p0_0_5_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for poisson0_0_5_v" + str(i) + " " + str(ABSSeq_p0_0_5_end - ABSSeq_p0_0_5_start))
            
#             #Run ABSSeq on poisson625_625 with 5 samples per cond
#             ABSSeq_p625_625_5_start = datetime.now()
#             ABSSeq_p625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('p625_625_5_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_p625_625_5_dir'))
#             ABSSeq_p625_625_5_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for poisson625_625_5_v" + str(i) + " " + str(ABSSeq_p625_625_5_end - ABSSeq_p625_625_5_start))
            
#             #Run ABSSeq on single0_0 with 5 samples per cond
#             ABSSeq_s0_0_5_start = datetime.now()
#             ABSSeq_s0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s0_0_5_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_s0_0_5_dir'))
#             ABSSeq_s0_0_5_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for single0_0_5_v" + str(i) + " " + str(ABSSeq_s0_0_5_end - ABSSeq_s0_0_5_start))
            
#             #Run ABSSeq on single625_625 with 5 samples per cond
#             ABSSeq_s625_625_5_start = datetime.now()
#             ABSSeq_s625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('s625_625_5_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_s625_625_5_dir'))
#             ABSSeq_s625_625_5_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for single625_625_5_v" + str(i) + " " + str(ABSSeq_s625_625_5_end - ABSSeq_s625_625_5_start))
            
#             #Run ABSSeq on random0_0 with 5 samples per cond
#             ABSSeq_r0_0_5_start = datetime.now()
#             ABSSeq_r0_0_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r0_0_5_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_r0_0_5_dir'))
#             ABSSeq_r0_0_5_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for random0_0_5_v" + str(i) + " " + str(ABSSeq_r0_0_5_end - ABSSeq_r0_0_5_start))
            
#             #Run ABSSeq on random625_625 with 5 samples per cond
#             ABSSeq_r625_625_5_start = datetime.now()
#             ABSSeq_r625_625_5 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('r625_625_5_v' + str(i)), analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'), analysis_cfg.get('ABSSeq_r625_625_5_dir'))
#             ABSSeq_r625_625_5_end = datetime.now()
#             logging.info("Elapsed time for ABSSeq for random625_625_5_v" + str(i) + " " + str(ABSSeq_r625_625_5_end - ABSSeq_r625_625_5_start))


    if 'compare' in targets:
        with open('config/comparison-params.json') as fh:
            compare_data_cfg = json.load(fh)
        
        comparison = run_comparison_rscript(compare_data_cfg.get('ABSSeq_dir'), compare_data_cfg.get('DESeq_dir'), compare_data_cfg.get('edgeR_dir'), compare_data_cfg.get('NOISeq_dir'), compare_data_cfg.get('ttest_dir'), compare_data_cfg.get('PoissonSeq_dir'), compare_data_cfg.get('voom_dir'), compare_data_cfg.get('out_dir'))



    if 'test' in targets:
        with open('config/test-params.json') as fh:
            t_data_cfg = json.load(fh)
        testing = run_test_rscript(**t_data_cfg)
    return

if __name__ == '__main__':
    targets = sys.argv[1]
    main(targets)
