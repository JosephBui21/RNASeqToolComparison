
myArgs <- commandArgs(trailingOnly = TRUE)

library('compcodeR')

data = myArgs[1]
n_vars = myArgs[2]
samples_per_cond = myArgs[3]
n_diffexp = myArgs[4]
output_file = myArgs[5]


create_synthetic_data <- function(data, n_vars, samples_per_cond, n_diffexp, output_file) {
    data = generateSyntheticData(dataset = data, n.vars = vars, samples.per.cond = samples_per_cond, n.diffexp = n_diffexp, output.file = output_file)
}
