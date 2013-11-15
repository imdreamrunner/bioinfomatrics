def getMatch(text, pattern, d):
    l = len(pattern)
    mismatch = [0] * l
    match = []
    for i in range(len(text)):
        char = text[i]
        if char == pattern[0]:
            mismatch[i%l] = 0
        else:
            mismatch[i%l] = 1
        for j in range(1, l):
            if i < j:
                continue
            num = (i-j)%l
            if mismatch[num] > d:
                continue
            if pattern[j] != char:
                mismatch[num] += 1
            if j == l-1 and mismatch[num] <= d:
                match.append(i-j)
    return len(match)

line = input().split(" ")
text = line[0]
k = int(line[1])
d = int(line[2])

lenText = len(text)

dic = {}

"""
geno = ["A", "T", "C", "G"]
for i in range(4**(k-1),4**k):
    print(i/4**k)
    key = ""
    while i > 0:
        key += geno[i%4]
        i //= 4
    dic[key] = getMatch(text, key, d)
"""

for i in range(lenText - k + 1):
    key = text[i:i+k]
    if not key in dic:
        dic[key] = getMatch(text, key, d)

currentKeys = list(dic.copy().keys())
for i in range(len(currentKeys)):
    for j in range(i+1, len(currentKeys)):
        diff = 0
        position = []
        for num in range(k):
            if currentKeys[i][num] != currentKeys[j][num]:
                diff += 1
                position.append(num)
            if diff > d*2:
                break
        if d < diff <= d*2:
            for newKeyID in range(2**diff):
                newKey = currentKeys[i]
                changeId = 0
                while newKeyID > 0:
                    if newKeyID%2 != 0:
                        positionToChange = position[changeId]
                        newKey = newKey[0:positionToChange] + currentKeys[j][positionToChange] + newKey[positionToChange+1:]
                    newKeyID //= 2
                    changeId += 1
                if not newKey in dic:
                    dic[newKey] = getMatch(text, newKey, d)
                    

maxValue = max(dic.values())
print(" ".join([str(i) for i, value in dic.items() if value == maxValue]))
