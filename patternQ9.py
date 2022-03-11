#		    1
#	    22
#    333
#  4444
#55555

r=1
while r<=5:
	a=1
	while a<=6-r:
		print(" ",end=" ")
		a+=1
	c=1
	while c<=r:
		print(r,end=" ")
		c+=1
	print()
	r+=1