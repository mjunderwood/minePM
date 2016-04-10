#!/bin/python

## OLD SCRIPT TO FETCH AND INSERT
## THERE ARE 500 Internal Errors that exist here so we will first 
## fetch the files and store locally, checking for the 500 error
## this script is in case they fix this.


from Bio import Entrez
from pymongo import MongoClient
from Bio import Medline
import logging

def updateDBdata(cancer):
	client = MongoClient('mongodb://localhost:27017/')
	db = client['minepm']
	Entrez.email = "garganom@my.easternct.edu"    # Always tell NCBI who you are
	if(cancer == "bladder"):
		handle = Entrez.esearch(db="pubmed", term="\"bladder cancer\"", retmax=1000000)
		collection = db.bladdercancer
	elif(cancer == "lung"):
		handle = Entrez.esearch(db="pubmed", term="\"lung cancer\"", retmax=10000)
		collection = db.lungcancer
	elif(cancer == "prostate"):
		handle = Entrez.esearch(db="pubmed", term="\"prostate cancer\"",retmax=10000)
		collection = db.prostatecancer	
	
	record = Entrez.read(handle)
	idlist = record["IdList"]
	logging.warning(str(len(idlist)))
	i = 1 
	count = 0
	for i in range(0,len(idlist),200):	
		handle = Entrez.efetch(db="pubmed", retmode="XML",rettype="", id=idlist[i:i+200],retstart=1, retmax=200)

	
		records = Entrez.parse(handle)	
		for x in records:	
			try:
			
				pmid = x['MedlineCitation']['PMID']
				title = x['MedlineCitation']['Article']['ArticleTitle']
				abstract = x['MedlineCitation']['Article']['Abstract']['AbstractText']
				item  = {"pmid": pmid,"title":title,"ab": abstract}
				collection.insert(item)
				
			
			except Exception,e:
				continue

			count = count + 1

		logging.warning("Count is equal to " + str(count))
		handle.close()
	


	client.close()


		
	
def main():
	updateDBdata("bladder")
	
	

if __name__ == "__main__":
	main()
	
