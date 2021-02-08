myArgs <- commandArgs(trailingOnly = TRUE)
library('compcodeR')

#Baseline 0 0
baseline0_0_ABSSeq <- readRDS(file.path(myArgs[1], "baseline0_0_ABSSeq.rds"))
baseline0_0_ABSSeq_diff_exp <- sum(baseline0_0_ABSSeq["prediction"])
baseline0_0_DESeq2 <- convertcompDataToList(readRDS(file.path(myArgs[2], "baseline0_0_DESeq2.rds")))
baseline0_0_DESeq2_diff_exp <- nrow(baseline0_0_DESeq2$result.table[baseline0_0_DESeq2$result.table$pvalue < 0.05,])
baseline0_0_edgeR <- convertcompDataToList(readRDS(file.path(myArgs[3], "baseline0_0_edgeR.exact.rds")))
baseline0_0_edgeR_diff_exp<- nrow(baseline0_0_edgeR$result.table[baseline0_0_edgeR$result.table$pvalue < 0.05,])
baseline0_0_NOISeq <- convertcompDataToList(readRDS(file.path(myArgs[4], "baseline0_0_NOISeq.rds")))
baseline0_0_NOISeq_diff_exp <- nrow(baseline0_0_NOISeq$result.table[baseline0_0_NOISeq$result.table$probabilities < 0.05,])
baseline0_0_ttest <- convertcompDataToList(readRDS(file.path(myArgs[5], "baseline0_0_ttest.rds")))
baseline0_0_ttest_diff_exp <- nrow(baseline0_0_ttest$result.table[baseline0_0_ttest$result.table$pvalue < 0.05,])
baseline0_0_PoissonSeq <- readRDS(file.path(myArgs[6], "baseline0_0_PoissonSeq.rds"))
baseline0_0_PoissonSeq_diff_exp <- sum(baseline0_0_PoissonSeq["prediction"])
baseline0_0_voom <- convertcompDataToList(readRDS(file.path(myArgs[7], "baseline0_0_voom.limma.rds")))
baseline0_0_voom_diff_exp <- nrow(baseline0_0_voom$result.table[baseline0_0_voom$result.table$pvalue < 0.05,])
#create a dataframe showing number of genes considered differentially expressed by each tool:
baseline0_0_df <- data.frame(DESeq2 = c(baseline0_0_DESeq2_diff_exp),
                             edgeR = c(baseline0_0_edgeR_diff_exp),
                             NOISeq = c(baseline0_0_NOISeq_diff_exp),
                             ttest = c(baseline0_0_ttest_diff_exp),
                             voom.limma = c(baseline0_0_voom_diff_exp),
                             PoissonSeq = c(baseline0_0_PoissonSeq_diff_exp),
                             ABSSeq = c(baseline0_0_ABSSeq_diff_exp))

