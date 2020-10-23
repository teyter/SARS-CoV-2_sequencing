# Sliding window method
def Count(Text,Pattern):
    count = 0
    lenText = len(Text)
    lenPatt = len(Pattern)
    for i in range(lenText-lenPatt):
        if Text[i:i+lenPatt] == Pattern:
            count += 1
    return count

# Method using str.find()
def findCount(Text,Pattern):
    count = 0
    i = Text.find(Pattern)
    if i < 0: return count
    while (i >= 0):
        count+=1
        i = Text.find(Pattern,i+1)
    return count

def indexMatch(Text,Pattern):
    i = Text.find(Pattern)
    if i < 0: print("No matches")
    c = 0
    while (i > 0):
        c += 1
        print("Match at:",i,"to",i+len(Pattern)-1)
        i = Text.find(Pattern,i+1)
        return indices
    print("Pattern matched",c, "in the sequence")

def patternExists(Text,Pattern):
    return Text.find(Pattern) >= 0

def printList(li):
    for i in li: print(i)

def bla():
    lis = []
    for i in seqs:
        start = ref.find(i)
        if start >= 0: 
            lis.append(start)
    return lis

# list to string
def string(li):
    s = ""
    for i in li:
        s += i
    return s

# aligns single pattern to a reference
def align_single_pattern(Text,Pattern):
    s = "-"*len(Text)
    s = list(s)
    index = Text.find(Pattern)
    if index >= 0:
        s[index:index+len(Pattern)] = list(Pattern)
        print("["+str(index)+":"+str(index+len(Pattern))+"]")
    return string(s)

def complement(s):
    li = []
    for i in s:
        if i == 'A':
            li.append('T')
        elif i == 'T':
            li.append('A')
        elif i == 'C':
            li.append('G')
        elif i == 'G':
            li.append('C')
    li.reverse()
    return(string(li))

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

def find_single_partial_pattern(ref,pattern):
    clip = 1
    for i in range(len(pattern)):
        section = pattern[:clip]
        if ref.find(section)>=0:
            clip+=1
        else:
            return section[:clip-1]

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

def find_single_partial_pattern(ref,pattern):
    clip = 1
    for i in range(len(pattern)):
        section = pattern[:clip]
        if ref.find(section)>=0:
            clip+=1
        else:
            return section[:clip-1]

        
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

# telja hversu uppfylltur align strengurinn er 
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

def output_sans_ends(ref,test0):
    print("Pos\tRef\tAlt")
    for i in range(37,29854):
        if ref[i] != test0[i]:
            print(str(i)+"\t"+str(ref[i])+"\t"+str(test0[i]))
