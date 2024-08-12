n=int(input())
time=int(input())
work=0
tleft=240-time
for i in range(1,n+1):
    t=i*5
    if tleft>=t:
        tleft-=t
        work+=1
print(work)        
    