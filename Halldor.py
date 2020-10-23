from parse import parse_fastq
from parse import parse_fasta
from teitlib import *
from time import sleep
from time import time
import os
import re

from fnmatch import fnmatch

start_time = time()

seqs1 = parse_fastq('SRR11397721_1.fastq',438663)
seqs2 = parse_fastq('SRR11397721_2.fastq',438663)
seqs = seqs1 + seqs2
name, ref = parse_fasta("reference.fasta")
#aname, test0 = parse_fasta("aligned_reference.fasta")
aname,test0 = parse_fasta('align_seqs_1og2.fasta')
#aname, test0 = parse_fasta("align_seqs1.fasta")

pname,morning = parse_fasta('morning.fasta')

with open('matches_seqs1og2.txt') as f:
    matches = f.read().splitlines()

with open('nomatches_seqs1og2.txt') as f:
    nomatches = f.read().splitlines()

B = 902-10
E = 910+10
print(ref[B:E])
print(morning[B:E])
print(test0[B:E])

find_similar = morning[902:910]

count = 0
li = []
for i in range(len(matches)):
    found = matches[i].find(find_similar)
    if found > -1:
        li.append( matches[i][found-10:found+len(find_similar)+10] )
        count += 1

printList(li)

