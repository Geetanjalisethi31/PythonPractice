print('*Create a list contains square of odd numbers using list Comprehension**')

matrix = []

for i in range(5):

    # Append an empty sublist inside the list
    matrix.append([])
    print('m1=',matrix)

    for j in range(7):
        print('m2=',matrix[i])
        matrix[i].append(j)

#print(matrix)

l=[10,20,30,40,50]
l1=l[0:2:2]
print(l1)