#command arguments from config/build-params.json which builds the synthetic data
myArgs <- commandArgs(trailingOnly = TRUE)

#install necessary packages
library('compcodeR')

data <- myArgs[1]
num_vars <- strtoi(myArgs[2])
samples_per_cond <- strtoi(myArgs[3])
num_diff_exp <- strtoi(myArgs[4])
ratio_upregulated <- as.numeric(myArgs[5])
output_dir <- myArgs[6]

syntheticData <- generateSyntheticData(dataset = data, n.vars = num_vars, samples.per.cond = samples_per_cond, n.diffexp = num_diff_exp, fraction.upregulated = ratio_upregulated, output.file = output_dir)
