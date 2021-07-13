# 

n1=int(input("enter the number: "))
i=0
while i<=n1:
    even_odd=input("enter the even/odd: ")
    n2=int(input("enter the num: "))
    j=0
    c1=0
    c2=0
    while True:
        if even_odd=="even":
            if j%2==0:
                c1=c1+1
                print(j)
            if c1==n2:
                break
        if even_odd=="odd":
            if j%2!=0:
                c2=c2+1
                print(j)
            if c2==n2:
                break
        j=j+1
    i=i+1
