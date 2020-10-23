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
