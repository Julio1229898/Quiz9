def superpower(a,b): #Julio Cesar Gonzalez Uribe A01229898
        cont=1
        num=1
        while(cont<=b):
        	num=num*a
        	cont=cont+1
        return num  
        
num=int(input("dame el numero que va a ser potenciado: "))
pot=int(input("dame el numero que quieres que sea la potencia: "))
print(superpower(num,pot))
