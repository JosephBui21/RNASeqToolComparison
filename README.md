# RNASeqToolComparison
Data Science Senior Capstone Project: Comparing RNA Sequencing Differential Gene Expression Analysis Tools

In this project, we want to compare distinct differential gene expression analysis tools on simulated data created with different numbers of genes differentially expressed.

## Running the project
* Use the command `launch.sh -i buijoseph21/rna-seq-tool-comparison:v1 -m 6` in order to have the necessary software from `compcodeR` (e.g., `generateSyntheticData`, `runDiffExp`, `ABSSeq`, `PoissonSeq`, etc.) to generate the synthetic data & perform differential gene expression analysis. The `-m 6` specifies the number of RAM which is needed to run tools that require more memory. 

## Building the project using `run.py`
* Use the command `python run.py build` to generate the synthetic data in `data/data<N>.rds`, where N represents the dataset number, using `generateSyntheticData`
* Use the command `python run.py analysis` to perform `DESeq2`, `edgeR.exact`, `NOISeq`, `PoissonSeq`, `ttest`, `ABSSeq`, and `voom.limma` on the synthetic data created in `data` folder which returns the results in `out/data<N>_<tool>.rds`, where N represents the dataset number & tool represents the software. The output of each tool will be organized in its respective `<tool_name>` folders. 
* Use the command `python run.py compare` to create a CSV called ` which returns the number of genes differentially expressed for every tool. In this case, we considered a gene to be differentially expressed if the p-value of the results from the software return < 0.05. 

## Running the project on test data
* `ssh` into dsmlp and `git clone` the repository
* Use the command `launch.sh -i buijoseph21/rna-seq-tool-comparison:v1 -m 6` in order to have the necessary software from `compcodeR` (e.g., `generateSyntheticData`, `runDiffExp`, `PoissonSeq`, etc.) to generate the test synthetic data & perform differential gene expression analysis. The `-m 6` specifies the number of RAM which is needed to run tools that require more memory. 
* Use the command `python run.py test` to create a test synthetic dataset of 100 genes differentially expressed where 50 are differentially expressed in condition 1 and 50 are differentially expressed in condition 2. This test dataset contains 5 samples per condition and is a baseline model with no outliers containing abnormal counts. When running `python run.py test`, it should first create a synthetic dataset which will be stored in the `data` folder and named as `test.rds`. Next, the 7 tools will be performed on the `test.rds` where the outputs will be stored in the `out/test` folder which is created when ran. Each tool will produce different results which is stored in `test_<tool>.rds`. For the next step of our pipeline, we want to produce the number of genes differentially expressed by each tool using a significance level of 0.05 where the output is stored in the `num_expressed_by_tool_test.csv` in the `out/test` folder. 

## Group Contributions
* Joseph built the dockerfile/container. He also created the starter code for building the synthetic datasets and performing differential expression analysis tools in `compcodeR` such as `DESeq2`, `edgeR`, `NOISeq`, `voom.limma`, and `ttest`. He was able to create an R script that read all the outputs from each tool mentioned previously to write out to a `num_expressed_by_tool.csv`. He also created the notebook that illustrates the timings/duration for each of the tools performed on each synthetic dataset.
* Brandon was responsible for creating the `random` outlier synthetic datasets and performing differential expression analysis tools not built-in `compcodeR`, including `ABSSeq` and `PoissonSeq`. Brandon helped write out to the `num_expressed_by_tool.csv` for his outputs produced by `ABSSeq` and `PoissonSeq`. 
* Luigi was responsible for creating the `single` outlier and `poisson` synthetic datasets and helped perform `NOISeq` and `voom.limma` on the synthetic datasets. 