#Baseline 1250 0
baseline1250_0_ABSSeq <- readRDS(file.path(myArgs[1], "baseline1250_0_ABSSeq.rds"))
baseline1250_0_ABSSeq_diff_exp <- sum(baseline1250_0_ABSSeq["prediction"])
baseline1250_0_DESeq2 <- convertcompDataToList(readRDS(file.path(myArgs[2], "baseline1250_0_DESeq2.rds")))
baseline1250_0_DESeq2_diff_exp <- nrow(baseline1250_0_DESeq2$result.table[baseline1250_0_DESeq2$result.table$pvalue < 0.05,])
baseline1250_0_edgeR <- convertcompDataToList(readRDS(file.path(myArgs[3], "baseline1250_0_edgeR.exact.rds")))
baseline1250_0_edgeR_diff_exp<- nrow(baseline1250_0_edgeR$result.table[baseline1250_0_edgeR$result.table$pvalue < 0.05,])
baseline1250_0_NOISeq <- convertcompDataToList(readRDS(file.path(myArgs[4], "baseline1250_0_NOISeq.rds")))
baseline1250_0_NOISeq_diff_exp <- nrow(baseline1250_0_NOISeq$result.table[baseline1250_0_NOISeq$result.table$probabilities < 0.05,])
baseline1250_0_ttest <- convertcompDataToList(readRDS(file.path(myArgs[5], "baseline1250_0_ttest.rds")))
baseline1250_0_ttest_diff_exp <- nrow(baseline1250_0_ttest$result.table[baseline1250_0_ttest$result.table$pvalue < 0.05,])
baseline1250_0_PoissonSeq <- readRDS(file.path(myArgs[6], "baseline1250_0_PoissonSeq.rds"))
baseline1250_0_PoissonSeq_diff_exp <- sum(baseline1250_0_PoissonSeq["prediction"])
baseline1250_0_voom <- convertcompDataToList(readRDS(file.path(myArgs[7], "baseline1250_0_voom.limma.rds")))
baseline1250_0_voom_diff_exp <- nrow(baseline1250_0_voom$result.table[baseline1250_0_voom$result.table$pvalue < 0.05,])
#create a dataframe showing number of genes considered differentially expressed by each tool:
baseline1250_0_df <- data.frame(DESeq2 = c(baseline1250_0_DESeq2_diff_exp),
                             edgeR = c(baseline1250_0_edgeR_diff_exp),
                             NOISeq = c(baseline1250_0_NOISeq_diff_exp),
                             ttest = c(baseline1250_0_ttest_diff_exp),
                             voom.limma = c(baseline1250_0_voom_diff_exp),
                             PoissonSeq = c(baseline1250_0_PoissonSeq_diff_exp),
                             ABSSeq = c(baseline1250_0_ABSSeq_diff_exp))

# #Baseline 625 625
baseline625_625_ABSSeq <- readRDS(file.path(myArgs[1], "baseline625_625_ABSSeq.rds"))
baseline625_625_ABSSeq_diff_exp <- sum(baseline625_625_ABSSeq["prediction"])
baseline625_625_DESeq2 <- convertcompDataToList(readRDS(file.path(myArgs[2], "baseline625_625_DESeq2.rds")))
baseline625_625_DESeq2_diff_exp <- nrow(baseline625_625_DESeq2$result.table[baseline625_625_DESeq2$result.table$pvalue < 0.05,])
baseline625_625_edgeR <- convertcompDataToList(readRDS(file.path(myArgs[3], "baseline625_625_edgeR.exact.rds")))
baseline625_625_edgeR_diff_exp<- nrow(baseline625_625_edgeR$result.table[baseline625_625_edgeR$result.table$pvalue < 0.05,])
baseline625_625_NOISeq <- convertcompDataToList(readRDS(file.path(myArgs[4], "baseline625_625_NOISeq.rds")))
baseline625_625_NOISeq_diff_exp <- nrow(baseline625_625_NOISeq$result.table[baseline625_625_NOISeq$result.table$probabilities < 0.05,])
baseline625_625_ttest <- convertcompDataToList(readRDS(file.path(myArgs[5], "baseline625_625_ttest.rds")))
baseline625_625_ttest_diff_exp <- nrow(baseline625_625_ttest$result.table[baseline625_625_ttest$result.table$pvalue < 0.05,])
baseline625_625_PoissonSeq <- readRDS(file.path(myArgs[6], "baseline625_625_PoissonSeq.rds"))
baseline625_625_PoissonSeq_diff_exp <- sum(baseline625_625_PoissonSeq["prediction"])
baseline625_625_voom <- convertcompDataToList(readRDS(file.path(myArgs[7], "baseline625_625_voom.limma.rds")))
baseline625_625_voom_diff_exp <- nrow(baseline625_625_voom$result.table[baseline625_625_voom$result.table$pvalue < 0.05,])
baseline625_625_df <- data.frame(DESeq2 = c(baseline625_625_DESeq2_diff_exp),
                                edgeR = c(baseline625_625_edgeR_diff_exp),
                                NOISeq = c(baseline625_625_NOISeq_diff_exp),
                                ttest = c(baseline625_625_ttest_diff_exp),
                                voom.limma = c(baseline625_625_voom_diff_exp),
                                PoissonSeq = c(baseline625_625_PoissonSeq_diff_exp),
                                ABSSeq = c(baseline625_625_ABSSeq_diff_exp))

