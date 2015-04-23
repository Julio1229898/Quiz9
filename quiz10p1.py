def findThrees(l):
	sum=0
	for x in l:
		if(x%3==0):
			sum=sum+x
	return sum	
num=[0,4,2,6,9,8,3,12]
print(findThrees(num))		
