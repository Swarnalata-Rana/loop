a=int(input("enter no"))
revers=0
while a>0:
	revers=revers*10+a%10
	a=a//10
print("revers=",revers)