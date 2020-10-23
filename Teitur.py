from teitlib import *
from time import time

def parse_fasta(fn):
    with open(fn,'r') as f:
        line = f.readline()
        name = line[1:line.find(' ')].strip()
        seq = []
        while line:
            line = f.readline()
            seq.append(line.strip())
    return name,''.join(seq)

def parse_fastq(fn,limit=438663):
    seqs = []
    with open(fn,'r') as f:
        i = 0
        while i < limit:
            _ = f.readline()
            seq = f.readline().strip()
            _ = f.readline()
            _ = f.readline()
            seqs.append(seq)
            i += 1
    return seqs

def alignX(Text,Pattern):
    s = "x"*len(Text)
    s = list(s)
    for i in range(len(Pattern)):
        index = Text.find(Pattern[i])
        if index >= 0:
            s[index:index+len(Pattern[i])] = list(Pattern[i])
    return string(s)

def string(li):
    s = ""
    for i in li:
        s += i
    return s

name,ref = parse_fasta('fasta/reference.fasta')

seqs = parse_fastq('SRR11397721_1.fastq',438663)
seqs2 = parse_fastq('SRR11397721_2.fastq',438663)
seqs = seqs + seqs2
# delete duplicates
#seqs = list(dict.fromkeys(seqs))
with open('nomatches_seqs1og2.txt') as f:
    nomatch = f.read().splitlines()
print(nomatches[0])
print(nomatches[1])
part = find_single_partial_pattern(ref,"TCTTTTCACTGCACTTTGGAAAGTAACA")

#alignd = alignX(ref,seqs)
end = time()
