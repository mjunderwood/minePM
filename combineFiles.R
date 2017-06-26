#Combines file from loadDBmod edit file.

getArticleList <-function(cancerType){

link = paste0("C:/Users/Mike/Desktop/Fall 2016/Independent study/",cancerType,"*.txt", collapse = "") 

cancer.files = Sys.glob(link)

all.cancer.files = lapply(cancer.files, read.delim, header = FALSE, quote = "")

all.cancer.files = do.call("rbind",all.cancer.files)

return(all.cancer.files)

}


