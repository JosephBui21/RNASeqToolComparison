import os
import subprocess
import shutil
import re

def run_rscript(data, n_vars, samples_per_cond, n_diffexp, output_file):
    
    directory = re.split('/', output_file)[1]
    par_dir = "./data/"
    
    #path for ./data/SyntheticData#
    path = os.path.join(par_dir, directory)
    
    #remove inner directory if one already exists
    if (os.path.exists(path) and os.path.isdir(path)):
        shutil.rmtree(path)
    
    #create a directory for a synthetic data
    os.mkdir(path)
    
    os.system("/opt/conda/envs/r-bio/bin/Rscript src/syntheticDataFunc.R " + data + ' ' + str(n_vars) + ' ' + str(samples_per_cond) + ' ' + str(n_diffexp) + ' ' + output_file)
    return

def run_rscript_test(string):
    os.system("/opt/conda/envs/r-bio/bin/Rscript src/test.R " + string)
    return
