if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("ABSSeq")

library(ABSSeq)

all_data <- c('baseline0_0', 'baseline1250_0', 'baseline2000_2000', 'baseline4000_0',
              'baseline625_625', 'poisson0_0','poisson625_625', 'random0_0',
              'random625_625', 'single0_0')

indir <- "data"
outdir <- "out/ABSSeq"
tool <- 'ABSSeq'
sample_no <- c('5')
versions <- c('v1', 'v2', 'v3', 'v4', 'v5',
              'v6', 'v7', 'v8', 'v9', 'v10')

for (data in all_data) {
    for (sample in sample_no) {
        for (v in versions) {
            file <- paste(data, sample, paste(v,'.rds',sep=""), sep="_")
            #reformat compcode data to work for PoissonSeq
            path <- paste("~/RNASeqToolComparison",indir,data,file,sep="/")
            temp_data <- readRDS(path)
            groups <- c(1,1,1,1,1,2,2,2,2,2)
            absdata <- ABSDataSet(temp_data@count.matrix, groups)
            
            obj <- ABSSeq(absdata, useaFold=TRUE)
            abs_res <- results(obj,c("Amean","Bmean","foldChange","pvalue","adj.pvalue"))
            
            labels <- matrix(c(temp_data@variable.annotations$differential.expression, c(1:NROW(temp_data@count.matrix))), ncol=2)
            colnames(labels) <- c("actual", "gene_number")
            abs_res <- cbind(gene = rownames(abs_res), abs_res)
            rownames(abs_res) <- 1:nrow(abs_res)
            abs_res <- cbind(gene_number = rownames(abs_res), abs_res)
            rownames(abs_res) <- 1:nrow(abs_res)
            results <- merge(x=labels, y=abs_res, by="gene_number",all.x=TRUE)
            result_df <- as.data.frame(results)
            result_df$prediction <- ifelse(result_df$adj.pval < 0.05, 1, 0)
            result_df$prediction[is.na(result_df$prediction)] <- 0
            result_df$dif <- abs(result_df$actual - result_df$prediction)
            result_df <- result_df[c("gene","Amean","Bmean","foldChange","pvalue","adj.pvalue","actual","prediction","dif")]
            
            filename <- paste(data,"_",sample,"_",v,"_",tool,".rds",sep="")
            out <- paste("~/RNASeqToolComparison", outdir, filename,  sep="/")
            saveRDS(result_df, out)
        }
    }
}




data <- dat
#reformat compcode data to work for PoissonSeq
path <- paste("~/RNASeqToolComparison",indir,data, sep="/")
temp_data <- readRDS("~/RNASeqToolComparison/data/test.rds")
groups <- c(1,1,1,1,1,2,2,2,2,2)
absdata <- ABSDataSet(temp_data@count.matrix, groups)

obj <- ABSSeq(absdata, useaFold=TRUE)
abs_res <- results(obj,c("Amean","Bmean","foldChange","pvalue","adj.pvalue"))

labels <- matrix(c(temp_data@variable.annotations$differential.expression, c(1:NROW(temp_data@count.matrix))), ncol=2)
colnames(labels) <- c("actual", "gene_number")
abs_res <- cbind(gene = rownames(abs_res), abs_res)
rownames(abs_res) <- 1:nrow(abs_res)
abs_res <- cbind(gene_number = rownames(abs_res), abs_res)
rownames(abs_res) <- 1:nrow(abs_res)
results <- merge(x=labels, y=abs_res, by="gene_number",all.x=TRUE)
result_df <- as.data.frame(results)
result_df$prediction <- ifelse(result_df$adj.pval < 0.05, 1, 0)
result_df$prediction[is.na(result_df$prediction)] <- 0
result_df$dif <- abs(result_df$actual - result_df$prediction)
result_df <- result_df[c("gene","Amean","Bmean","foldChange","pvalue","adj.pvalue","actual","prediction","dif")]

filename <- paste(substr(data, 0, nchar(data)-4),"_", tool, ".rds",sep="")
out <- paste("~/RNASeqToolComparison", outdir, filename,  sep="/")
saveRDS(result_df, out)