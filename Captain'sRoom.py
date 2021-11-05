k = int(input())
lst = list(map(int, input().split()))

uni = set()
rep = set()

for i in lst:
    if i in uni:
        rep.add()
    else:
        uni.add()
        
diff = uni.difference(rep)
print(*diff)