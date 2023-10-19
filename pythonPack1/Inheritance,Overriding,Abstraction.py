'''print('***********Single level inheritance****************')
class A():
    def m1(self):
      print('class A started')
    @staticmethod
    def m3():
        print('Class A m3 started')
class B(A):
    def m2(self):
        print('class B started')
b1=B()
A.m3()
B.m3()
b1.m1()
b1.m2()

print('***********Multi level inheritance****************')

class A():
    def m1(self):
        print('M1 started')
class B(A):
    def m2(self):
        print('m2 started')

class C(B):
    def m3(self):
        print('m3 started')
c1=C()
c1.m1()
c1.m2()
c1.m3()
print('***********Hierarchy inheritance****************')
class A():
    def __init__(self,a):
        print('A const')

    def m1(self):
        print('m1 started')
class B(A):
    def __init__(self):
        print('mm')
        super().__init__(10)
    def m2(self):
        print('m2 started')
class C(A):
    def m3(self):
        print('m3 started')
b1=B()
b1.m1()
b1.m2()

c1=C(10)
c1.m1()
c1.m3()
print('***********Method overriding****************')

class A():
    def Animal(self,a):
        print('Makes Sound')
class B(A):
    def Animal(self,a):
        print('mew mew')
b1=B()
b1.Animal('cat')

print('***********Abstract Class****************')
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def m1(self):
        pass
class B(A):
    def m1(self):
        print('overrided abstract method')

b1=B()
b1.m1()
print('***********Abstract Class Program****************')
from abc import ABC,abstractmethod
class car(ABC):
    def __init__(self):
        print('kk')
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class bmw(car):
    def start(self):
        print('start bmw')
    def move(self):
        print('move bmw')
    def stop(self):
        print('stop bmw')
b1=bmw()
b1.start()
b1.move()
b1.stop()'''

