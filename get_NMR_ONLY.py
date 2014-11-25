#! /usr/bin/python
# -*- coding: utf-8 -*-

from Bio import SeqIO
import time
import logging
import os, sys

seqData = {}
allData = []
count = 0

stopList = []

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("running %s" % " ".join(sys.argv))

f = open("30to200_NMR_ONLY.txt", "w")

with open("30to200_NMR.txt", 'r') as fp:
    for seq_record in SeqIO.parse(fp, "fasta"):
        seqData[seq_record.id] = seq_record.format("fasta")

print("===============================================================")
print("=================NMR_ONLY==========================")
print("===============================================================")
with open("30to200_NMR_XRAY_over30_bitscore.txt", 'r') as fp:
    for line_ in fp:
        line = line_.rstrip().split()
        proteinId = line[0]

        if proteinId in seqData.keys():
            # del seqData[proteinId]
            stopList.append(proteinId)

for stopWord in stopList:
    del seqData[stopWord]

for myKey in seqData.keys():
    f.write(str(seqData[myKey]))
    count += 1
f.close()

print("Count: ", count)

program = os.path.basename(sys.argv[0])
logging.info("finished running %s" % program)

