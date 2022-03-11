##harsahad number
num=int(input("enter no:-"))
sum=0
c=num
while c>0:
	b=c%10
	sum=sum+b
	c=c//10
if num%sum==0:
	print("harsahad number")
else:
	print("not harsahad no")