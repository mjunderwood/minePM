import xml.etree.ElementTree as ET
import re
import csv
from pymongo import MongoClient

def extractGeneData(cancer,gene_dict):
    #open db connection,get the cancer collection
    #loop through collection
    #Do original analysis
    client = MongoClient('mongodb://localhost:27017/')
    db = client['minepm']
 	
    if(cancer == "bladder"):
           collection = db.bladdercancer.find()
    elif(cancer == "lung"):
           collection = db.lungcancer.find()
    elif(cancer == "prostate"):
           collection = db.prostatecancer.find()
    for x in collection:    
      abstract = line.split(",")
      abstract = list(abstract) 
      uid = uid.split("\n")
      uid = filter(bool,uid) 
      x = len(abstract) 
      for i in range(0,x):	
        word = str(abstract[i]).strip()
        try:
          valueMatch = gene_dict[word]
          if (valueMatch != 0): 
	    if(word == "TP53"):
		print valueMatch
            valueMatch[0] = valueMatch[0] + 1
            valueMatch.append(uid[0]) 
	    gene_dict[word] = valueMatch
          else: 
	    newlist = []
            newlist.append(1)
            newlist.append(uid[0])	     
            gene_dict[word] = newlist
        except Exception, e:
          continue   
    return gene_dict


def returnGeneList():
    with open('./data/genes.txt','rb') as csvfile:
        genereader = csv.reader(csvfile,delimiter='\n')
        genesym = []
        for row in genereader:
           row = ''.join(row)
           genesym.append(row) 
        genesym.pop(0)
        return genesym

def writecsv(data):
    csvfile = "./matrix-test.csv"
    with open(csvfile, "w") as output:
      writer = csv.writer(output, lineterminator='\n')
      writer.writerows(data)

def reset_dict():
  gene = returnGeneList();
  gene_dict = {}
  for  i in range(0,len(gene)):
    gene_dict[str(gene[i])] = 0
  return gene_dict

    
def main():
    # Define Matrix (col)(row)
    #39825
    Matrix = [[ x for x in range(3)] for x in range(39825)]
    Matrix[0][0] = "GeneSymbol"
    Matrix[0][1] = "BladderCount"
    Matrix[0][2] = "ArticleIds"
   #Matrix[0][2] = "Lung Count"
    #Matrix[0][3] = "Brain Count"
    # Conduct the mining and inserting of the matrix.
    #39824 
    print "Mining gene symbols"
    gene_dict = reset_dict()
    bladder = extractGeneData("bladder cancer",gene_dict) 
    count = 0
    for key, value in bladder.iteritems():
      count = count + 1
      if(value != 0): 
        Matrix[count][0] = key
        Matrix[count][1] = value[0]
        Matrix[count][2] =",".join(value[1:])
      else:
        Matrix[count][0] = key
        Matrix[count][1] = 0
        Matrix[count][2] = "None"
    if(False):
      gene_dict = reset_dict()
      lung =  extractGeneData("./big-data/lung-data.txt","Lung Cancer",gene_dict)
      count = 0
      for key,value in lung.iteritems():
        count = count + 1
        Matrix[count][2] = value

      gene_dict = reset_dict()
      brain = extractGeneData("./big-data/brain-data.txt","Brain Cancer",gene_dict)
      count = 0 
      for key,value in brain.iteritems():   
        count = count + 1
        Matrix[count][3] = value
    

    writecsv(Matrix)
    print "Wrote Matrix to file in /big-data: Matrix.csv"


main()
