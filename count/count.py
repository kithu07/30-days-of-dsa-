n=int(input("enter no"))
s=str(n)
count=0
for i in s:
    if n%int(i)==0:
        count=count+1
print("No of digits perfectly divisible is",count)