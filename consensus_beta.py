from teitlib import *

matches = [
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT",
    "TTTTTTTTT"
    ]

with open('test_consensus2.txt') as f:
    test_consensus = f.read().splitlines()
                    
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


def brainlet(regex):
    all_consensus = []
    for i in regex:
        all_consensus.append(get_consensus_sequence(i))
    return all_consensus 

def insert_x(x,aligned,index):
    aligned[index:len(x)] = x
    return aligned
    

print( get_consensus_sequence(test_consensus) )