# #Baseline 4000 0
baseline4000_0_ABSSeq <- readRDS(file.path(myArgs[1], "baseline4000_0_ABSSeq.rds"))
baseline4000_0_ABSSeq_diff_exp <- sum(baseline4000_0_ABSSeq["prediction"])
baseline4000_0_DESeq2 <- convertcompDataToList(readRDS(file.path(myArgs[2], "baseline4000_0_DESeq2.rds")))
baseline4000_0_DESeq2_diff_exp <- nrow(baseline4000_0_DESeq2$result.table[baseline4000_0_DESeq2$result.table$pvalue < 0.05,])
baseline4000_0_edgeR <- convertcompDataToList(readRDS(file.path(myArgs[3], "baseline4000_0_edgeR.exact.rds")))
baseline4000_0_edgeR_diff_exp<- nrow(baseline4000_0_edgeR$result.table[baseline4000_0_edgeR$result.table$pvalue < 0.05,])
baseline4000_0_NOISeq <- convertcompDataToList(readRDS(file.path(myArgs[4], "baseline4000_0_NOISeq.rds")))
baseline4000_0_NOISeq_diff_exp <- nrow(baseline4000_0_NOISeq$result.table[baseline4000_0_NOISeq$result.table$probabilities < 0.05,])
baseline4000_0_ttest <- convertcompDataToList(readRDS(file.path(myArgs[5], "baseline4000_0_ttest.rds")))
baseline4000_0_ttest_diff_exp <- nrow(baseline4000_0_ttest$result.table[baseline4000_0_ttest$result.table$pvalue < 0.05,])
baseline4000_0_PoissonSeq <- readRDS(file.path(myArgs[6], "baseline4000_0_PoissonSeq.rds"))
baseline4000_0_PoissonSeq_diff_exp <- sum(baseline4000_0_PoissonSeq["prediction"])
baseline4000_0_voom <- convertcompDataToList(readRDS(file.path(myArgs[7], "baseline4000_0_voom.limma.rds")))
baseline4000_0_voom_diff_exp <- nrow(baseline4000_0_voom$result.table[baseline4000_0_voom$result.table$pvalue < 0.05,])
baseline4000_0_df <- data.frame(DESeq2 = c(baseline4000_0_DESeq2_diff_exp),
                                 edgeR = c(baseline4000_0_edgeR_diff_exp),
                                 NOISeq = c(baseline4000_0_NOISeq_diff_exp),
                                 ttest = c(baseline4000_0_ttest_diff_exp),
                                 voom.limma = c(baseline4000_0_voom_diff_exp),
                                 PoissonSeq = c(baseline4000_0_PoissonSeq_diff_exp),
                                 ABSSeq = c(baseline4000_0_ABSSeq_diff_exp))

# #Baseline 2000 2000
baseline2000_2000_ABSSeq <- readRDS(file.path(myArgs[1], "baseline2000_2000_ABSSeq.rds"))
baseline2000_2000_ABSSeq_diff_exp <- sum(baseline2000_2000_ABSSeq["prediction"])
baseline2000_2000_DESeq2 <- convertcompDataToList(readRDS(file.path(myArgs[2], "baseline2000_2000_DESeq2.rds")))
baseline2000_2000_DESeq2_diff_exp <- nrow(baseline2000_2000_DESeq2$result.table[baseline2000_2000_DESeq2$result.table$pvalue < 0.05,])
baseline2000_2000_edgeR <- convertcompDataToList(readRDS(file.path(myArgs[3], "baseline2000_2000_edgeR.exact.rds")))
baseline2000_2000_edgeR_diff_exp<- nrow(baseline2000_2000_edgeR$result.table[baseline2000_2000_edgeR$result.table$pvalue < 0.05,])
baseline2000_2000_NOISeq <- convertcompDataToList(readRDS(file.path(myArgs[4], "baseline2000_2000_NOISeq.rds")))
baseline2000_2000_NOISeq_diff_exp <- nrow(baseline2000_2000_NOISeq$result.table[baseline2000_2000_NOISeq$result.table$probabilities < 0.05,])
baseline2000_2000_ttest <- convertcompDataToList(readRDS(file.path(myArgs[5], "baseline2000_2000_ttest.rds")))
baseline2000_2000_ttest_diff_exp <- nrow(baseline2000_2000_ttest$result.table[baseline2000_2000_ttest$result.table$pvalue < 0.05,])
baseline2000_2000_PoissonSeq <- readRDS(file.path(myArgs[6], "baseline2000_2000_PoissonSeq.rds"))
baseline2000_2000_PoissonSeq_diff_exp <- sum(baseline2000_2000_PoissonSeq["prediction"])
baseline2000_2000_voom <- convertcompDataToList(readRDS(file.path(myArgs[7], "baseline2000_2000_voom.limma.rds")))
baseline2000_2000_voom_diff_exp <- nrow(baseline2000_2000_voom$result.table[baseline2000_2000_voom$result.table$pvalue < 0.05,])
baseline2000_2000_df <- data.frame(DESeq2 = c(baseline2000_2000_DESeq2_diff_exp),
                                edgeR = c(baseline2000_2000_edgeR_diff_exp),
                                NOISeq = c(baseline2000_2000_NOISeq_diff_exp),
                                ttest = c(baseline2000_2000_ttest_diff_exp),
                                voom.limma = c(baseline2000_2000_voom_diff_exp),
                                PoissonSeq = c(baseline2000_2000_PoissonSeq_diff_exp),
                                ABSSeq = c(baseline2000_2000_ABSSeq_diff_exp))

