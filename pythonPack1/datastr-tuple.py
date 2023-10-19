'''print('*********************Different type of tuple***************************************')
s1='Geeta'
t1=tuple(s1)
print('String conversion',t1)

l=[20,30,40]
t2=tuple(l)
print('List to tuple',t2)

t3=tuple('greeks')  #conversion using built-in functionality
print('Built in conversion',t3)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('g', 'r', 'e', 'e', 'k', 's')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)
print(Tuple3[0])
print(Tuple3[1])
print(t2[-1])



l1=list(Tuple1)
print(l1)
l1.reverse()
print(l1)
l1.sort()
print(l1)

print("**************** Clearing a tuple*********************************")

tup=(2,3,'o')
del tup
print(tup) #name 'tup' is not defined'''


print("**************** sorting a tuple*********************************")

t1=(1,2,9,8,5)

print(sorted(t1))  #[1, 2, 5, 8, 9]

