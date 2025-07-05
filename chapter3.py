###########################
### chapter 3 exercises ###
###########################

# splitting genomic DNA
# Write a program that will split the genomic DNA into coding and non-coding parts,
# and write these sequences to two separate files.
# use genomic_dna.txt file

genomic_dna = open("genomic_dna.txt")
genomic_dna_content = genomic_dna.read()
print(genomic_dna_content)

exon3_1 = genomic_dna_content[0:62]
exon3_2 = genomic_dna_content[90:]
codingseq3 = exon3_1 + exon3_2
intron3 = genomic_dna_content[62:90]

coding_parts3 = open("coding_parts.txt", "w")
coding_parts3.write(codingseq3)
coding_parts3.close()

noncoding_parts3 = open("noncoding_parts.txt", "w")
noncoding_parts3.write(intron3)
noncoding_parts3.close()

# writing a fasta file

header_1 = ">ABC123"
header_2 = ">DEF456"
header_3 = ">HIJ789"
s1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
s2 = "actgatcgacgatcgatcgatcacgact"
s2 = s2.upper()
s3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
s3 = s3.replace("-", "")
text3 = header_1+ "\n" + s1 + "\n" + header_2+ "\n" + s2 + "\n" + header_3+ "\n" + s3 + "\n"

fasta3 = open("fasta3.txt", "w")
fasta3_sequences = fasta3.write(text3)
fasta3.close()

# writing multiple fasta files

# Use the data from the previous exercise, but instead of creating a single FASTA file,
# create three new FASTA files – one per sequence.
# The names of the FASTA files should be the same as the sequence header names,
# with the extension .fasta.

header_1 = ">ABC123"
header_2 = ">DEF456"
header_3 = ">HIJ789"
s1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
s2 = "actgatcgacgatcgatcgatcacgact"
s2 = s2.upper()
s3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
s3 = s3.replace("-", "")

file1 = open("ABC123.fasta", "w")
fasta1 = header_1+ "\n" + s1
file1.write(fasta1)
file1.close()

file2 = open("DEF456.fasta", "w")
fasta2 = header_2+ "\n" + s2
file2.write(fasta2)
file2.close()

file3 = open("HIJ789.fasta", "w")
fasta3 = header_3+ "\n" + s3
file3.write(fasta3)
file3.close()
