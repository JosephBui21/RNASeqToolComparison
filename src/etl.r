create_synthetic_data <- function(data, vars, samples_per_cond, n_diffexp, output_file) {
    data = generateSyntheticData(dataset = data, n.vars = vars, samples.per.cond = samples_per_cond, n.diffexp = n_diffexp, output.file = output_file)
}
