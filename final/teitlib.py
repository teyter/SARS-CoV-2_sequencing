# aligns single pattern to a reference
def align_single_pattern(Text,Pattern):
    s = "-"*len(Text)
    s = list(s)
    index = Text.find(Pattern)
    if index >= 0:
        s[index:index+len(Pattern)] = list(Pattern)
        print("["+str(index)+":"+str(index+len(Pattern))+"]")
    return string(s)

# aligns list of sequences to a reference
def aligndash(Text,Pattern):
    s = "-"*len(Text)
    s = list(s)
    for i in range(len(Pattern)):
        index = Text.find(Pattern[i])
        if index >= 0:
            s[index:index+len(Pattern[i])] = list(Pattern[i])
    return string(s)

# "-" tekur python mikli lengri tima ad lesa
# nota x i stadinn
def align(Text,Pattern):
    s = "x"*len(Text)
    s = list(s)
    for i in range(len(Pattern)):
        index = Text.find(Pattern[i])
        if index >= 0:
            s[index:index+len(Pattern[i])] = list(Pattern[i])
    return string(s)

# Takes in a non-matching sequence and finds
# a section of it that does match the ref
def find_single_partial_pattern(ref,pattern):
    clip = 1
    for i in range(len(pattern)):
        section = pattern[:clip]
        if ref.find(section)>=0:
            clip+=1
        else:
            return section[:clip-1]

def most_common(lst):
    return max(set(lst), key=lst.count)

# Finds consesnus string from list
# of of sequence sections
# relies on most_common above
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

# same as above but for a list
# of non matching seqs
def find_partial_pattern(ref,li):
    clip = 1
    ret = []
    for i in range(len(li)):
        clip = 1
        for j in range(len(li[i])):
            section = li[i][:clip]
            if ref.find(section)>=0:
                clip+=1
        ret.append(li[i][:clip-1])
    return ret

# prints how well filled out
# the alignment string is
def uppfylling(teitur):
    empties = 0
    filled = 0
    for i in teitur:
        if i == "x":
            empties += 1
        if i != "x":
            filled += 1
    print("Empty:",empties)
    print("Filled:",filled)
    print((filled/len(teitur))*100,"% filled")

def csv(ref,test0):
    print("Pos,Ref,Ali,Alt")
    for i in range(len(ref)):
       print(str(i)+","+str(ref[i])+","+str(test0[i]))

def output(ref,test0):
    print("Pos\tRef\tAlt")
    for i in range(len(ref)):
        if ref[i] != test0[i]:
            print(str(i)+"\t"+str(ref[i])+"\t"+str(test0[i]))

def patternExists(Text,Pattern):
    return Text.find(Pattern) >= 0

def printList(li):
    for i in li: print(i)

# list to string
def string(li):
    s = ""
    for i in li:
        s += i
    return s
