def pair(d):
    return {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }[d]

text = input()
length = len(text)
for i in range(length-1, -1, -1):
    print(pair(text[i]), end="")
print()