n=int(input()) 
arr=list(map(int,input().split()))

m=[False]*n

arr.sort()

for i in range(n): 
    for j in range(i+1,n): 
        avg=(arr[i]+arr[j])/2 
        if arr[i]<avg and not m[i]: 
            arr[i]=0 
            m[i]=True 
            if arr[j]<avg and not m[j]: 
                arr[j]=0 
                m[j]=True
print(sum(arr))