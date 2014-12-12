#! /usr/bin/python
# -*- coding: utf-8 -*-

from Bio import SeqIO
import logging
import os, sys

f = open("annotate_prot.txt", "w")

def write_record(readFile, writeFile, annotation):
    with open(readFile, 'r') as fp:
        for seq_record in SeqIO.parse(fp, "fasta"):
            f.write(str(' '.join([amino for amino in seq_record.seq])) + "," + annotation + "\n")
            print(str(' '.join([amino for amino in seq_record.seq])) + "," + annotation)
    fp.close

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("running %s" % " ".join(sys.argv))

print("===============================================================")
print("=================結晶化するタンパク質==========================")
print("===============================================================")
print("bin02_nr50_30to200_XRAY.txt")
write_record("bin02_nr50_30to200_XRAY.txt", "annotate_prot.txt", "1")

print("===============================================================")
print("=================結晶化しないタンパク質==========================")
print("===============================================================")
print("bin02_nr50_30to200_NMR_ONLY.txt")
write_record("bin02_nr50_30to200_NMR_ONLY.txt", "annotate_prot.txt", "0")

f.close
program = os.path.basename(sys.argv[0])
logging.info("finished running %s" % program)
