n=5
for _ in range(n):
    arr=input().split()
    nums=[]
    for i in arr:
       nums.append(chr(ord(i)-32))
    print(*nums)