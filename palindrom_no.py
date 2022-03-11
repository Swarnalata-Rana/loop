##palindrom number
a=int(input("enter no:-"))
palindrom=0
while a>0:
	palindrom=palindrom*10+a%10
	a=a//10
print("palindrom=",palindrom)