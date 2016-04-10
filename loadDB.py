#!/bin/python
from Bio import Entrez
from pymongo import MongoClient
from Bio import Medline
import logging
import os

def updateDBdata(cancer):
	client = MongoClient('mongodb://localhost:27017/')
	db = client['minepm']
	Entrez.email = "garganom@my.easternct.edu"    # Always tell NCBI who you are
	if(cancer == "bladder"):
		collection = db.bladdercancer
		dir = './records/bc/'
	elif(cancer == "lung"):
		collection = db.lungcancer
		dir = "./records/lc/"
	elif(cancer == "prostate"):
		collection = db.prostatecancer	
		dir = "./records/pc/"
	elif(cancer == "colon"):
		collection = db.coloncancer
		dir = "./records/colc/"
	elif(cancer == "pancreatic"):
		collection = db.pancreaticcancer
		dir = "./records/panc/"
	for f in os.listdir(dir):
		print f
		handle = open(dir + f,'r')
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
	        handle.close()



	client.close()


		
	
def main():
	updateDBdata("pancreatic")
	
	

if __name__ == "__main__":
	main()
	
