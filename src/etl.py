import os

def run_rscript(data, n_vars, samples_per_cond, n_diffexp, output_file):
    os.system("Rscript src/syntheticDataFunc.R ")# + data + ' ' + str(n_vars) + ' ' + str(samples_per_cond) + ' ' + str(n_diffexp) + ' ' + output_file)
    return
