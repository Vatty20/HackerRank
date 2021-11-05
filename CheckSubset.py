t = int(input())
res = False

for i in range(t):
    num1 = int(input())
    lst1 = list(map(int, input().split()))
    num2 = int(input())
    lst2 = list(map(int, input().split()))
    
    set1 = set(lst1)
    set2 = set(lst2)
    
    if num1 > num2:
        print(res)
    elif set1.issubset(set2):
        res = True
        print(res)
    else:
        print(res)
        
    res = False