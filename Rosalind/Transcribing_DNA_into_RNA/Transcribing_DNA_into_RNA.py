file = open(r'C:\Users\Francis\Documents\Directory\Python\rosalind_dna.txt', 'r')   
dnaSequence = file.read()

rnaSequence = dnaSequence.replace("T", "U"); print rnaSequence
