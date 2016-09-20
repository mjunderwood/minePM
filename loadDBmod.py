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
    retmax = 200 

    handle = Entrez.esearch(db="pubmed", term = searchTerm, retmax=retmax)
    record = Entrez.read(handle)
    idlist = record["IdList"]

    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",
                           retmode="text")
    records = Medline.parse(handle)

    records = list(records) #all pmids are in this list

    count = 1
    for record in records:

	#print record

	print "Article #", count
	print "PMID: ", record.get("PMID", "?") 
        print "title:", record.get("TI", "?")
        print "authors:", record.get("AU", "?")           #writes the title, author, 
        print "source:", record.get("SO", "?")           #source and abstract to a file
	
	count = count + 1
        f.write("PMID: " + record.get("PMID", "?"))
        f.write("title: " + record.get("TI", "?"))
        f.write("authors: " + record.get("AU", "?"))            #writes the title, author, 
        f.write("source: " + record.get("SO", "?"))           #source and abstract to a file
        f.write("abstract: " + record.get("AB", "?"))
        
    handle.close()
    f.close()
