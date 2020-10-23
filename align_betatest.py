from teitlib import align
from teitlib import *

# list to string
def string(li):
    s = ""
    for i in li:
        s += i
    return s

1
def aligndash(Text,Pattern):
    s = "-"*len(Text)
    s = list(s)
    for i in range(len(Pattern)):
        index = Text.find(Pattern[i])
        if index >= 0:
            s[index:index+len(Pattern[i])] = list(Pattern[i])
    return string(s)

ref = "teiturgudmundarson"
seqs = [
    "teit",
    "rgudm",
    "mund",
    "son"
    ]

align(ref,seqs)
Output:
teit-rgudmund--son
