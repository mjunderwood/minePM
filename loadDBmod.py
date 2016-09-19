from Bio import Entrez
from Bio import Medline

searchTerm = raw_input("Enter cancer type")
filename = ArticleInfo.txt
def getCancerData(searchTerm , filename)
    f = open(filename, "w")
    Entrez.email = "underwoodmi@my.easternct.edu"     # Always tell NCBI who you are
    handle = Entrez.egquery(term= searchTerm)
    record = Entrez.read(handle)
    for row in record["eGQueryResult"]:
        if row["DbName"]=="pubmed":
            print(row["Count"])         #prints number of articles

    handle = Entrez.esearch(db="pubmed", term = searchTerm, retmax=row["Count"])
    record = Entrez.read(handle)
    idlist = record["IdList"]


    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",
                           retmode="text")
    records = Medline.parse(handle)

    records = list(records) #all pmids are in this list

    for record in records:
        f.write("PMID:" , idlist[record])
        f.write("title:", record.get("TI", "?"))
        f.write("authors:", record.get("AU", "?"))            #writes the title, author, 
        f.write("source:", record.get("SO", "?"))           #source and abstract to a file
        f.write("abstract:", record.get("AB", "?")
        
    handle.close()
f.close()
