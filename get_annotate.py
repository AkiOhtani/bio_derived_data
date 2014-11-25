#! /usr/bin/python
# -*- coding: utf-8 -*-

from Bio import SeqIO
import logging
import os, sys

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("running %s" % " ".join(sys.argv))

f = open("annotate_prot.txt", "w")

print("===============================================================")
print("=================結晶化するタンパク質==========================")
print("===============================================================")
with open("nr50_30to200_XRAY.txt", 'r') as fp:
    for seq_record in SeqIO.parse(fp, "fasta"):
        print("nr50_30to200_XRAY.txt:", seq_record.id)
        f.write(str(' '.join([amino for amino in seq_record.seq]))+",1\n")
        print(str(' '.join([amino for amino in seq_record.seq]))+",1")

print("===============================================================")
print("=================結晶化しないタンパク質==========================")
print("===============================================================")
with open("nr50_30to200_NMR_ONLY.txt", 'r') as fp:
    for seq_record in SeqIO.parse(fp, "fasta"):
        print("nr50_30to200_NMR_ONLY.txt:", seq_record.id)
        f.write(str(' '.join([amino for amino in seq_record.seq]))+",0\n")
        print(str(' '.join([amino for amino in seq_record.seq]))+",0")

f.close

program = os.path.basename(sys.argv[0])
logging.info("finished running %s" % program)
