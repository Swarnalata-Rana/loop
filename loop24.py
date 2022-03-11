i=1
sum1=0
sum2=0
while i<=500:
	if i%2==0:
		sum1=sum1+i
	else:
		sum2=sum2+i
	i=i+1
	print(sum1,"even")
	print(sum2,"odd")