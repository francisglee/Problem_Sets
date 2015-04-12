file = open(r'C:\Users\Me\Documents\Directory\Python\rosalind_dna.txt', 'r')
dnaSequence = file.read()

aCount = 0
cCount = 0
tCount = 0
gCount = 0

for c in dnaSequence:
    if c == 'A':
        aCount = aCount + 1
    elif c == 'C':
        cCount = cCount + 1
    elif c == 'T':
        tCount = tCount + 1
    elif c == 'G':
        gCount = gCount + 1

print "A C G T:", aCount, cCount, gCount, tCount
