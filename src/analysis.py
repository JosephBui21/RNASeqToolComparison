import os

def run_diff_exp_rscript(in_dir, synthetic_data, tool, tool_rmd, out_dir):
    os.system("/opt/conda/envs/r-bio/bin/Rscript src/performDiffExp.R " + in_dir + ' ' + synthetic_data + ' ' + tool + ' ' + tool_rmd + ' ' + out_dir)
    return

def run_comparison_rscript(tool_dir1, tool_dir2, tool_dir3, tool_dir4, tool_dir5, tool_dir6, tool_dir7, out_dir):
    os.system("/opt/conda/envs/r-bio/bin/Rscript src/compareTools.R " + tool_dir1 + ' ' + tool_dir2 + ' ' + tool_dir3 + ' ' + tool_dir4 + ' ' + tool_dir5 + ' ' + tool_dir6 + ' ' + tool_dir7 + ' ' + out_dir)
    return

def run_graph_rscript():
    os.system("/opt/conda/envs/r-bio/bin/Rscript src/generateGraphs.R")
    return
