#!/usr/bin/env python
# coding: utf-8

# In[3]:



def parse_fasta(fn):
    with open(fn,'r') as f:
        line = f.readline()
        name = line[1:line.find(' ')].strip()
        seq = []
        while line:
            line = f.readline()
            seq.append(line.strip())
    return name,''.join(seq)
                


# In[12]:


name,ref = parse_fasta('reference.fasta')


# In[13]:


print(name,len(ref))


# In[14]:


def parse_fastq(fn,limit=None):
    seqs = []
    with open(fn,'r') as f:
        i = 0
        while i < limit or limit is None:
            _ = f.readline()
            seq = f.readline().strip()
            _ = f.readline()
            _ = f.readline()
            seqs.append(seq)
            i += 1
    return seqs


# In[15]:


seqs = parse_fastq('SRR11397721_1.fastq')


# In[ ]:


# perfect match
i = ref.find(seqs[0])
print(i)


# In[24]:


# not a perfect match
i = ref.find(seqs[1])
i1 = ref.find(seqs[1][:30])
print(i,i1)

# In[23]:


print(ref[i1:i1+len(seqs[1])])
print('')
print(seqs[1])
