def align(Text,Pattern):
    s = "-"*len(Text)
    s = list(s)
    for i in range(len(Pattern)):
        index = Text.find(Pattern[i])
        if index >= 0:
            s[index:index+len(Pattern[i])] = list(Pattern[i])
    return string(s)

def xutput(ref,result):
    print("pos\tref\talignment")
    for i in range(len(ref)):
        print(str(i)+"\t"+str(ref[i])+"\t"+str(result[i]))

def output(ref,result):
    print(ref)
    print(result)
    print(len(ref))

# list to string
def string(li):
    s = ""
    for i in li:
        s += i
    return s

ref = "thequickbrownfoxjumpedoverthelazydog"
print(len(ref))
seqs = [
    "thequick","quickbrown","brownfox","pedov","dog","lazy", "thequickbrownfo"
    ]
def space(s):
    s = list(s)
    for i in range(0,2*len(s),2):
        s.insert(i," ")
    return string(s)

result = align(ref,seqs)
output(space(ref),space(result))

