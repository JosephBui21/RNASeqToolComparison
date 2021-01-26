#command arguments from config/comparison-params.json which specifies what tool is being compared & in/out file directories
myArgs <- commandArgs(trailingOnly = TRUE)
library('compcodeR')
library('rpanel')

runComparisonGUI(input.directories = data.frame(input.files = file.path(myArgs[1],
                         c(myArgs[2], myArgs[3])),
                         stringsAsFactors = FALSE), recursive = FALSE)