# #Poisson 0 0
poisson0_0_ABSSeq <- readRDS(file.path(myArgs[1], "poisson0_0_ABSSeq.rds"))
poisson0_0_ABSSeq_diff_exp <- sum(poisson0_0_ABSSeq["prediction"])
poisson0_0_DESeq2 <- convertcompDataToList(readRDS(file.path(myArgs[2], "poisson0_0_DESeq2.rds")))
poisson0_0_DESeq2_diff_exp <- nrow(poisson0_0_DESeq2$result.table[poisson0_0_DESeq2$result.table$pvalue < 0.05,])
poisson0_0_edgeR <- convertcompDataToList(readRDS(file.path(myArgs[3], "poisson0_0_edgeR.exact.rds")))
poisson0_0_edgeR_diff_exp<- nrow(poisson0_0_edgeR$result.table[poisson0_0_edgeR$result.table$pvalue < 0.05,])
poisson0_0_NOISeq <- convertcompDataToList(readRDS(file.path(myArgs[4], "poisson0_0_NOISeq.rds")))
poisson0_0_NOISeq_diff_exp <- nrow(poisson0_0_NOISeq$result.table[poisson0_0_NOISeq$result.table$probabilities < 0.05,])
poisson0_0_ttest <- convertcompDataToList(readRDS(file.path(myArgs[5], "poisson0_0_ttest.rds")))
poisson0_0_ttest_diff_exp <- nrow(poisson0_0_ttest$result.table[poisson0_0_ttest$result.table$pvalue < 0.05,])
poisson0_0_PoissonSeq <- readRDS(file.path(myArgs[6], "poisson0_0_PoissonSeq.rds"))
poisson0_0_PoissonSeq_diff_exp <- sum(poisson0_0_PoissonSeq["prediction"])
poisson0_0_voom <- convertcompDataToList(readRDS(file.path(myArgs[7], "poisson0_0_voom.limma.rds")))
poisson0_0_voom_diff_exp <- nrow(poisson0_0_voom$result.table[poisson0_0_voom$result.table$pvalue < 0.05,])
poisson0_0_df <- data.frame(DESeq2 = c(poisson0_0_DESeq2_diff_exp),
                                   edgeR = c(poisson0_0_edgeR_diff_exp),
                                   NOISeq = c(poisson0_0_NOISeq_diff_exp),
                                   ttest = c(poisson0_0_ttest_diff_exp),
                                   voom.limma = c(poisson0_0_voom_diff_exp),
                                   PoissonSeq = c(poisson0_0_PoissonSeq_diff_exp),
                                   ABSSeq = c(poisson0_0_ABSSeq_diff_exp))

