library('cvAUC')

tools <- c('DESeq2', 'edgeR.exact', 'voom.limma', 'ttest', 'PoissonSeq', 'ABSSeq')
data_list <- c('baseline625_625', 'baseline1250_0', 'baseline2000_2000',
               'baseline4000_0', 'random625_625', 'poisson625_625', 'single625_625')

data_0_list <- c('baseline0_0', 'poisson0_0', 'random0_0', 'single0_0')

sample_no <- c('2', '5', '10')
versions <- c('v1', 'v2', 'v3', 'v4', 'v5',
              'v6', 'v7', 'v8', 'v9', 'v10')
m <- matrix(ncol=9, nrow=length(tools)*length(data_list)*length(sample_no)*length(versions))
m0 <- matrix(ncol=5, nrow=length(tools)*length(data_0_list)*length(sample_no)*length(versions))
i<-1w
j<-1
for (tool in tools){
    for (data in data_list) {
        for (sample in sample_no) {
            for (v in versions) {
                dir <- paste(data,sample,sep="_")
                file <- paste(dir,v,paste(tool,"rds",sep="."),sep="_")
                if (tool=='edgeR.exact') {
                    path <- paste("~/RNASeqToolComparison/out",'edgeR',dir,file,sep="/")
                } else {
                    path <- paste("~/RNASeqToolComparison/out",tool,dir,file,sep="/")
                }
                des <- readRDS(path)
                if ((tool != 'ABSSeq') & (tool != 'PoissonSeq')) {
                    des_table <- des@result.table
                    des_df <- as.data.frame(des_table)
                    des_df$prediction <- ifelse(des_df$pval < 0.05, 1, 0)
                    des_df$prediction[is.na(des_df$prediction)] <- 0
                    des_df$actual <- des@variable.annotations$differential.expression
                    des_df$dif <- des_df$prediction - des_df$actual
                } else {
                    des_df <- des
                }
                TOTALP <- sum(des_df$prediction)
                FP <- length(which(des_df$dif == 1))
                FDR <- FP/TOTALP
                TP <- length(which(des_df$actual==1 & des_df$prediction==1))
                TN <- length(which(des_df$actual==0 & des_df$prediction==0))
                N <- length(which(des_df$actual == 0))
                P <- length(which(des_df$actual == 1))
                sensitivity <- TP/P
                specificity <- TN/N
                accuracy <- NROW(which(des_df$dif==0)) / NROW(des_df)
                if (length(unique(des_df$actual)) == 1) {
                    auc <- 'NULL'
                } else {
                    auc <- AUC(des_df$prediction, des_df$actual)
                }
                m[i,] <- c(tool, data, sample, v, FDR, sensitivity, specificity, auc, accuracy)
                i<-i+1
            }
        }
    }
    for (data in data_0_list) {
        for (sample in sample_no) {
            for (v in versions) {
                dir <- paste(data,sample,sep="_")
                file <- paste(dir,v,paste(tool,"rds",sep="."),sep="_")
                if (tool=='edgeR.exact') {
                    path <- paste("~/RNASeqToolComparison/out",'edgeR',dir,file,sep="/")
                } else {
                    path <- paste("~/RNASeqToolComparison/out",tool,dir,file,sep="/")
                }
                des <- readRDS(path)
                if ((tool != 'ABSSeq') & (tool != 'PoissonSeq')) {
                    des_table <- des@result.table
                    des_df <- as.data.frame(des_table)
                    des_df$prediction <- ifelse(des_df$pval < 0.05, 1, 0)
                    des_df$prediction[is.na(des_df$prediction)] <- 0
                    des_df$actual <- des@variable.annotations$differential.expression
                    des_df$dif <- des_df$prediction - des_df$actual
                } else {
                    des_df <- des
                }
                FPR <- sum(des_df$prediction) / NROW(des_df)
                m0[j,] <- c(tool, data, sample, v, FPR)
                j<-j+1
            }
        }
    }
}
colnames(m) <- c('Tool', 'Data', 'Samples per Condition', 'Version', 'FDR', 'Sensitivty', 'Specificity', 'AUC', 'Accuracy')
colnames(m0) <- c('Tool', 'Data', 'Samples per Condition', 'Version', 'False Positive Rate')
write.table(m, 'out/statistics.csv')
write.table(m0, 'out/statistics_0.csv')
