N=int(input())
numB=list(map(int,input().split()))
counter=0
j=2
while j>1:
    numB.sort(reverse=True)
    print(numB)
    j=0
    numB[0]-=1
    numB[1]-=1
    for i in range(N):
        if numB[i]!=0:
            j+=1
    counter+=1
print(counter)