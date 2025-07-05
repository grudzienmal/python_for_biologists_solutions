###########################
### chapter 2 exercises ###
###########################

# please note that although chapter 2 does not cover the loops
# I solved "complementing DNA" exercise using a loop

# computing AT content
DNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
AT_content = (DNA.count('A') + DNA.count('T'))*100/len(DNA)
print(AT_content)
# AT content is 68,5%

# complementing DNA
DNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# we can do it using upper and lower case
# but it's easier to do a loop
DNA2 = ""
for i in DNA:
    if i == "A":
        DNA2 = DNA2 + "T"
    elif i == "C":
        DNA2 = DNA2 + "G"
    elif i == "G":
        DNA2 = DNA2 + "C"
    else:
        DNA2 = DNA2 + "A"
print(DNA2)

# restriction fragment lengths
DNA = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
# e.coli EcoRI cuts G*AATTC
# produce 2 fragments after digestion
DNA_cut = DNA.replace("GAATTC","G*AATTC")
print(DNA_cut)
DNA_cut.find("*")
# * is at position 22, so this is the 23 character
# first position is 0
# the length of first fragment = from beginning to *
size1 = DNA_cut.find("*")
size2 = len(DNA) - size1 - 1
print("First fragment: " + str(size1))
print("Second fragment: " + str(size2))

# splicing out introns pt 1
# the following string has 2 exons and 1 intron
# The first exon runs from the start of the sequence to the 63rd character,
# and the second exon runs from the 91st character to the end of the sequence.
# Write a program that will print just the coding regions of the DNA sequence.

gdna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = gdna[0:62]
exon2 = gdna[90:]
codingseq = exon1 + exon2

# compare if codingseq is same as the answer
# answer = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCATCGATCGATATCGATGCATCGACTACTAT"
# codingseq == answer
# if TRUE, they are the same

# splicing out introns pt 2
# Using the data from part one, write a program that will calculate
# what percentage of the DNA sequence is coding.

coding_percentage = len(codingseq) * 100 / len(gdna)
print(coding_percentage)

# splicing introns out pt 3
# Using the data from part one, write a program that will print out the original
# genomic DNA sequence with coding bases in uppercase and non-coding bases in lowercase.
intron = gdna[62:90]
gdna_new = exon1.upper() + intron.lower() + exon2.upper()
print(gdna_new)
