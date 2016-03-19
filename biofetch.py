#!/bin/python
from Bio import Entrez
from pymongo import MongoClient
from Bio import Medline


def updateDBdata(cancer):
	client = MongoClient('mongodb://localhost:27017/')
	db = client['minepm']
	Entrez.email = "garganom@my.easternct.edu"    # Always tell NCBI who you are
	if(cancer == "bladder"):
		handle = Entrez.esearch(db="pubmed", term="bladder cancer", retmax=10000)
		collection = db.bladdercancer
	elif(cancer == "lung"):
		handle = Entrez.esearch(db="pubmed", term="lung cancer")
		collection = db.lungcancer
	elif(cancer == "prostate"):
		handle = Entrez.esearch(db="pubmed", term="prostate cancer")
		collection = db.prostatecancer	
	
	record = Entrez.read(handle)
	idlist = record["IdList"]	
	handle = Entrez.efetch(db="pubmed", rettype="medline", id=idlist, retmax=10000,retmode="xml")
	records = Entrez.parse(handle)	
	for x in records:
		try:
			pmid = x['MedlineCitation']['PMID']
			title = x['MedlineCitation']['Article']['ArticleTitle']
			abstract = x['MedlineCitation']['Article']['Abstract']['AbstractText']
			item  = {"pmid": pmid,"title":title,"ab": abstract}
			collection.insert(item)
		
		except Exception,e:
		#print "\n" 
		#print x["MedlineCitation"]["Abstract"]["AbstractText"]
		#print abstract
			continue
		
		
		
	handle.close()
	client.close()



def main():
	updateDBdata("bladder")
	
	

if __name__ == "__main__":
	main()
	
