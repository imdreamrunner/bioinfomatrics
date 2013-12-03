import rna

D2R = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "C"
}

R2R = {
    "A": "U",
    "U": "A",
    "C": "G",
    "G": "C"
}

def toRNA(dna):
    rna = ""
    for char in dna:
        rna = D2R[char] + rna
    return rna

def reverse(rnas):
    result = ""
    for char in rnas:
        result = R2R[char] + result
    return result

def translate(text):
    result = ""
    i = 0
    while i < len(text):
        result += rna.translate(text[i:i+3])
        i += 3
    return result

def compare(text, acid):
    rna = toRNA(text)
    if translate(rna) == acid:
        return True
    if translate(reverse(rna)) == acid:
        return True
    return False

text = input()
acid = input()
length = len(text)
lenacid = len(acid)
for i in range(length - lenacid*3 - 1):
    key = text[i:i+3*lenacid]
    if compare(key, acid):
        print(key)