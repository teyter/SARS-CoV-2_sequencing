from time import time
import re

start_time = time()
def parse_fasta(fn):
    with open(fn,'r') as f:
        line = f.readline()
        name = line[1:line.find(' ')].strip()
        seq = []
        while line:
            line = f.readline()
            seq.append(line.strip())
    return name,''.join(seq)

# limit None would not work
# we found out exatly how many
# sequences were in each fastq
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

name, ref = parse_fasta("reference.fasta")
seqs1 = parse_fastq('SRR11397721_1.fastq')
seqs2 = parse_fastq('SRR11397721_2.fastq')
seqs = seqs1 + seqs2
# delete duplicates
seqs = list(dict.fromkeys(seqs))

   

# list to string
# str(li) does not work properly
def string(li):
    s = ""
    for i in li:
        s += i
    return s

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

test0 = align(ref,seqs)
mi = get_missing_indices_brief(test0)

# for combined
#mi2 = [(mi[2],mi[3]),(mi[4],mi[5]),(mi[6],mi[7]),(mi[8],mi[9]),(mi[10],mi[11])]

# for aligned_seqs2.fasta
#mi2 = [(mi[2],mi[3]),(mi[4],mi[5]),(mi[6],mi[7]),(mi[8],mi[9])]

# scalable non-hardcoding version
mi2 = [(mi[i],mi[i+1]) for i in range(len(mi)-1)]
# assuming we can ignore the ends
mi2.pop(0)
mi2.pop(-1)

print("Pos\tRef\tAlt")
for mi in mi2:
	matches = find_similar(mi,30)
	if (matches != []):
		consensus = get_consensus_sequence(matches)
		for i, j in zip(range(mi[0],mi[1]+1),range(len(consensus))):
			if (ref[i] != consensus[j]):
				print("%d\t%s\t%s" %(i, ref[i], consensus[j]))

end_time = time()
print(end_time-start_time,"secs")
