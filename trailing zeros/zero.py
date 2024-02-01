n=int(input("enter num"))
f=1
for i in range(1,n+1):
    f=f*i
s=str(f)
zero=0
for i in s[::-1]:
    if int(i)==0:
        zero+=1
    else:
        break
print("No of trailing zeros is",zero)