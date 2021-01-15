import os
import subprocess

def run_rscript(data, n_vars, samples_per_cond, n_diffexp, output_file):
    os.system("Rscript src/syntheticDataFunc.R " + data + ' ' + str(n_vars) + ' ' + str(samples_per_cond) + ' ' + str(n_diffexp) + ' ' + output_file)
    return

def run_rscript_test(string):
    print(os.getcwd())
    curr = os.getcwd()
    path = os.path.join(curr, 'src/test.R')
    print(path)
    subprocess.call(['Rscript', path , string])
