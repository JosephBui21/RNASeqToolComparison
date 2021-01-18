# RNASeqToolComparison
Data Science Senior Capstone Project: Comparing RNA Sequencing Tools

In this project, we want to compare distinct differential gene expression analysis tools on simulated data created with different numbers of genes differentially expressed.

## Running the project
* Use the command `launch.sh -i buijoseph21/rna-seq-tool-comparison:v1` in order to have the necessary software from `compcodeR` (e.g., `generateSyntheticData`, `runDiffExp`, `runComparison`) to generate the synthetic data & perform differential gene expression analysis

## Building the project using `run.py`
* Use the command `python run.py build` to generate the synthetic data in the `data/SyntheticData{N}`, where N represents the dataset number, using `generateSyntheticData` 