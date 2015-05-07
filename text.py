def text(filename):
  midprice=0
  citympg=0
  highwaympg=0
  cont=0
  text_file=open(	filename,'r')
  for line in text_file:
   cont=cont+1
   if(cont%2==1):
       price = line[42:46]
       city = line[52:54]
       highway= line[55:57]
       a=float(price)
       b=float(city)
       c=float(highway)
       midprice=midprice+a
       citympg=citympg+b
       highwaympg=highwaympg+c
  cars=cont/2 
  midave=midprice/cars
  cit=citympg/cars
  high=highwaympg/cars
  mid= '%.2f' % midave
  citym= '%.2f' % cit
  highw= '%.2f' % high
  return (mid, citym, highw)
print (text('93cars.txt'))  
