a,b=map(int,input().split())
y=input()

# k=0
# if y[a]=='-':
#     for i in range(len(y)) :
#         if y[i] in '-0123456789' :
#             k=1

#         else:
#             k=0
#             break

# if k==1:
#     print("Yes")
# else:
#     print("No")
if (a+b+1)==len(y):
    if y[a]=='-':
            print("Yes")
    else:
        print("No")    
else:
    print("No")