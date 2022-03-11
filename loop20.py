num=int(input("enter any binary no"))
sum=0
i=1
while num!=0:
	r=num%10
	sum=sum+r*pow(2,1)
	num= int(num/10)
	i=i+1
print("decimal num",sum)
# Binary to decimal