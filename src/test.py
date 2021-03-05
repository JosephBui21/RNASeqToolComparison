import os
import shutil

def run_test_rscript(synthetic_name, num_vars, samples_per_cond, rep_id, seq_depth, num_diff_exp, ratio_upregulated, dispersion_num, synData_output_dir, indir, data, tool1, rmdFunc1, tool2, rmdFunc2, tool3, rmdFunc3, tool4, rmdFunc4, tool5, rmdFunc5, outdir):
    
    os.system("/opt/conda/envs/r-bio/bin/Rscript src/test.R " + synthetic_name + ' ' + str(num_vars) + ' ' + str(samples_per_cond) + ' ' + str(rep_id) + ' ' + seq_depth + ' ' + str(num_diff_exp) + ' ' + ratio_upregulated + ' ' + str(dispersion_num) + ' ' + synData_output_dir + ' ' + indir + ' ' + data + ' ' + tool1 + ' ' + rmdFunc1 + ' ' + tool2 + ' ' + rmdFunc2 + ' ' + tool3 + ' ' + rmdFunc3 + ' ' + tool4 + ' ' + rmdFunc4 + ' ' + tool5 + ' ' + rmdFunc5 + ' ' + outdir)
    return