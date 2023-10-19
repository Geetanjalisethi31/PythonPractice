
'''print('***********Static Method************')
class static():
    @staticmethod
    def m1():
        print('m1 Hi')
    @staticmethod
    def m2():
        print('m2 Ho')
static.m1()
static.m2()
print('***********importing Static Method************')
from pythonPack1.Practice1 import imprt
imprt.m2()
print('***********Static Variable or class variable************')
class stVar():
    a=10
    @staticmethod
    def m1():
        print('inside m1 print')
        print(stVar.a)
        stVar.b=20
        print(stVar.b)
        print('m1 print stopped')
    @staticmethod
    def m2():
        print('inside m2')
        print(stVar.a)
        print('m2 print stopped')
stVar.m1()
stVar.m2()
print('outside the class')
print(stVar.a)
print(stVar.b)
print('***********Static Variable from different-Practice1 file************')
from pythonPack1.Practice1 import imprt1
imprt1.m2()
print(imprt1.stv1)
print('***********To convert local Variable to global Variable************')

class stVar1():
    name='Muna'
    @staticmethod
    def m1(name):
        print('m1 print started')
        print(stVar1.name)
        stVar1.name=name
        print(stVar1.name)
        print('m1 print ends')
stVar1.m1('dipti')
print(stVar1.name,'outside class')

print('***********non-static Variable/method or instance Variable/method************')
class nonStat():
    a=10
    def m1(self):
        print('m1 print start')
        self.b=20
        print(nonStat.a)
        print(self.b)
        print('m1 print ends')
    def m2(self):
        print('m2 print starts')
        self.m1()
        print('b',self.b)
        print(o1.a)
        print('m2 ends')
    @staticmethod
    def m3():
        print('m3 print starts')
        print('b',o1.b)
        print('m3 print ends')
        o1.m1()


o1=nonStat()
o1.m1()
o1.m2()
nonStat.m3()
print('outside nonstatic varable',o1.b)
print('outside static varable',o1.a)


from pythonPack1.Practice1 import imprt1
i1=imprt1()
i1.m5()
print('********************Converting local variable to non-static variable***********************************')
class locNonStat():
    def non(self,name):
        print('nonstat started')
        self.a='Geeta'
        print('non-stat a',self.a)
        self.name=name #conversion
        print(name)
        print('nonstat ended')
    def display(self):
        print('Display started')
        print(self.name,'non stat name')
        print('Display ended')
obj1=locNonStat()
obj1.non('Muna')
obj1.display()'''
print('********************Converting local variable to static variable***********************************')
class statc():
    outside='Geeta'
    @staticmethod
    def st(name):
        print('St started')
        print('Local Name',name)
        statc.Name=name  #local to static conversion
        print('After conversion',statc.Name)
        statc.b=20
        print('b',statc.b)
        print('st ended')
    @staticmethod
    def disply():
        print('Disply started')
        print('static name',statc.Name)
        print('Display ended')
    def nonstatDisply(self):
        print('nonstatdisply',statc.Name)
        statc.disply()
        print('nonstat ended')
statc.st('muna')
statc.disply()
e1=statc() #through object
e1.nonstatDisply()
#e1.st('gundu')
