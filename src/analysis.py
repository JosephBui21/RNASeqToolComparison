import os

def run_diff_exp_rscript(in_dir, synthetic_data, tool, tool_rmd, out_dir):
    os.system("/opt/conda/envs/r-bio/bin/Rscript src/performDiffExp.R " + in_dir + ' ' + synthetic_data + ' ' + tool + ' ' + tool_rmd + ' ' + out_dir)
    return