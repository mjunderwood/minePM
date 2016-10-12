from Bio import Entrez
from Bio import Medline

def getCancerData(searchTerm , filename, email):
        
        Entrez.email = email     # Always tell NCBI who you are
        handle = Entrez.egquery(term= searchTerm)
        record = Entrez.read(handle)

               
        idlistAll = 0
        for row in record["eGQueryResult"]:
            if row["DbName"]=="pubmed":
                print(row["Count"])         #prints number of articles     
        retmax = int(row["Count"])

        
        
        handle = Entrez.esearch(db="pubmed", term = searchTerm, retmax=retmax)
        record = Entrez.read(handle)
        idlistAll = record["IdList"]

### loop through each batch
        start = 0
        
        
        while start < len(idlistAll):

                filename2 = filename + str(start) + ".txt"
                f = open(filename2, "w")
                
                batchSize = 2000

                end = start + batchSize
                if end > len(idlistAll) + 1 :
                        end = len(idlistAll) + 1
                        
                idlist = idlistAll[start:end]
                
                
                handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
                records = Medline.parse(handle)
                records = list(records) #all pmids are in this list
                
                for record in records:	#print record
                  #  print "Article #", count
                  #  print "PMID: ", record.get("PMID", "?") 
                  #  print "title:", record.get("TI", "?")
                  #  print "authors:", record.get("AU", "?")           #writes the title, author, 
                  #  print "source:", record.get("SO", "?")           #source and abstract to a file
                  #  count = count + 1
                    s = ", "
                    authors = s.join(record.get("AU", "?"))
                    f.write("PMID: " + record.get("PMID", "?") + "\t")
                    f.write("Title: " + record.get("TI", "?")+ "\t")
                    f.write("Authors: " + authors + "\t")                       #writes the title, author, 
                    f.write("Source: " + record.get("SO", "?")+ "\t")           #source and abstract to a file
                    f.write("Abstract: " + record.get("AB", "?")+ "\n")
                     
                print ("Batch starting at " + str(start) + " is complete")  
                
                start = start + batchSize
        handle.close()
        f.close

