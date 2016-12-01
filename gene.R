
getGeneList <- function(){
  
gene.list <- read.delim("C:/Users/Mike/Desktop/Fall 2016/Independent study/gene list.txt")

Approved.Symbols = gene.list$Approved.Symbol

gene_groups_list = list()
listNum = 1
i = 1
while (i < length(Approved.Symbols)) {
  start = i
  end = i + 2499
  
  if (end > length(Approved.Symbols)) {
    end = length(Approved.Symbols)
  }
  
  gene_groups_list[[listNum]] = Approved.Symbols[start:end]
  listNum = listNum + 1
  i = end+1
  
}

rm(list =c("Approved.Symbols"))
return(gene_groups_list = lapply(gene_groups_list,paste, collapse = "|"))

}
