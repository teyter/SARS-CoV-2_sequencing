from parse import parse_fasta
from parse import parse_fastq

from teitlib import *

from time import time

start = time()
refname,ref = parse_fasta('reference.fasta')
aliname,ali = parse_fasta('align_seqs_1og2.fasta')
#aliname,ali = parse_fasta('align_seqs1.fasta')
#aliname,ali = parse_fasta('align12_reverse.fasta')
#aliname,ali = parse_fasta('aligned12_wduplicates.fasta')
seqs = parse_fastq('SRR11397721_1.fastq',438663)
   
with open('nomatches_seqs1og2.txt') as f:
    nomatch = f.read().splitlines()
   
matches = [i for i in seqs if ref.find(i) > -1]
printList(matches)
   
mi = [i for i in range(len(ali)) if ali[i] == 'x'] 


def get_start_and_end_ofxinterval(li):
    ret = []
    ret.append(li[0])
    for i in range(len(li)-1):
        if li[i] != li[i+1]-1:
            ret.append(li[i])
            ret.append(li[i+1])
    ret.append(li[-1])
    return ret

print(get_start_and_end_ofxinterval(mi))
start_and_end_ofxinterval = get_start_and_end_ofxinterval(mi)

def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

x_interval_matrix = to_matrix(start_and_end_ofxinterval,2)

# assumin we can ignore ends
x_interval_matrix.pop(0)
x_interval_matrix.pop(-1)
printList(x_interval_matrix)


#def operation_find_candidates(ref,

end = time()
print(end-start,"secs")
"""
