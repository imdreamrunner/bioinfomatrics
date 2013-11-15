import rna

text = input()
length = len(text)
i = 0
while i < length:
    print(rna.translate(text[i:i+3]), end="")
    i += 3

print()