# #Poisson 625 625
poisson625_625_ABSSeq <- readRDS(file.path(myArgs[1], "poisson625_625_ABSSeq.rds"))
poisson625_625_ABSSeq_diff_exp <- sum(poisson625_625_ABSSeq["prediction"])
poisson625_625_DESeq2 <- convertcompDataToList(readRDS(file.path(myArgs[2], "poisson625_625_DESeq2.rds")))
poisson625_625_DESeq2_diff_exp <- nrow(poisson625_625_DESeq2$result.table[poisson625_625_DESeq2$result.table$pvalue < 0.05,])
poisson625_625_edgeR <- convertcompDataToList(readRDS(file.path(myArgs[3], "poisson625_625_edgeR.exact.rds")))
poisson625_625_edgeR_diff_exp<- nrow(poisson625_625_edgeR$result.table[poisson625_625_edgeR$result.table$pvalue < 0.05,])
poisson625_625_NOISeq <- convertcompDataToList(readRDS(file.path(myArgs[4], "poisson625_625_NOISeq.rds")))
poisson625_625_NOISeq_diff_exp <- nrow(poisson625_625_NOISeq$result.table[poisson625_625_NOISeq$result.table$probabilities < 0.05,])
poisson625_625_ttest <- convertcompDataToList(readRDS(file.path(myArgs[5], "poisson625_625_ttest.rds")))
poisson625_625_ttest_diff_exp <- nrow(poisson625_625_ttest$result.table[poisson625_625_ttest$result.table$pvalue < 0.05,])
poisson625_625_PoissonSeq <- readRDS(file.path(myArgs[6], "poisson625_625_PoissonSeq.rds"))
poisson625_625_PoissonSeq_diff_exp <- sum(poisson625_625_PoissonSeq["prediction"])
poisson625_625_voom <- convertcompDataToList(readRDS(file.path(myArgs[7], "poisson625_625_voom.limma.rds")))
poisson625_625_voom_diff_exp <- nrow(poisson625_625_voom$result.table[poisson625_625_voom$result.table$pvalue < 0.05,])
poisson625_625_df <- data.frame(DESeq2 = c(poisson625_625_DESeq2_diff_exp),
                            edgeR = c(poisson625_625_edgeR_diff_exp),
                            NOISeq = c(poisson625_625_NOISeq_diff_exp),
                            ttest = c(poisson625_625_ttest_diff_exp),
                            voom.limma = c(poisson625_625_voom_diff_exp),
                            PoissonSeq = c(poisson625_625_PoissonSeq_diff_exp),
                            ABSSeq = c(poisson625_625_ABSSeq_diff_exp))

# #Single 0 0
single0_0_ABSSeq <- readRDS(file.path(myArgs[1], "single0_0_ABSSeq.rds"))
single0_0_ABSSeq_diff_exp <- sum(single0_0_ABSSeq["prediction"])
single0_0_DESeq2 <- convertcompDataToList(readRDS(file.path(myArgs[2], "single0_0_DESeq2.rds")))
single0_0_DESeq2_diff_exp <- nrow(single0_0_DESeq2$result.table[single0_0_DESeq2$result.table$pvalue < 0.05,])
single0_0_edgeR <- convertcompDataToList(readRDS(file.path(myArgs[3], "single0_0_edgeR.exact.rds")))
single0_0_edgeR_diff_exp<- nrow(single0_0_edgeR$result.table[single0_0_edgeR$result.table$pvalue < 0.05,])
single0_0_NOISeq <- convertcompDataToList(readRDS(file.path(myArgs[4], "single0_0_NOISeq.rds")))
single0_0_NOISeq_diff_exp <- nrow(single0_0_NOISeq$result.table[single0_0_NOISeq$result.table$probabilities < 0.05,])
single0_0_ttest <- convertcompDataToList(readRDS(file.path(myArgs[5], "single0_0_ttest.rds")))
single0_0_ttest_diff_exp <- nrow(single0_0_ttest$result.table[single0_0_ttest$result.table$pvalue < 0.05,])
single0_0_PoissonSeq <- readRDS(file.path(myArgs[6], "single0_0_PoissonSeq.rds"))
single0_0_PoissonSeq_diff_exp <- sum(single0_0_PoissonSeq["prediction"])
single0_0_voom <- convertcompDataToList(readRDS(file.path(myArgs[7], "single0_0_voom.limma.rds")))
single0_0_voom_diff_exp <- nrow(single0_0_voom$result.table[single0_0_voom$result.table$pvalue < 0.05,])
single0_0_df <- data.frame(DESeq2 = c(single0_0_DESeq2_diff_exp),
                                edgeR = c(single0_0_edgeR_diff_exp),
                                NOISeq = c(single0_0_NOISeq_diff_exp),
                                ttest = c(single0_0_ttest_diff_exp),
                                voom.limma = c(single0_0_voom_diff_exp),
                                PoissonSeq = c(single0_0_PoissonSeq_diff_exp),
                                ABSSeq = c(single0_0_ABSSeq_diff_exp))

