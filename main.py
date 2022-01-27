print("========================================")

#Program 11
Name=input("Enter the Name")
for I in range(0,len(Name)):
    for J in range(0,I+1):
        print(Name[J],end=" ")
    print()

print("========================================")

#Program 12
N=int(input("Enter the Number"))
for I in range(0,N):
    for J in range(0,I+1):
        print(J+1,end=" ")
    print()

print("========================================")

#Program 13
for I in range(0,6):
    for J in range(0,7):
        if((I==0 and J%3!=0) or (I==1 and J%3==0) or (I+J)==8 or (I-J)==2):
            print('*',end="")
        else:
            print(" ",end="")
    print()

print("========================================")

#Program 14
N=int(input("Enter the Number"))
k=1
for I in range(0,N):
    for J in range(0,I+1):
        print(k,end=" ")
        k=k+1
    print()

print("========================================")


#Program 15
def fact(n):
    f=1
    if n==0:
        return 1
    for I in range(2,n+1):
        f=f*I
    return f
def comb(m,n):
    res=fact(m)//(fact(m-n)*fact(n))
    return res
N=int(input("Enter the Number:"))
for I in range(0,N):
    for J in range(0,I+1):
        print(comb(I,J)," ",end=" ")
    print()

print("========================================")