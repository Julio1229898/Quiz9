import math
def readNumbersFromFile (text):#Julio Cesar Gonzalez Uribe A01229898
    cont=0
    value=0
    a=0
    text_file = open(text,'r')
    for line in text_file:
        cont=cont+1
        line=int(line)
        value=value+line
    average=value/cont
    text_file = open(text,'r')
    for lines in text_file:
        lines=int(lines)
        a=a+((lines-average)**2)
    averages=a/cont    
    standardeviation=math.sqrt(averages)
    print('the number of values is: ',cont)
    print('the total of values is: ',value)
    print('the average of the values is: ',average)
    print('the standard deviation is: ', standardeviation)
    return ''
text='numbers.txt'
print(readNumbersFromFile(text))    
