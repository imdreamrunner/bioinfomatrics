import table

seq = input()
length = len(seq)

select = [True]*length

def weight():
    sum = 0
    for i in range(length):
        if select[i]:
            sum += table.table[seq[i]]

    return sum

result = [0, weight()]

for theL in range(1,length):
    for position in range(0, length):
        select = [False]*length
        for i in range(position, position + theL):
            select[i%length] = True
        result.append(weight())


result.sort()
print(" ".join([str(i) for i in result]))
