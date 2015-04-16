def triangle(x): #Julio CEsar Gonzalez Uribe A01229898     
	for i in range(0,x,1):
	   for y in (0,i+1):
	     print("T"*y,end='')
	   print()	
	for h in range(x-1,-1,-1):
	   for g in (0,h+1):
	     print("T"*g,end='')
	   print()
	return ''
size=int(input("give me the size of the triangle you want: "))
print(triangle(size))
		
