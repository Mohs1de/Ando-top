nim = int(input())
print(nim % 10 * 100 + nim // 10 % 10 * 10 + nim // 100)