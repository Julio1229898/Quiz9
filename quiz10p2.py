def dotProduct(x,y):
	dotprod=0
	cont=0
	if(len (x) == len (y)):
		for a in x:
		  	b=y[cont]
		  	prod=(a*b)
		  	dotprod=dotprod+prod
		  	cont=cont+1
		return dotprod  	
	else:
	  return 'Error the vectors do not have the same size'			
v1=[2,4,5,6]
v2=[1,2,3,4]
print (dotProduct(v1,v2))	  
