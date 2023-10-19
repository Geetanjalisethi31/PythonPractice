'''
print('******************Get a list as input from user in Python using Loop************************')
lst=[]
n=int(input('enter the final range'))
for i in range(0,n):

    lst.append(i) #here we can not write lst/l1=lst.append(i)as element will be added to the base list(lst) and we can not restore
    #it in another list .it will show None value

print('final list is :',lst)



print('**********Removing nested list in a list*************')
l=[0, [1,2,3], [4,5,[6,7,8,[9,10,11]], [12, 13]], 15, 16]

output = []
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output.append(i)


# Driver code
print('The original list: ', l)
reemovNestings(l)
print('The list after removing nesting: ', output)


print('**************** Python3 program to Find missing integers in list*********************')

def find_missing(lst):

    print(lst[0], lst[-1])
    print(set(range(lst[0], lst[-1])))
    print(set(lst))
    return sorted(set(range(lst[0], lst[-1])) - set(lst))



# Driver code
lst = [1, 2, 4, 6, 9, 10,18]
print(find_missing(lst))

print('**********************Reversing list*************************************')
a=[10,20,30,40,50]

for i in range(len(a)-1,-1,-1):
    print(a[i])#it will print elements in reverse but not in the list .to get reverse list use below methods

a=[10,20,30,40,50]
output=[]
for i in range(len(a)-1,-1,-1):
    #print(a[i])
    output.append(a[i]) #o/p=[50, 40, 30, 20, 10]


print(output)

lst = [10, 11, 19, 13, 14, 15]
lst.reverse()
print(lst)

lst.sort(reverse=True)
print(lst)

#3rd way

a=[20,30,50,10]

print(a[::-1])

import operator

List = [['Geeks', 'For'], ['Geeks']]

# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])
print('************input 2 numbers at once*********************')
x, y =input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)

print('************List Comprehension*********************')

x= [int(x) for x in input('enter multiple values').split()]
print(x)


x=[20,30,91,80]
for i in range(0,len(x)):
    print(x[i])
print('************List modification using operator*********************')
l=[1,5,6,7,8]
print(*l)
operator.setitem(l,3,4)
print(l)
operator.delitem(l,3)

print('**',l)
print(operator.getitem(l,1))
print('****',l)
for i in l:
    print(i)

print('************List modification using operator slicing fun*********************')

l=[1,2,3,4,5,10,11,12]
print(operator.getitem(l,slice(3,6)))
operator.setitem(l,slice(5,7),[6,7,8])
print('after set',l)

operator.delitem(l,slice(5,7))
print('after del,',l)

print('*********************Python List Slicing*******************************')

l=[10,20,30,40,50,60,70]
l1=l[1:5:2]
print(l1)

print('************To check common items in two list/list overlapping*******************')

l1=[1,2,3,4,5]
l2=[4,5]
for i in l1:
    if i in l2:
        print(i,'is overlapping')
    else:
        print(i,'not overlapping')

print('************To check common items in two list/list overlapping using defination*******************')

def m1():
    l3=[1,2,3,4,5,6,7,9,11]
    l4=[1,5,6,7,8,11]
    #print(l3[-1])
    for i in range(0,len(l3)):
        for j in range(0,len(l4)):
            while l3[i]==l4[j]:
                print(l3[i],'Over lap')
                break
m1()

print('************not in operator*******************')
x=10
y=30
l=[10,20,80]

if x not in l:
    print(x,'Not present')
else:
    print(x,'Present')
if y not in l:
    print(y,'not present')
else:
    print(y,'Present')


print('************is operator*******************')
x = 5
y = 5
print(x is y)
id(x)
id(y)

print('********************| Find elements of a list by indices*******************************')

a=[10,20,30,40,60]
b=[1,2,4]
c=[]
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if i==b[j]:
            c.append(a[i])

print(c)


print('*Create a list contains square of odd numbers using list Comprehension**')
l1=[X**2 for X in range (1,11) if X%2==1]
print(l1)

# Second way without List comph

l1=[]
for i in range(1,11):
    if i%2==1:
        l1.append(i*i)

print(l1)

#  filtering odd numbers
lst = filter(lambda x : x % 2 == 1, range(1, 20))
print (list(lst))


print('***************l=[1,2,3,4,5,6]*************************')
l1=[1,2,3,4]
l2=[3,4,5,6]
#l=[1,2,3,4,5,6]

l3= set(l1)
l4=set(l2)

l=l3.union(l4)
l5=list(l)
 #OR second way for code optimization
l=set(l1+l2)
print(l)
l6=[]
for i in range(0,len(l1)):

    for j in range(0,len(l2)):
        if l1[i]!=l2[j]:
            l6.append(l1[i])
            break
print(l6)  #o/p-[1, 2, 3, 4]


for i in l2:
    for j in l1:
        if l2[i] != l1[j]:
            l6.append(i)
            break

print(l6)  #o/p=[1, 2, 3, 4, 1, 2, 3, 4]


print('***************o/p=l=[1,2,3,4,5,6,7,8,9]*************************')
l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[]
def m1(l1):
    for i in l1:
        if type(i)==list:
            m1(i)
        else:
            l2.append(i)



m1(l1)
print(l2)

l1=[[1,2,3],[4,5,6],[7,8,9]]

l2=[i for sub in l1 for i in sub ]

print(l2)

l=[0, [1,2,3], [4,5,[6,7,8,[9,10,11]], [12, 13]], 15, 16]

l3=[i for sub in l for i in sub ]

print(l3) #    l3=[i for sub in l for i in sub ]
#TypeError: 'int' object is not iterable

print('********************Iterate through Nested List**********************')

l=[1,2,3,[4,5,6]]
print(l[-1])
print(l[-1][0])
print(l[-1][1])

l1=[['Ram',40],['Sita',57]]
for j,i in l1:
    print(i,'@@',j)

print('********************Convert a nested list into a flat list using Nested for Loops****************************')
lis = [10,50,[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]
flatList=[]
for element in lis:
    if type(element) is list:
        # Check if type is list than iterate through the sublist
        for item in element:
            flatList.append(item)
    else:
        flatList.append(element)
print(flatList)

print('******************To verify if a number is pallindrum*************************')
l1=[1,2,3]
l2=l1
print('l2=',l2)

if l1.reverse()==l1:
    print('pallindrum')
else:
    print('Not a pallindrum')
a='321'
l3=list(a)
print(l3)


if l3.reverse()==l3:
    print('pallindrum')
else:
    print('Not a pallindrum')

print('******************List count() method*************************')
list2 = ['b', 'a', 'a', 'b', 'b', 'a', 'b', 'b']
print(list2.count('b'))
list2 = ['b', 'a', 'a', 'b', 'b', 'a', 'b', 'b','d']
list2.pop(0)

print(list2)  #['a', 'a', 'b', 'b', 'a', 'b', 'b', 'd']

list2.remove('d')
print(list2)  #['a', 'a', 'b', 'b', 'a', 'b', 'b']

print('*****************To get Min /Max value in a list*************************')

l=[1,3,5,2,6,9]

print(min(l)) #1

print(max(l)) #6
#second Method
l1=[3,5,2,0,6,10,-5]
n=l1[0]
for i in l1:
    if n>i:
        n=i
print(n)
print('*****************Sorting in a list*************************')
l=[1,4,2,3,9]
temp=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            temp=l[j]
            l[j]=l[i]
            l[i]=temp

print(l) #[1, 2, 3, 4, 9]'''

print('*****************Create  list*************************')
#WAP to create a list by concating [p,q] with 1 to n
#final list=['p1',q1,p2,q2,p3,q3]

l1=['p','q']
FL=['{}{}'.format(x,y) for y in range (1,7) for x in l1]
print(FL) #['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5', 'p6', 'q6']

