Key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
o = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
n=int(input())
a=input()
if n==1:
    for i in range(len(a)):
        for j in range(len(o)):
            if a[i]==o[j]:
                print(Key[j],end="")
                break
if n==2:
    for i in range(len(a)):
        for j in range(len(Key)):
            if a[i]==Key[j]:
                print(o[j],end="")
                break