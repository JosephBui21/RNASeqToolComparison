# RNASeqToolComparison
Data Science Senior Capstone Project: Comparing RNA Sequencing Tools

In this project, we want to compare distinct differential gene expression analysis tools on simulated data created with different numbers of genes differentially expressed.

## Running the project
* Use the command `launch.sh -i buijoseph21/rna-seq-tool-comparison:v1 -m 8` in order to have the necessary software from `compcodeR` (e.g., `generateSyntheticData`, `runDiffExp`, `runComparison`) to generate the synthetic data & perform differential gene expression analysis. The `-m 6` specifies the number of RAM which is needed to run tools that require more memory. 

## Building the project using `run.py`
* Use the command `python run.py build` to generate the synthetic data in `data/data<N>.rds`, where N represents the dataset number, using `generateSyntheticData`
* Use the command `python run.py analysis` to perform `DESeq2` and `edgeR.exact` on the synthetic data created in `data` folder which returns the results in `out/data<N>_<tool>.rds`, where N represents the dataset number & tool represents the software
* Use the command `python run.py compare` to compare the tools...