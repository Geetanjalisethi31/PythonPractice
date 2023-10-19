'''print('**********************default constructor***************************')
class const1():
    def __int__(self):
        print('constructor 1 started')
        print('constructor 1 ended')
a=const1() #constructor called implicitly
print('**********************parameterised constructor***************************')
class const2():
    def __init__(self,a):
        print('const2 started')
        print('local',a)
        self.a=a
        print('const2 ended')
    def disply(self):
        print('non static a',self.a)
ob2=const2(10)
ob2.disply()
print('**********************Method overloading-->Two method of same name and diff param***************************')
class const3():
    def m1(self):
        print('m1')
    def m1(self,a):
        print('ma,a')

obj3=const3()
#obj3.m1() it will through missing argument error
obj3.m1(10)'''
print('**********************Const overloading-->Two const of same name and diff param***************************')

class const4():
    def __int__(self):
        print('default one')
    def __init__(self,a):
        print('parameter one')
#const4() #it will through missing argument error
const4(10)




