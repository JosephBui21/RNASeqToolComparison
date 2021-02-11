#! /usr/bin/env python
import sys
import os
import json
sys.path.insert(0, 'src')
from etl import run_create_data_rscript
from analysis import run_diff_exp_rscript, run_comparison_rscript
from test import run_test_rscript
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

        #All the synthetic data below is created with 12,500 genes
        for i in range(1, 11):
            
            #Create baseline synthetic data #1 with 0 differentially expressed genes for 5 samples per condition 10x
            print("Generating baseline synthetic data v" + str(i) + " with 0 differentially expressed genes for 5 samples per condition")
            baseline0_0_5 = run_create_data_rscript(data_cfg.get("b0_0_5_v" + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get("output_fileB0_0_5_v" + str(i)), data_cfg.get('seqdepth'))
            
            #Create baseline synthetic data #2 with 1250 differentially expressed genes with 1250 upregulated in condition 1 and 0 downregulated in condition 2 for 5 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 1250 upregulated in condition 1 and 0 downregulated in condition 2 for 5 samples per condition")
            baseline1250_0_5 = run_create_data_rscript(data_cfg.get('b1250_0_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB1250_0_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create baseline synthetic data #3 with 1250 differentially expressed genes with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 5 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 625 upregulated in condition 1 and 625 downregulated in condition 2 for 5 samples per condition")
            baseline625_625_5 = run_create_data_rscript(data_cfg.get('b625_625_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB625_625_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create baseline synthetic data #4 with 4000 differentially expressed genes with 4000 upregulated in condition 1 & 0 in condition 2 for 5 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 4000 upregulated in condition 1 and 0 downregulated in condition 2 for 5 samples per condition")
            baseline4000_0_5 = run_create_data_rscript(data_cfg.get('b4000_0_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp4000'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB4000_0_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create baseline synthetic data #5 with 4000 differentially expressed genes with 2000 upregulated in condition 1 & 2000 in condition 2 for 5 samples per condition
            print("Generating baseline synthetic data v" + str(i) + " with 2000 upregulated in condition 1 & 2000 in condition 2 for 5 samples per condition")
            baseline2000_2000_5 = run_create_data_rscript(data_cfg.get('b2000_2000_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp4000'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileB2000_2000_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #6 whose counts were drawn from poisson distribution with 0 genes differentially expressed for 5 samples per condition
            print("Generating poisson synthetic data v" + str(i) + " with 0 differentially expressed for 5 samples per condition")
            poisson0_0_5 = run_create_data_rscript(data_cfg.get('p0_0_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileP0_0_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #7 whose counts were drawn from poisson distribution with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 5 samples per condition
            print("Generating poisson synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 5 samples per condition")
            poisson625_625_5 = run_create_data_rscript(data_cfg.get('p625_625_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_fileP625_625_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #8 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 0 differentially expressed genes
            print("Generating single synthetic data v" + str(i) + " with 0 upregulated in condition 1 & 0 downregulated in condition 2 for 5 samples per condition")
            single0_0_5 = run_create_data_rscript(data_cfg.get('s0_0_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single_count'), data_cfg.get('output_fileS0_0_5_v' + str(i)), data_cfg.get('seqdepth'))

                #Create synthetic data #9 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 625 genes expressed in cond 1 & 625 in cond 2
            print("Generating single synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 5 samples per condition")
            single625_625_5 = run_create_data_rscript(data_cfg.get('s625_625_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single_count'), data_cfg.get('output_fileS625_625_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #10 where fraction of genes for which we selected a random sample and multiplied the corresponding count with a factor between 5 and 10 with 0 differentially expressed genes
            print("Generating random synthetic data v" + str(i) + " with 0 upregulated in condition 1 & 0 downregulated in condition 2 for 5 samples per condition")
            random0_0_5 = run_create_data_rscript(data_cfg.get('r0_0_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type3'), data_cfg.get('random_outlier'), data_cfg.get('output_fileR0_0_5_v' + str(i)), data_cfg.get('seqdepth'))

            #Create synthetic data #11 where fraction of genes for which we selected a random sample and multiplied the corresponding count with a factor between 5 and 10 with 625 genes expressed in cond 1 & 625 in cond 2
            print("Generating random synthetic data v" + str(i) + " with 625 upregulated in condition 1 & 625 downregulated in condition 2 for 5 samples per condition")
            random625_625_5 = run_create_data_rscript(data_cfg.get('r625_625_5_v' + str(i)), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond5'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type3'), data_cfg.get('random_outlier'), data_cfg.get('output_fileR625_625_5_v' + str(i)), data_cfg.get('seqdepth'))



    #Run differential gene expression analysis tools on the synthetic data
    if 'analysis' in targets:
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)

        for i in range(1, 12):
            synthetic_num = str(i)

            #Run DESeq2 on the 11 synthetic datasets above
            logging.info("Performing DESeq2 on synthetic data #" + synthetic_num)
            deseq2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                          analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'),
                                          analysis_cfg.get('DESeq2_dir'))
            logging.info("Finished performing DESeq2 on synthetic data #" + synthetic_num)

            #Run edgeR.exact on the 11 synthetic datasets above
            logging.info("Performing edgeR on synthetic data #" + synthetic_num)
            edgeR = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                          analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'),
                                          analysis_cfg.get('edgeR_dir'))
            logging.info("Finished performing edgeR on synthetic data #" + synthetic_num)

            #Run voom.limma on the 11 synthetic datasets above
            logging.info("Performing voom.limma on synthetic data #" + synthetic_num)
            voom_limma = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                          analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'),
                                          analysis_cfg.get('voom_limma_dir'))
            logging.info("Finished performing voom.limma on synthetic data #" + synthetic_num)

            #Run NOISeq on the 11 synthetic datasets above
            logging.info("Performing NOISeq on synthetic data #" + synthetic_num)
            NOISeq = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                          analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'),
                                          analysis_cfg.get('NOISeq_dir'))
            logging.info("Finished performing NOISeq on synthetic data #" + synthetic_num)

            #Run ttest on the 11 synthetic datasets above
            logging.info("Performing ttest on synthetic data #" + synthetic_num)
            ttest = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                          analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'),
                                          analysis_cfg.get('ttest_dir'))
            logging.info("Finished performing ttest on synthetic data #" + synthetic_num)


            #Run PoissonSeq on the 11 synthetic datasets above
            logging.info("Performing PoissonSeq on synthetic data #" + synthetic_num)
            POIS = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                           analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'),
                                           analysis_cfg.get('PoissonSeq_dir'))
            logging.info("Finished performing PoissonSeq on synthetic data #" + synthetic_num)

             #Run ABSSeq on the 11 synthetic datasets above
            logging.info("Performing ABSSeq on synthetic data #" + synthetic_num)
            ABSSeq = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                            analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'),
                                            analysis_cfg.get('ABSSeq_dir'))
            logging.info("Finished performing ABSSeq on synthetic data #" + synthetic_num)


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
