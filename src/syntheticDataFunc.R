#command arguments from config/build-params.json which builds the synthetic data
myArgs <- commandArgs(trailingOnly = TRUE)

#install necessary packages
library('compcodeR')
library('DESeq2')
library('edgeR')

#Create synthetic data #1
example <- generateSyntheticData(dataset = myArgs[1], n.vars = strtoi(myArgs[2]), samples.per.cond = strtoi(myArgs[3]), n.diffexp = strtoi(myArgs[4]))

#Run DESeq2 on synthetic data #1
#runDiffExp(data.file = '~/Downloads/', result.extent = "DESeq2", Rmdfunction = "DESeq2.createRmd", output.directory = )




#Run edgeR on synthetic data #1



#Create synthetic data #2

#Run DESeq2 on synthetic data #2

#Run edgeR on synthetic data #2
