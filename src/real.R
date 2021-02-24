myArgs <- commandArgs(trailingOnly = TRUE)

library('magrittr')
library('dplyr')
library('compcodeR')

in_dir <- myArgs[1]

gene_matrix <- read.csv(file.path(in_dir, "gene_matrix.csv"))
annotations <- read.csv(file.path(in_dir, "SraRunTable.csv"))

valids <- colnames(gene_matrix)
valids <- valids[-1]

annotations <- annotations[annotations$Run %in% valids, ]

# Real dataset divided by different clinical diagnosis
schizo <- annotations[(annotations[, "clinical_diagnosis"] == 'Control' | annotations[, "clinical_diagnosis"] == 'Schizophrenia'),]
mdd <- annotations[(annotations[, "clinical_diagnosis"] == 'Control' | annotations[, "clinical_diagnosis"] == 'Major Depression'),]
bipolar <- annotations[(annotations[, "clinical_diagnosis"] == 'Control' | annotations[, "clinical_diagnosis"] == 'Bipolar Disorder'),]

# Create gene matrixes for each clinical diagnosis
schizo_gene <- gene_matrix %>% select(schizo$Run)
mdd_gene <- gene_matrix %>% select(mdd$Run)
bipolar_gene <- gene_matrix %>% select(bipolar$Run)

# First, try to run each with only condition and gene name
# schizo_annotation <- data.frame(schizo$clinical_diagnosis)
# row.names(schizo_annotation) <- schizo$Run
# colnames(schizo_annotation) <- "condition"

# mdd_annotation <- data.frame(mdd$clinical_diagnosis)
# row.names(mdd_annotation) <- mdd$Run
# colnames(mdd_annotation) <- "condition"

# bipolar_annotation <- data.frame(bipolar$clinical_diagnosis)
# row.names(bipolar_annotation) <- bipolar$Run
# colnames(bipolar_annotation) <- "condition"

# Try more stuff
schizo_annotation <- data.frame(schizo$clinical_diagnosis, schizo$age_at_death, schizo$Brain_pH)
row.names(schizo_annotation) <- schizo$Run
schizo_annotation <- schizo_annotation %>% rename(condition = schizo.clinical_diagnosis, age_at_death = schizo.age_at_death, Brain_pH = schizo.Brain_pH)

mdd_annotation <- data.frame(mdd$clinical_diagnosis, mdd$age_at_death, mdd$Brain_pH)
row.names(mdd_annotation) <- mdd$Run
mdd_annotation <- mdd_annotation %>% rename(condition = mdd.clinical_diagnosis, age_at_death = mdd.age_at_death, Brain_pH = mdd.Brain_pH)

bipolar_annotation <- data.frame(bipolar$clinical_diagnosis, bipolar$age_at_death, bipolar$Brain_pH)
row.names(bipolar_annotation) <- bipolar$Run
bipolar_annotation <- bipolar_annotation %>% rename(condition = bipolar.clinical_diagnosis, age_at_death = bipolar.age_at_death, Brain_pH = bipolar.Brain_pH)

# Create an info parameters for each condition
schizo_info <- list(dataset = "schizo", uID = "1000000000")
mdd_info <- list(dataset = "mdd", uID = "1000000001")
bipolar_info <- list(dataset = "bipolar", uID = "1000000002")

# Create the compCodeR objects
schizo_object <- compData(schizo_gene, schizo_annotation, schizo_info)
mdd_object <- compData(mdd_gene, mdd_annotation, mdd_info)
bipolar_object <- compData(bipolar_gene, bipolar_annotation, bipolar_info)

# Save the objects to a .rds file
saveRDS(schizo_object, file = file.path(in_dir, "schizo.rds"))
saveRDS(mdd_object, file = file.path(in_dir, "mdd.rds"))
saveRDS(bipolar_object, file = file.path(in_dir, "bipolar.rds"))

print("Successfully created the rds file for the real dataset. Ready to implement tools on real datasets")
print("-----------------------------------")