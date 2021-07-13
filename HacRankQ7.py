num1=int(input("enter num..."))
i=0
lis=[]
while i<num1:
    num2=int(input("enter any num...."))
    j=0
    while j<num2:
        if num2 not in lis:
            lis.append(num2)
        j=j+1
    i=i+1
print(lis)
a=0
max=0
while a<len(lis):
	if lis[a]>max:
	    max=lis[a]
	a+=1
	b=0
	sec=0
	while b<len(lis):
	    if max>lis[b]>sec:
	        sec=lis[b]
	    b+=1
print(max)
print(sec)