# #Single 625 625
single625_625_ABSSeq <- readRDS(file.path(myArgs[1], "single625_625_ABSSeq.rds"))
single625_625_ABSSeq_diff_exp <- sum(single625_625_ABSSeq["prediction"])
single625_625_DESeq2 <- convertcompDataToList(readRDS(file.path(myArgs[2], "single625_625_DESeq2.rds")))
single625_625_DESeq2_diff_exp <- nrow(single625_625_DESeq2$result.table[single625_625_DESeq2$result.table$pvalue < 0.05,])
single625_625_edgeR <- convertcompDataToList(readRDS(file.path(myArgs[3], "single625_625_edgeR.exact.rds")))
single625_625_edgeR_diff_exp<- nrow(single625_625_edgeR$result.table[single625_625_edgeR$result.table$pvalue < 0.05,])
single625_625_NOISeq <- convertcompDataToList(readRDS(file.path(myArgs[4], "single625_625_NOISeq.rds")))
single625_625_NOISeq_diff_exp <- nrow(single625_625_NOISeq$result.table[single625_625_NOISeq$result.table$probabilities < 0.05,])
single625_625_ttest <- convertcompDataToList(readRDS(file.path(myArgs[5], "single625_625_ttest.rds")))
single625_625_ttest_diff_exp <- nrow(single625_625_ttest$result.table[single625_625_ttest$result.table$pvalue < 0.05,])
single625_625_PoissonSeq <- readRDS(file.path(myArgs[6], "single625_625_PoissonSeq.rds"))
single625_625_PoissonSeq_diff_exp <- sum(single625_625_PoissonSeq["prediction"])
single625_625_voom <- convertcompDataToList(readRDS(file.path(myArgs[7], "single625_625_voom.limma.rds")))
single625_625_voom_diff_exp <- nrow(single625_625_voom$result.table[single625_625_voom$result.table$pvalue < 0.05,])
single625_625_df <- data.frame(DESeq2 = c(single625_625_DESeq2_diff_exp),
                           edgeR = c(single625_625_edgeR_diff_exp),
                           NOISeq = c(single625_625_NOISeq_diff_exp),
                           ttest = c(single625_625_ttest_diff_exp),
                           voom.limma = c(single625_625_voom_diff_exp),
                           PoissonSeq = c(single625_625_PoissonSeq_diff_exp),
                           ABSSeq = c(single625_625_ABSSeq_diff_exp))

# #Random 0 0
random0_0_ABSSeq <- readRDS(file.path(myArgs[1], "random0_0_ABSSeq.rds"))
random0_0_ABSSeq_diff_exp <- sum(random0_0_ABSSeq["prediction"])
random0_0_DESeq2 <- convertcompDataToList(readRDS(file.path(myArgs[2], "random0_0_DESeq2.rds")))
random0_0_DESeq2_diff_exp <- nrow(random0_0_DESeq2$result.table[random0_0_DESeq2$result.table$pvalue < 0.05,])
random0_0_edgeR <- convertcompDataToList(readRDS(file.path(myArgs[3], "random0_0_edgeR.exact.rds")))
random0_0_edgeR_diff_exp<- nrow(random0_0_edgeR$result.table[random0_0_edgeR$result.table$pvalue < 0.05,])
random0_0_NOISeq <- convertcompDataToList(readRDS(file.path(myArgs[4], "random0_0_NOISeq.rds")))
random0_0_NOISeq_diff_exp <- nrow(random0_0_NOISeq$result.table[random0_0_NOISeq$result.table$probabilities < 0.05,])
random0_0_ttest <- convertcompDataToList(readRDS(file.path(myArgs[5], "random0_0_ttest.rds")))
random0_0_ttest_diff_exp <- nrow(random0_0_ttest$result.table[random0_0_ttest$result.table$pvalue < 0.05,])
random0_0_PoissonSeq <- readRDS(file.path(myArgs[6], "random0_0_PoissonSeq.rds"))
random0_0_PoissonSeq_diff_exp <- sum(random0_0_PoissonSeq["prediction"])
random0_0_voom <- convertcompDataToList(readRDS(file.path(myArgs[7], "random0_0_voom.limma.rds")))
random0_0_voom_diff_exp <- nrow(random0_0_voom$result.table[random0_0_voom$result.table$pvalue < 0.05,])
random0_0_df <- data.frame(DESeq2 = c(random0_0_DESeq2_diff_exp),
                               edgeR = c(random0_0_edgeR_diff_exp),
                               NOISeq = c(random0_0_NOISeq_diff_exp),
                               ttest = c(random0_0_ttest_diff_exp),
                               voom.limma = c(random0_0_voom_diff_exp),
                               PoissonSeq = c(random0_0_PoissonSeq_diff_exp),
                               ABSSeq = c(random0_0_ABSSeq_diff_exp))

