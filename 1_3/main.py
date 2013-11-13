pattern = input()
text = input()

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
        found.append(str(i))
    move = j - table[j-1]
    i += max(move, 1)

print(" ".join(found))