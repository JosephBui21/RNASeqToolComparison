#command arguments from config/comparison-params.json which specifies what tool is being compared & in/out file directories
myArgs <- commandArgs(trailingOnly = TRUE)
library('compcodeR')


file.table <- data.frame(input.files = file.path(myArgs[1], c(myArgs[2], myArgs[3])), stringAsFactors = FALSE)

params <- list(incl.nbr.samples = strtoi(myArgs[4]), incl.replicates = strtoi(myArgs[5]), incl.dataset = myArgs[6], incl.de.methods = NULL, fdr.threshold = as.numeric(myArgs[7]), tpr.threshold = as.numeric(myArgs[7]), typeI.threshold = as.numeric(myArgs[7]), ma.threshold = as.numeric(myArgs[7]), overlap.thresold = as.numeric(myArgs[7]), fracsign.threshold = as.numeric(myArgs[7]), mcc.threshold = as.numeric(myArgs[7]), nbrtpfp.threshold = as.numeric(myArgs[7]), comparisons = c("auc", "fdr", "tpr", "ma", "correlation"))

runComparison(file.table = file.table, parameters = params, output.directory = file.path(myArgs[1]))