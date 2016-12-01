
if(!exists("getGeneList", mode = "function")){
  source("C:/Users/Mike/Desktop/Fall 2016/Independent study/gene.R")
}

if(!exists("getArticleList", mode = "function")){
  source("C:/Users/Mike/Desktop/Fall 2016/Independent study/combineFiles.R")
}

if(!exists("filter_by_gene", mode = "function")){
  source("C:/Users/Mike/Desktop/Fall 2016/Independent study/Match Genes.R")
}

##########################################################
#Gene T is causing us to get every article while filtering.
##########################################################

genes = getGeneList()

bladder.data = getArticleList("bladder")

pancreatic.data = getArticleList("pancreatic")

lung.data = getArticleList("lung")

filtered.bladder = filter_by_gene(bladder.data, genes)
write.table(filtered.bladder, file = "C:/Users/Mike/Desktop/Fall 2016/Independent study/filtered.bladder.txt", sep = "\t")

filtered.pancreatic = filtgener_by_e(pancreatic.data, genes)
write.table(filtered.pancreatic, file = "C:/Users/Mike/Desktop/Fall 2016/Independent study/filtered.pancreatic.txt", sep = "\t")

filtered.lung = filter_by_gene(lung.data, genes)
write.table(filtered.lung, file = "C:/Users/Mike/Desktop/Fall 2016/Independent study/filtered.lung.txt", sep = "\t")



