'''Name="Geeta"
Age=25
sal=12.00
data=True
print(Name,Age, sal,data)
print('***********************************')
print("welcome",end=' ')
print('to',end=' ')
print('BBSR')
print('***********************************')
print(10,20)
print('Geeta','Muna')

a=int(input('enter int value'))
print (a)
print('***********************************')

p=int(input('enter pinciple'))
t=int(input('enter time'))
r=int(input('enter rate of interest'))
si=(p*t*r)/100
print(si)

print('****Swap numbers****')
a=int(input('emter value of a'))
b=int(input('emter value of b'))
#o/p=b=10 a=20

c=a #c=10
print(c,a)
a=b
print(c,b,a)
b=c
print ("a=",a,'b=',b)
print('sum is',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)'''

'''print('****Operators****')
print('****<=Operators****')
age=int(input('Enter Age of the child'))
if age<=18:

 print("not eligible for voting")

else:

 print('eligible for voting')

print('****Ccheck Even odd number****')

number=int(input('Enter the Number'))

if number%2==0:
 print(number,"is even number")
else:
 print(number,'is odd number') 

print('****Ccheck biggest number****') 

number1=int(input('enter the first number'))
number2=int(input('enter the second number'))
if number1>number2:
 print(number1,"number1 is bigger")
elif number2>number1:
 print(number2,"number2 is bigger")
else:
 print('both are equal') 

print('********************for loop********************')
print('print 1 to 5')
for i in range(1,6):
 print(i)

print('********************10 to0********************')

for i in range(10,-1,-1):
  print(i)
print('********************even odd count from 1 to i********************')
even=0
odd=0
i=int(input('enter value for i'))
for i in range(1,i):
 if i%2==0:
  #print('even', i)
  even=even+1

 else:
 # print('odd',i)
   odd=odd+1

print('even=',even)
print('odd=',odd)

print('********************Nested For Loop********************')
print('* in  full box ')
for i in range(1,5):
 for j in range(1,5):
  print('*',end='')
 print('-')

print('* in a rectangle')

for i in range(1,6):
 for j in range(1,6):
  if i==1 or i==5 or j==1 or j==5:
   print('*',end='')
  else:
   print('   ')
print()

print('* in a diagonal*')
for i in range(1,6):
 for j in range(1,6):
  if i==j:
   print('*',end=' ')
  else:
   print('.',end='')
 print()

print('* in a SQUARE*')
for i in range(1,6):
 for j in range(1,6):
  if i==1 or i==5 or j==1 or j==5:
   print('*',end=' ')
  else:
   print('   ',end='')
 print()
print('* in a diagonal*')
for i in range(1,6):
 for j in range(1,6):
  if i+j==6:
   print('*',end=' ')
  else:
   print('   ',end='')
 print()
print ('*******in cross diagonal******')

for i in range(1,6):
    for j in range(1,6):
        if i==j or i+j==6:
            print('*',end='')
        else:
           print(' ',end='')
    print()

print ('*******in lower triangle******')
for i in range(1,6):
    for j in range(1,6):
        if 6<=i+j<=10:
            print('* ',end='')
        else:
            print(' ',end='')
    print()
print('******1,0 in pattern************')

for i in range (1,6):
    for j in range(1,6):
        if (i+j)%2==0 and i>=j:
            print('1',end='')
        else:
            print('0',end='')
    print()
print('******1,0 in pattern in left triangle************')

for i in range (1,6):
    for j in range(1,i+1):
        if (i+j)%2==0 :
            print('1',end='')
        else:
            print('0',end='')
    print()
print('******number in  left triangle************')

for i in range (1,6):
    for j in range(1,i+1):
        if i>=j :
            print(i,end='')
        else:
            print(' ',end='')
    print()
print('******number increment in  left triangle************')
n=1
for i in range (1,5):

    for j in range(1,i+1):

      print(n,end='')

      n=n+1
    print()
if a<=10:
    print (a)
    a=a+1

studentid=1
def studentInfo(Name,Age):
    print('Name=',Name)
    print('Age=',Age)
print('Import static Class to the Class file')
class imprt():
    @staticmethod
    def m2():
        print('import success')

class imprt1():
    stv1=10
    @staticmethod
    def m2():
        print('importing started')

        imprt1.stv2=20
        print(imprt1.stv2)
        print('import success')
    def m5(self):
        print('m5start')'''



        


    


