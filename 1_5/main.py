text = input()

countC = 0
countG = 0

result = []

for char in text:
    result.append(countG - countC)
    if char == "C":
        countC += 1
    elif char == "G":
        countG += 1

result.append(countG - countC)

minSkew = min(result)

i = 0

output = []

for skew in result:
    if skew == minSkew:
        output.append(i)
    i += 1

print(" ".join([str(i) for i in output]))