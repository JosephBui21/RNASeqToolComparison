
myArgs <- commandArgs(trailingOnly = TRUE)

library('compcodeR')

generateSyntheticData(dataset = myArgs[1], n.vars = strtoi(myArgs[2]), samples.per.cond = strtoi(myArgs[3]), n.diffexp = strtoi(myArgs[4]), output.file = myArgs[5])
