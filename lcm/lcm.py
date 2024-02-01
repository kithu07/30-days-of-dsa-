a=int(input("enter first num"))
b=int(input("enter second num"))
max=a
if b>a:
    max=b
while 1:
    if max%a==0 and max%b==0:
        print("LCM of the two numbers is",max)
        break
    else:
        max+=1