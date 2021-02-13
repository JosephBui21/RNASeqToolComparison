install.packages("PoissonSeq")
library("PoissonSeq")

all_data <- c('baseline0_0', 'baseline1250_0', 'baseline2000_2000', 'baseline4000_0',
              'baseline625_625', 'poisson0_0','poisson625_625', 'random0_0',
              'random625_625', 'single0_0')

indir <- "data"
outdir <- "out/PoissonSeq"
tool <- 'PoissonSeq'
sample_no <- c('5')
versions <- c('v1', 'v2', 'v3', 'v4', 'v5',
              'v6', 'v7', 'v8', 'v9', 'v10')

for (data in all_data) {
  for (sample in sample_no) {
    for (v in versions) {
      file <- paste(data, sample, paste(v,'.rds',sep=""), sep="_")
      #reformat compcode data to work for PoissonSeq
      path <- paste("~/RNASeqToolComparison",indir,data,file, sep="/")
      temp_data <- readRDS(path)
      n <- temp_data@count.matrix
      y <- c(1,1,1,1,1,2,2,2,2,2)
      type <-'twoclass'
      pair <- FALSE
      transformed_data <- list(n=n, y=y, type=type, pair=pair)
      pois_res <- PS.Main(transformed_data)
      ordered_pois_res <- pois_res[order(pois_res['gname'], decreasing=FALSE),]
      
      labels <- matrix(c(temp_data@variable.annotations$differential.expression, c(1:NROW(n))), ncol=2)
      colnames(labels) <- c("actual", "gene_number")
      results <- merge(x=labels, y=pois_res, by.x="gene_number", by.y="gname", all.x=TRUE)
      result_df <- as.data.frame(results)
      
      result_df$prediction <- ifelse(result_df$pval < 0.05, 1, 0)
      
      result_df$prediction[is.na(result_df$prediction)] <- 0
      
      result_df$dif <- abs(result_df$actual - result_df$prediction)
      
      
      filename <- paste(data,"_",sample,"_",v,"_",tool,".rds",sep="")
      out <- paste("~/RNASeqToolComparison", outdir, filename,  sep="/")
      saveRDS(result_df, out)
    }
  }
}




data <- 'poisson0_0.rds'
#reformat compcode data to work for PoissonSeq
path <- paste("~/RNASeqToolComparison",indir,data, sep="/")
temp_data <- readRDS(path)
n <- temp_data@count.matrix
y <- c(1,1,1,1,1,2,2,2,2,2)
type <-'twoclass'
pair <- FALSE
transformed_data <- list(n=n, y=y, type=type, pair=pair)
pois_res <- PS.Main(transformed_data)
ordered_pois_res <- pois_res[order(pois_res['gname'], decreasing=FALSE),]

labels <- matrix(c(temp_data@variable.annotations$differential.expression, c(1:NROW(n))), ncol=2)
colnames(labels) <- c("actual", "gene_number")
results <- merge(x=labels, y=pois_res, by.x="gene_number", by.y="gname", all.x=TRUE)
result_df <- as.data.frame(results)

result_df$prediction <- ifelse(result_df$pval < 0.05, 1, 0)

result_df$prediction[is.na(result_df$prediction)] <- 0

result_df$dif <- abs(result_df$actual - result_df$prediction)


filename <- paste(substr(data, 0, nchar(data)-4),"_", tool, ".rds",sep="")
out <- paste("~/RNASeqToolComparison", outdir, filename,  sep="/")
saveRDS(result_df, out)
