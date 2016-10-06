from Bio import Entrez
from Bio import Medline

def getCancerData(searchTerm , filename, email) :
    f = open(filename, "w")
    Entrez.email = email     # Always tell NCBI who you are
    handle = Entrez.egquery(term= searchTerm)
    record = Entrez.read(handle)
    for row in record["eGQueryResult"]:
        if row["DbName"]=="pubmed":
            print(row["Count"])         #prints number of articles

 
    retmax = row["Count"]
    retmax = 300000 

    handle = Entrez.esearch(db="pubmed", term = searchTerm, retmax=retmax)
    record = Entrez.read(handle)
    idlist = record["IdList"]

    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",
                           retmode="text")
    records = Medline.parse(handle)

    records = list(records) #all pmids are in this list

    for record in records:
	s = ", "
	authors = s.join(record.get("AU", "?"))
	count = count + 1
        f.write("PMID: " + record.get("PMID", "?"))
        f.write("Title: " + record.get("TI", "?"))
        f.write("Authors: " + authors)                        #writes the title, author, 
        f.write("Source: " + record.get("SO", "?"))           #source and abstract to a file
        f.write("Abstract: " + record.get("AB", "?"))
        
    handle.close()
    f.close()
