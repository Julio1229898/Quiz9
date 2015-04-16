import math #	Julio Cesar Gonzalez Uribe A01229898
def hipo(x1,y1,x2,y2):
	a=x2-x1
	b=y2-y1
	c=math.sqrt((a**2)+(b**2))
	return c
x1=int(input("give me the first x coordinate: "))
y1=int(input("give me the first y coordinate: "))
x2=int(input("give me the second x coordinate: "))
y2=int(input("give me the second y coordinate: "))
print(hipo(x1,y1,x2,y2))