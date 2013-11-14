def KMP(pattern, text):

    lenPattern = len(pattern)
    lenText = len(text)

    # Partial Match Table
    pre = []
    table = []
    for i in range(lenPattern):
        p = pattern[0:i+1]
        pre.append(p)
        lenMax = 0
        for j in range(i):
            if pre[j] == p[i-j:i+1]:
                lenMax = j+1
        table.append(lenMax)

    # find
    found = []
    i = 0
    while i <= lenText - lenPattern:
        for j in range(lenPattern):
            if text[i + j] != pattern[j]:
                j -= 1
                break
        j += 1
        if j == lenPattern:
            found.append(i)
        move = j - table[j-1]
        i += max(move, 1)

    return found

text = input()

print("preprocessing...")

k = 9
l = 500
t = 3
length = len(text)
d = {}
for i in range(length-k+1):
    key = text[i:i+k]
    if key in d.keys():
        d[key] += 1
    else:
        d[key] = 1

result = []

print("looping...")

for key, value in d.items():
    if value >= t:
        print("KMP...")
        result.append("lalala")
        """
        distribute = KMP(key, text)
        for i in range(len(distribute) - t + 1):
            if distribute[i+t-1] - distribute[i] < l:
                result.append(key)
                break
        """
print(len(result))