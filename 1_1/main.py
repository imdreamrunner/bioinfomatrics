text = input()
k = int(input())

length = len(text)
d = {}
for i in range(length-k+1):
    key = text[i:i+k]
    if key in d.keys():
        d[key] += 1
    else:
        d[key] = 1

maxi = max(d.values())
maxi_keys = [key for key, value in d.items() if value == maxi]
print(" ".join(maxi_keys))