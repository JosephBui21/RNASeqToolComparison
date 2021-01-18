library('compcodeR')
# #Run DESeq2 on synthetic data #1
# deseq2_data1 <- runDiffExp(data.file = file.path('out', myArgs[5]), result.extent = "DESeq2", Rmdfunction = "DESeq2.createRmd", output.directory = file.path('out'), fit.type = "parametric", test = "Wald", beta.prior = TRUE, independent.filtering = TRUE, cooks.cutoff = TRUE, impute.outliers = TRUE)

# #Run edgeR on synthetic data #1
# edgeR_data1 <- runDiffExp(data.file = file.path('out', myArgs[5]), result.extent = "edgeR.exact", Rmdfunction = "edgeR.exact.createRmd", output.directory = file.path('out'), norm.method = "TMM", disp.type = "tagwise", trend.method = "movingave")

# #Compare the two tools
# file.table <- data.frame(input.files = file.path('out', c("data1_DESeq2.rds", "data1_edgeR.exact.rds")), stringsAsFactors = FALSE)
# params <- list(incl.nbr.samples = 5, incl.replicates = 1, incl.dataset = "dataExample", incl.de.methods = NULL,
#                    fdr.threshold = 0.05, tpr.threshold = 0.05, typeI.threshold = 0.05, ma.threshold = 0.05, fdc.maxvar = 1500, 
#                    overlap.threshold = 0.05, fracsign.threshold = 0.05, mcc.threshold = 0.05, nbrtpfp.threshold = 0.05,
#                    comparisons = c("auc", "fdr", "tpr", "ma", "correlation"))
# runComparison(file.table = file.table, parameters = params, output.directory = 'out')
#Run DESeq2 on synthetic data #1
#runDiffExp(data.file = '~/Downloads/', result.extent = "DESeq2", Rmdfunction = "DESeq2.createRmd", output.directory = )




#Run edgeR on synthetic data #1



#Create synthetic data #2

#Run DESeq2 on synthetic data #2

#Run edgeR on synthetic data #2