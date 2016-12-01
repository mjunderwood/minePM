
filter_by_gene <- function(pubMed, genes) {
  t1 = Sys.time()
  
  pubMed.titles = pubMed$V2
  pubMed.abstracts = pubMed$V5
  
  fixed.pubMed.titles =  sapply(pubMed.titles , as.character)
  fixed.pubMed.abstracts = sapply(pubMed.abstracts , as.character)
  
  s = paste(fixed.pubMed.titles, fixed.pubMed.abstracts)  
  
  s = strsplit(s, " ")
  s = lapply(s, unique)
  s = sapply(s, paste, collapse = " ")
  s = unlist(s)
  
  pubMed.indicies = vector(mode = "logical", length = 0)
 
    for(i in 1:length(genes)){
      indicies = grep(genes[[i]],s)
      pubMed.indicies = c(pubMed.indicies,indicies)
    }
    
    pubMed.indicies = unique(pubMed.indicies)
  
    t2 = Sys.time()
      
    print(t2-t1)
    
    return(pubMed[pubMed.indicies,])
  
}

