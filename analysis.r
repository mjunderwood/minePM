##############################
#
# minePM Analysis R script
# 
# Michael Gargano 
#################################
# get data from csv file
data = read.csv("~/develop/minePM/matrix.csv")
#remove insignificant values
data = data.frame(data[data$BladderCancer>=3 & data$LungCancer >=3 & data$ProstateCancer >=3 & data$ColonCancer >= 3 & data$PancreaticCancer >=3,])

#################################################################
# Creating dataframe of sum counts
data.sum = apply(data[,2:6],1,sum) #Sum total Amounts
data.match = data.frame(data[,1],data.sum) # match genename with total counts
#data.top = subset(data.match,data.match[,1] >=3) # subset the data to greater than sum 3
colnames(data.match) <- c("GeneSymbol","TotalCount")
#################################################################



#################################################################
#DENDROGRAM OF TOP 10 Most Hit GENES
data.top.sorted = data.match[order(data.match[,2],data.match[,1],decreasing=TRUE),]
top.25.genes = data.top.sorted[1:10,1]
m = match(top.25.genes, data[,1])
d <- dist(data[m,2:6], method = "euclidean") # distance matrix
fit <- hclust(d, method="ward.D2") 
plot(fit,labels = data[m,1]) # display dendogram
################################################################

################################################################
#DENDROGRAM FOR CANCER TYPES distance based
#function for clustering
plot.clust <-function(x) {
  d = dist(t(x))
  print(d)
  h = hclust(d)
  plot(h)
}
#CLuster shows which cancer types are most similar
plot.clust(data[,2:6])

################################################################


#create and transpose matrix for fisher test
mt = matrix(c(data$BladderCount,data$LungCount,data$ProstateCount), ncol = 3, byrow = FALSE)
mt = t(m)

#fisher test function
f <- function(r){
  x = r[1]
  y = r[2]
  z = r[3]
  mm = matrix(c(x,20000-x, 
               y, 20000 - y,
               z, 20000 - z ),nrow = 3, byrow = TRUE)
  
  f = fisher.test(mm, workspace = 800000,hybrid = TRUE)
  
  return (f$p.value)
}

#apply fisher test to entire matrix
fisher.p = apply(mt,2,f)

#add back gene symbol names and pull out top 5 genes based on fisher.p value
fisher.frame = data.frame(data1$Gene.Symbol, fisher.p)
fisher.frame = fisher.frame[order(-fisher.frame$fisher.p),]
mtch = match(fisher.frame$data1.Gene.Symbol[1:5],data1$Gene.Symbol)
data1[mtch,]

#ATTEMPTED BOXPLOT NoT SURE IF THIS IS WORKING RIGHT
boxplot(data1[mtch,2:4])

#Pull out bottom five genes
fisher.frame = fisher.frame[order(fisher.frame$fisher.p),]
mtch = match(fisher.frame$data1.Gene.Symbol[1:5],data1$Gene.Symbol)
data1[mtch,]
#plot shows extreme differences between hits across these
barplot(t(as.matrix(data1[mtch,2:4])),xlab = "Gene Symbol", 
        col =c("red","green","blue"),names.arg = data[mtch,1], legend=colnames(data1[,2:4]), beside=TRUE)



data1 = data1[order(data1[,2],decreasing = TRUE),]






#data.sum = apply(as.integer(data1[2:4]),1,sum)
data.sum = apply(data1[,2:4],1,sum)
data2 = data.frame(data.sum, row.names = data1[,1])
pct = round(data.sum/sum(data.sum) * 100)
lbls <- paste(data1[0,],pct)
lbls <- paste(pct,"%",sep="") # ad % to labels 

pie(data.sum,labels = lbls,main="Word Proportions over 3 documents")








