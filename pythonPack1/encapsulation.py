'''print('*************Hiding the data/making private -->ENCAPSULATION*******************')

class enc():
    def __init__(self,Empname):
            self.__Empname=Empname
    def display(self):
        print('Name=',self.__Empname)
        return  self.__Empname
e1=enc('geeta')
e1.display()
newName=e1.display()
newName='Muna'
print('NewName',newName)
print(e1.display())
print('*************Wraping the data/making protected -->ENCAPSULATION 0n Inheritance*******************')

class A():
    def __init__(self):
        self._a=10
        #return self._a constructer does not allow return value
class B(A):
    def __init__(self):
        A.__init__(self)
        print('Calling protected Member',self._a)
        self._a=20
        print('Calling modified protected variable',self._a)
b1=B()
a1=A()
print(a1._a)
print('Under B class',b1._a)
# Python program to
# demonstrate protected members

# Creating a base class
class Base:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)
print('*************Wraping the data/making Private -->ENCAPSULATION 0n Inheritance*******************')
class A():
    def __init__(self):
        self.__a=10
        print(self.__a)
class B(A):
    def __init__(self):
        super().__init__()
        print('Private Member of A',self.__a)
        self.__a=20
a1=A()
b1=B()#attribute error as private member can not be accessed outside the class



# demonstrate private members

# Creating a Base class'''


class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)

    # print(self.__c) AttributeError: 'Derived' object has no attribute '_Derived__c'


# Driver code
obj1 = Base()
print(obj1.a)

#print(obj1.c)
# raise an AttributeError

obj2 = Derived()
