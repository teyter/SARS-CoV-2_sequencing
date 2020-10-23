import numpy as np


#N = [False for i in range(len(s))]
#arr = np.array([1,2,3,4,5,6,7,8,9])
#A = [False for i in range(len(arr))]
# arr[A]

def str2np(streng):
    ret = np.zeros(len(streng),dtype='str')
    for i in range(len(streng)):
        ret[i] = streng[i]
    return ret

def np2str(nparr):
    stre = ""
    for i in range(len(nparr)):
        stre += str(nparr[i])
    return stre

s = "teiturgudmundarson"
nafn = str2np(s)
nafnBOOL = [False for i in range(len(nafn))]
# real test

p = [
    "teit",
    "gudmu"
    ]

def boolize():
    for j in range(len(p)):
        index = s.find(p[j])
        if (index >= 0):
            for i in range(index,index+len(p[j])):
                nafnBOOL[i] = True

boolize()
print(nafn[nafnBOOL])
