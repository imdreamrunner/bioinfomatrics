pattern = input()
text = input()
k = int(input())
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
        if mismatch[num] > k:
            continue
        if pattern[j] != char:
            mismatch[num] += 1
        if j == l-1 and mismatch[num] <= k:
            match.append(i-j)

print(" ".join([str(i) for i in match]))

