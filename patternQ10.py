#			      1
#		      21
#        321
#      4321
#    54321
r=1
while r<=5:
	c=1
	while c<=5-r:
		print(" ",end=" ")
		c+=1
	j=r
	while j>=1:
		print(j,end=" ")
		j-=1
	print()
	r+=1