str = input ("Enter number :")
num = int(str)
str2 = input ("Enter number till which number you want :")
num2 = int(str2)

     
for i in range(1,num2+1):
   print(num, 'x', i, '=', num*i)