# #Random 625 625
random625_625_ABSSeq <- readRDS(file.path(myArgs[1], "random625_625_ABSSeq.rds"))
random625_625_ABSSeq_diff_exp <- sum(random625_625_ABSSeq["prediction"])
random625_625_DESeq2 <- convertcompDataToList(readRDS(file.path(myArgs[2], "random625_625_DESeq2.rds")))
random625_625_DESeq2_diff_exp <- nrow(random625_625_DESeq2$result.table[random625_625_DESeq2$result.table$pvalue < 0.05,])
random625_625_edgeR <- convertcompDataToList(readRDS(file.path(myArgs[3], "random625_625_edgeR.exact.rds")))
random625_625_edgeR_diff_exp<- nrow(random625_625_edgeR$result.table[random625_625_edgeR$result.table$pvalue < 0.05,])
random625_625_NOISeq <- convertcompDataToList(readRDS(file.path(myArgs[4], "random625_625_NOISeq.rds")))
random625_625_NOISeq_diff_exp <- nrow(random625_625_NOISeq$result.table[random625_625_NOISeq$result.table$probabilities < 0.05,])
random625_625_ttest <- convertcompDataToList(readRDS(file.path(myArgs[5], "random625_625_ttest.rds")))
random625_625_ttest_diff_exp <- nrow(random625_625_ttest$result.table[random625_625_ttest$result.table$pvalue < 0.05,])
random625_625_PoissonSeq <- readRDS(file.path(myArgs[6], "random625_625_PoissonSeq.rds"))
random625_625_PoissonSeq_diff_exp <- sum(random625_625_PoissonSeq["prediction"])
random625_625_voom <- convertcompDataToList(readRDS(file.path(myArgs[7], "random625_625_voom.limma.rds")))
random625_625_voom_diff_exp <- nrow(random625_625_voom$result.table[random625_625_voom$result.table$pvalue < 0.05,])
random625_625_df <- data.frame(DESeq2 = c(random625_625_DESeq2_diff_exp),
                           edgeR = c(random625_625_edgeR_diff_exp),
                           NOISeq = c(random625_625_NOISeq_diff_exp),
                           ttest = c(random625_625_ttest_diff_exp),
                           voom.limma = c(random625_625_voom_diff_exp),
                           PoissonSeq = c(random625_625_PoissonSeq_diff_exp),
                           ABSSeq = c(random625_625_ABSSeq_diff_exp))

new <- rbind(baseline0_0_df, baseline1250_0_df, baseline625_625_df, baseline4000_0_df, baseline2000_2000_df, poisson0_0_df, poisson625_625_df, single0_0_df, single625_625_df, random0_0_df, random625_625_df)
rownames(new) <- c("baseline0_0", "baseline1250_0", "baseline625_625", "baseline4000_0", "baseline2000_2000", "poisson0_0", "poisson625_625", "single0_0", "single625_625", "random0_0", "random625_625")
new
write.csv(new, file.path(myArgs[8], "num_expressed_by_tool.csv"))