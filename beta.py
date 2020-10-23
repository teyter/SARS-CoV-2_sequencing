ref = "abcdefhjiklmnop"
li = [
    "abcdefhjXklmnop",
    "abcX",
    "abcdeX"
    ]

pattern = "abcdefhjXklmnop"

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

#x = find_partial_pattern(ref,li)
x = find_single_partial_pattern(ref,pattern)

print(x)
