'''def Method1():
    print('Basic of method')
Method1()

def method2(a,b):

    print(a,b)
method2(20,50)
method2(70,80)

print('***************1 to 10 without loop***********************')

def loop(a):
    if a<=10:
        print(a)
        a=a+1
        loop(a)

loop(1)
print('*********')
def method2(a,b=9):

    print(a,b)


method2(20, b=2)
method2(70, 80)'
print('***************display student info by input function***********************')

def stdInfo(Name,Class,Age):
    print('Name=',Name)
    print('Age=',Age)
    print('class=',Class)

X=input('Enter the Name')
Y=int(input('Enter The class'))
Z=int(input('Enter Age'))
stdInfo('X',Y,Z)
print('***************display return Value***********************')


def m1():
    a = 10
    b=7
    return a
    return b


def m2():
    b = 20
    print(b)


b=m1()
m2()
print(b)
print('***************display prime Number***********************')
def prime(a):
    if a%2==0:
        print('prime number=',a)
    else:
        print(a,'Not a prime number')

prime(20)
print('***************display factorial Number***********************')
def f(a):
 fact=1
 n=int(input('Enter factorial Number'))
 for i in range (1,n):
    fact=fact*i
 print('Factorial=',fact)

f('n')
print('***************display fibbonaccie series***********************')
n=int(input('enter value of n'))
n1=0
print(n1,end='')
n2=1
print(n2,end='')

for i in range(1,n):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end='')'
#print('***************display pallindrom***********************')





print('***************global local variable**********************')
a=10
def m1(a):
        print (a)
m1(20)
print(a)
title1='Selenium'
def course(title):
        title1=title
        print(title1)
def course2():
       # title1='pythn'
        print(title1)
course('java')
course2()
print('**********************Importing Files*******************************')

from pythonPack2 import file1
print(file1.course1)
file1.coureScience()

print('********Converting Local Variable to Global***********')

BookPrice1=500
def Book(BookName,BookPrice):
    global BookPrice1
    BookPrice1=BookPrice #converting local to global
def Display():
     print(BookPrice1)
Display()
Book('physics',600)
Display()'''
print('********Print Local Variable to Global in sae name***********')

BookPrice1=300
def Book(Name,BookPrice):

    global BookPrice1
    BookPrice1=BookPrice
    print(BookPrice1)
def Display():
    print(BookPrice1)
Book('Physics',400)
Display()
print('********************Importing variable and method from another file***********************************')
from pythonPack2 import file1
from pythonPack2 import file2

file1.studentInfo('Geeta',31)
file2.Display()




