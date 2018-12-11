#!/usr/bin/env python

# Creating amino acid dictionary
AminoDic = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
		"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
		"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
		"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
		"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
		"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
		"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
		"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
		"UAU":"Y", "UAC":"Y", "UAA":"stop", "UAG":"stop",
		"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
		"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
		"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
		"UGU":"C", "UGC":"C", "UGA":"stop", "UGG":"W",
		"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
		"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
		"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
		}

import sys

#Starting list for reading multiple files
filelist = []
user_args = sys.argv[1:]
for filename in user_args:
    with open(filename, 'r') as file:
        lines = file.read().replace('\n', '')
    filelist.append(lines)

 #Transcription of DNA sequences from files
dnaSeq = ''.join(filelist)
dnaSeq = dnaSeq.upper()
print("DNA sequence (ALL CAPS): %s" %dnaSeq)

rnaSeq = dnaSeq.replace("T","U")
print("Transcription sequence: %s" %rnaSeq)

 # Translation of RNA seqence to amino acid sequence
proteinSeq = ""
for i in range(0, len(rnaSeq), 3):
    if rnaSeq[i:i+3] in AminoDic:
        proteinSeq += AminoDic[rnaSeq[i:i+3]]
print("Protein Sequence : %s" %proteinSeq)

 # Printing amino acid sequence to one output file
outFileName = "ProteinSeq.txt"
outFile = open(outFileName, 'w')
outFile.write("%s \n" %proteinSeq)
print("See ProteinSeq.txt for protein sequence")