from Bio import Entrez
from Bio import Medline

# This files extracts information from Pubmed and puts them into files

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

### loop through each batch. There is a limit to efetch 
        start = 0
        
        
        while start < len(idlistAll):

                filename2 = filename + str(start) + ".txt"      #Creates file names
                f = open(filename2, "w")                        #Opens them
                
                batchSize = 2000

                end = start + batchSize
                if end > len(idlistAll) + 1 :
                        end = len(idlistAll) + 1     #Creates the batches
                        
                idlist = idlistAll[start:end]
                
                
                handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text") #
                records = Medline.parse(handle)                                                   # Extracts the info from pubmed
                records = list(records) #all pmids are in this list
                
                for record in records:	#print record
                  #  print "Article #", count
                  #  print "PMID: ", record.get("PMID", "?") 
                  #  print "title:", record.get("TI", "?")
                  #  print "authors:", record.get("AU", "?")           
                  #  print "source:", record.get("SO", "?")           
                  #  count = count + 1
                    s = ", "
                    authors = s.join(record.get("AU", "?"))
                    f.write("PMID: " + record.get("PMID", "?") + "\t")
                    f.write("Title: " + record.get("TI", "?")+ "\t")
                    f.write("Authors: " + authors + "\t")                       #writes the title, author, 
                    f.write("Source: " + record.get("SO", "?")+ "\t")           #source and abstract to a file
                    f.write("Abstract: " + record.get("AB", "?")+ "\n")
                     
                print ("Batch starting at " + str(start) + " is complete")  
                
                start = start + batchSize    #moves to next batch
        handle.close()
        f.close

