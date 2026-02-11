def palindrome(s):
   
    h=list(reversed(s))
    if s==h:
       
        return "YES" 
    return "NO"
n= int(input())
s=list(map(int,input().split()))
print(palindrome(s))
    