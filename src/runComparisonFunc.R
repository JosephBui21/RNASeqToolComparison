#command arguments from config/comparison-params.json which specifies what tool is being compared & in/out file directories
myArgs <- commandArgs(trailingOnly = TRUE)
library('compcodeR')

print('1')
file.table <- data.frame(input.files = file.path(myArgs[1], c(myArgs[2], myArgs[3], myArgs[4], myArgs[5])), stringAsFactors = FALSE)
print('2')
params <- list(incl.nbr.samples = strtoi(myArgs[6]), incl.replicates = strtoi(myArgs[7]), incl.dataset = myArgs[8], incl.de.methods = NULL, fdr.threshold = as.numeric(myArgs[9]), tpr.threshold = as.numeric(myArgs[9]), typeI.threshold = as.numeric(myArgs[9]), ma.threshold = as.numeric(myArgs[9]), overlap.thresold = as.numeric(myArgs[9]), fracsign.threshold = as.numeric(myArgs[9]), mcc.threshold = as.numeric(myArgs[9]), nbrtpfp.threshold = as.numeric(myArgs[9]), comparisons = c("auc", "fdr", "tpr", "ma", "correlation"))
print('3')
runComparison(file.table = file.table, parameters = params, output.directory = file.path(myArgs[1], myArgs[10]))
print('4')