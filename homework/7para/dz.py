amd = "ААААBBBCCF"
result = ""

for i in set(amd):
    number = amd.count(amd[0])
    result += str(number)
    result += amd[0]
    amd = [j for j in amd if j != amd[0]]

print(result)