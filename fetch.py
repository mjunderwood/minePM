import urllib2  # to read file from url
from Bio import Entrez
import logging
import time,subprocess,os
from urllib2 import HTTPError

Entrez.email = "garganom@easternct.edu"     # Always tell NCBI who you are

handle = Entrez.esearch(db="pubmed", term="\pancreatic cancer\"", retmax=25000)
record = Entrez.read(handle)

idlist = record["IdList"]
#start = 13401
#end = start + 201
# can do below for each id 
# get handle which is handle to url
fileNum = 1
end = len(idlist) + 200
#end = 22601

for i in range(0,end,200):
	slice = idlist[i:i+200]
	for attempt in range(10):
		try:
			handle = Entrez.efetch(db="pubmed", retmode="XML",rettype = "", id=",".join(slice),retstart=1,retmax=200)
			xml = urllib2.urlopen(handle.url)
			text = xml.read() # convert contents to string
		  
			# save to file BC_#.xml
			fileName = "./records/panc/PRC_"+str(fileNum)+".xml"
			f = open(fileName, "w")
			f.write(text)
			f.close()
			line = subprocess.check_output(['tail', '-1', fileName])[0:-1]
			if(line == "</html>"):
				os.remove(fileName)
				raise NameError('Error 500 during write')	
			logging.warning("Success " + str(fileNum))
			fileNum = fileNum + 1
			handle.close()
			break
		 	
		except (HTTPError,NameError),e:
			logging.warning(e)
			handle.close()
			time.sleep(5)
			continue
	
