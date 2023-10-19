'''s1=set('Geeta')
print(s1)

l1=[10,20,'o',30]
s2=set(l1)
print(s2)

s3=set()
print(s3)

for i in s2:
    print(i)
print(20 in s2)

print('******************Find missing Number*********************')
l1=[1,2,3,7,6,9]
#l1.sort()
#print(l1)
l=list(set(range(l1[0],l1[-1]))-set(l1))
l.sort()
print(l)
print('******************Sorting a set*********************')
s={1,3,9,6,7}
sorted(s)
print(s) #{1, 3, 6, 7, 9}
#OR

print(sorted(s))  #[1, 3, 6, 7, 9]


print("*****************Append Multiple elements in set*********************")

s1={1,2,3,4}
s1.add(5)
print(s1) #{1, 2, 3, 4, 5}
l1=[6,7,8] # or l1={6,7,8}
s1.update(l1)
print(s1) #{1, 2, 3, 4, 5, 6, 7, 8}

s2={10,20,30}
s3={40,50,30}
s4=s2.union(s3)
print(s4) #{50, 20, 40, 10, 30}'''
import operator

print("*****************Remove items from Set*********************")

'''s1={11,22,33,44,50}
s1.pop() #it will delete any element as set doesnot have index o/p- {11, 44, 50, 22}
print(s1)
s1.remove(50)
print(s1)  #{11, 44, 22}

#second way to delete complete set

# initialize the set
my_set = set([12, 10, 15, 8, 9,13,18])

# remove elements one by one using remove() method
for i in range(len(my_set)):
    my_set.remove(13)
    print(my_set)  #{8, 9, 10, 12, 15,18}'''
s={3,5,9}
print(operator.countOf(s,9)>0) #True
+