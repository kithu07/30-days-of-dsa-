n=int(input("enter no"))
rev=0
org=n
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if rev==org:
    print("The no is palindrome")
else:
    print("The no is not palindrome")