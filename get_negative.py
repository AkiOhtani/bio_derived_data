#! /usr/bin/python
# -*- coding: utf-8 -*-

from Bio import SeqIO
import time
import logging
import os, sys

seqData = {}
allData = []
count = 0

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("running %s" % " ".join(sys.argv))

f = open("30to200_NMR.txt", "w")
# f2 = open("", "w")

with open("pdb_seqres.txt", 'r') as fp:
    for seq_record in SeqIO.parse(fp, "fasta"):
        # seqData[seq_record.id] = seq_record.seq
        seqData[seq_record.id] = seq_record.format("fasta")
        if seq_record.description.split()[1] == "mol:protein" and 30 <= len(seq_record.seq) and len(seq_record.seq) <= 200:
            allData.append(seq_record.id)

print("===============================================================")
print("================結晶化しないタンパク質=========================")
print("===============================================================")

with open("pdb_entry_type.txt", 'r') as fp2:
    for line_ in fp2:
        line = line_.rstrip().split()
        proteinId, proteinDist, proteinMeth = line[0], line[1], line[2]

        if proteinMeth == "NMR" and proteinDist == "prot":
            for myKey in allData:
                if proteinId in myKey:
                    # print("pdb_entry_type.txt:", proteinId, proteinDist, proteinMeth)
                    # print("pdb_seqres.txt:", myKey)
                    # f.write(str(' '.join([amino for amino in seqData[myKey]]))+",0\n")
                    # print(str(' '.join([amino for amino in seqData[myKey]]))+",0")
                    f.write(str(seqData[myKey]))
                    count += 1

print("Count: ", count)
count = 0

# print("===============================================================")
# print("=================結晶化するタンパク質==========================")
# print("===============================================================")
# with open("pdb_entry_type.txt", 'r') as fp:
#     for line_ in fp:
#         line = line_.rstrip().split()
#         proteinId, proteinDist, proteinMeth = line[0], line[1], line[2]

#         if proteinMeth == "diffraction" and proteinDist == "prot":
#             for myKey in allData:
#                 if proteinId in myKey:
#                     # print("pdb_entry_type.txt:", proteinId, proteinDist, proteinMeth)
#                     # print("pdb_seqres.txt:", myKey)
#                     # f.write(str(' '.join([amino for amino in seqData[myKey]]))+",1\n")
#                     # print(str(' '.join([amino for amino in seqData[myKey]]))+",1")
#                     f2.write(str(seqData[myKey]))
#                     count += 1
# print("Count: ", count)
f.close
# f2.close()

program = os.path.basename(sys.argv[0])
logging.info("finished running %s" % program)
