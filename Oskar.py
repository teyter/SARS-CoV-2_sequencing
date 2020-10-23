from parse import parse_fasta
from parse import parse_fastq
from teitlib import *
from time import sleep
from time import time
import os
import re

from fnmatch import fnmatch

start_time = time()
"""
seqs1 = parse_fastq('SRR11397721_1.fastq',438663)
seqs2 = parse_fastq('SRR11397721_2.fastq',438663)
seqs = seqs1 + seqs2
"""
name, ref = parse_fasta("reference.fasta")
#aname, test0 = parse_fasta("aligned_reference.fasta")
aname,test0 = parse_fasta('align_seqs_1og2.fasta')
#aname, test0 = parse_fasta("align_seqs1.fasta")
with open('nomatches_seqs1og2.txt') as f:
    seqs = f.read().splitlines()

pname,morning = parse_fasta('morning.fasta')
p = "ATTCTGCTGTCAAATTACAGAATAATGAGCTTAG"
"""
matching = [i for i in seqs if ref.find(i) > -1]
c = 0
for i in range(len(matching)):
    if matching[i].find(p) >= 0:
        c+=1
print("c:",c)                        
"""
# aligns list of sequences to a reference
def align(Text,Pattern):
    s = "x"*len(Text)
    s = list(s)
    for i in range(len(Pattern)):
        index = Text.find(Pattern[i])
        if index >= 0:
            s[index:index+len(Pattern[i])] = list(Pattern[i])
    return string(s)


# returns all missing indices
def get_missing_indices(aligned_reference):
	missing_indices = []
	for i in range(len(aligned_reference)):
		curr = aligned_reference[i]
		if curr == 'x':
			missing_indices.append(i)
	return missing_indices

# returns start and end of missing indices
def get_missing_indices_brief(aligned_reference):
	missing_indices = []
	next = "" 
	prev = "" 
	for i in range(len(aligned_reference)):
		curr = aligned_reference[i]
		if i < len(aligned_reference)-1:
			next = aligned_reference[i+1]
		if i > 0:
			prev = aligned_reference[i-1]	
		if (curr == 'x' and (next != 'x' or prev != 'x')):
			missing_indices.append(i)
		# skitaredding
		if (i == len(aligned_reference) -1):
			missing_indices.append(i)
	return missing_indices


def find_similar(mi_tuple, size):
	start = mi_tuple[0]
	end = mi_tuple[1]
	length = end-start
	matches = []
	
	# skoda fyrir framan missandi gildi
	if end < len(test0)-1:
		pattern1 = ''.join(("([ACGT]","{",str(length+1),"})",test0[end+1:end+size+1]))
		matches += iterate_seqs_with_re(pattern1)

	# skoda fyrir aftan missandi gildi
	if start > 0:
		pattern2 = ''.join((test0[start-size*2:start-1],"([ACGT]","{",str(length+1),"})"))
		matches += iterate_seqs_with_re(pattern2)

	# skoda fyrir framan og aftan missandi gildi
	if start > 0 and end < len(test0)-1:
		pattern3 = ''.join((test0[start-size:start],"([ACGT]","{",str(length+1),"})",test0[end+1:end+size+1]))
		matches += iterate_seqs_with_re(pattern3)
	return matches

# hjaparfall fyrir find_similar
def iterate_seqs_with_re(pattern):
	matches = []
	p = re.compile(pattern)
	for i in range(len(seqs)):
		match = p.search(seqs[i])
		if match != None:
			matches.append(match.group(1))
	return matches

def most_common(lst):
    return max(set(lst), key=lst.count)


def get_consensus_sequence(matches):
	consensus = list("x"*len(matches[0]))
	contenders = []
	for i in range(len(consensus)):
		for j in range(len(matches)):
			contenders.append(matches[j][i])
		winner = most_common(contenders)
		consensus[i] = winner
		contenders.clear()

	return string(consensus)

mi = get_missing_indices_brief(test0)
print(mi)
mi2 = [(mi[0],mi[1]),(mi[8],mi[9])]

#=============================================================
#for i in range(len(mi)-1):
#	if i % 2 == 0:
#		print(test0[mi[i]:mi[i+1]])
#		print(ref[mi[i]:mi[i+1]])
#		print("==========")
#
#pattern = ''.join((test0[mi[8]-20:mi[9]],'[ACGT]{49}'))
#print(iterate_seqs_with_re(pattern))
#=============================================================
conlist = []
for mi in mi2:
    matches = find_similar(mi,160)
    if (matches != []):
        con = get_consensus_sequence(matches)
#       conlist.append(con)
    reference = ""
    for i in range(mi[0], mi[1]+1):
        reference += ref[i]
    print(mi)
    print(reference)
    if (matches != []):
        print(con)
    print("=========")

#print(conlist)
print("XOXOXOXOXOXO")
