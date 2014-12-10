#! /usr/bin/python
# -*- coding: utf-8 -*-

from Bio import SeqIO
import logging
import os, sys

def write_length_record(readFile, writeFile):
    with open(readFile, 'r') as fp:
        with open(writeFile, 'w') as f:
            for seq_record in SeqIO.parse(fp, "fasta"):
                print(writeFile + ":", seq_record.id)
                f.write(str(' '.join([amino for amino in seq_record.seq])) + "," + str(len(seq_record.seq)) + "\n")
                print(str(' '.join([amino for amino in seq_record.seq])) + "," + str(len(seq_record.seq)))
        f.close
    fp.close

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("running %s" % " ".join(sys.argv))

print("===============================================================")
print("=================結晶化するタンパク質==========================")
print("===============================================================")
write_length_record("nr50_30to200_XRAY.txt", "nr50_30to200_XRAY_lengthlist.txt")

print("===============================================================")
print("=================結晶化しないタンパク質==========================")
print("===============================================================")
write_length_record("nr50_30to200_NMR_ONLY.txt", "nr50_30to200_NMR_ONLY_lengthlist.txt")

program = os.path.basename(sys.argv[0])
logging.info("finished running %s" % program)
