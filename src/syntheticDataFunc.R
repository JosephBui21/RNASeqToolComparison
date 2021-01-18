#command arguments from config/build-params.json which builds the synthetic data
myArgs <- commandArgs(trailingOnly = TRUE)

#install necessary packages
library('compcodeR')

#tmpdir <- normalizePath(tempdir(), winslash = "/")

#Create synthetic data #1 with 5 samples per conditon & 200 differentially expressed genes
fiveSamples_200diff <- generateSyntheticData(dataset = myArgs[1], n.vars = strtoi(myArgs[2]), samples.per.cond = strtoi(myArgs[3]), n.diffexp = strtoi(myArgs[4]), output.file = file.path(myArgs[5]))

#Create synthetic data #2 with 5 samples per conditon & 500 differentially expressed genes
fiveSamples_500diff <- generateSyntheticData(dataset = myArgs[1], n.vars = strtoi(myArgs[2]), samples.per.cond = strtoi(myArgs[3]), n.diffexp = strtoi(myArgs[4]), output.file = file.path(myArgs[5]))

