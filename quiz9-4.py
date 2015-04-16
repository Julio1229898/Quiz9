def fibonacci(x): #Julio Cesar Gonzalez Uribe A01229898
	if(x==0):
		return 0
	elif(x==1):
		return 1
	return fibonacci(x-2)+fibonacci(x-1)
num=int(input(" give a positive number to know what number you want to know of the fibonacci serie: "))
print(fibonacci(num))
