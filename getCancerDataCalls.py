execfile("loadDBMod.py")
from Bio import Entrez
from Bio import Medline


email = "underwoodmi@my.easternct.edu"
bladderCancer = "bladder cancer"
pancreaticCaner = "pancreatic cancer"
lungCancer = "lung cancer"

getCancerData(bladderCancer , "bladder.txt", email)
getCancerData(pancreaticCancer , "pancreatic.txt", email)
getCancerData(lungCancer , "lung.txt", email)
