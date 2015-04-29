def cont_banana(filename):#Julio Cesar Gonzalez Uribe A01229898
    cont=0
    text_file=open(filename,'r')
    for line in text_file:
     	line=line.lower()
     	index=line.find('banana')
     	if (index!=-1):
     		cont=cont+1
     	while(index!=-1):
     	   index=line.find('banana',index+1)
     	   if (index!=-1):
     	   	 cont=cont+1
    return cont
print('you found ', cont_banana('banana.txt'),' bananas')    