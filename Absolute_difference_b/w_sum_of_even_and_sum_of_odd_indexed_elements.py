n = int(input())
sum1 = 0
sum2 = 0
li1=list(map(int,input().split()))
for i in range(0,n):
    if i%2==0:
        sum1=sum1+li1[i]
    else:
        sum2=sum2+li1[i]
print(abs(sum1-sum2))

