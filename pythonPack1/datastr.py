'''s1='python is Easy'
s2=s1.split()
print(s2)
count=0
for i in range(0,len(s2)):
    count=count+1
print(count)

print('****************count vowel**********************')
s1='python is easy'
count = 0
for j in range(0,len(s1)):
    #print(s1[i])

   if s1[j]=='a' or s1[j]=='e' or s1[j]=='i' or s1[j]=='o' or s1[j]=='u':
       count=count+1

print(count)

print('****************string compare**********************')
s1='python is easy'
s2='python is easy'
s3='manual'
print(s1.__eq__(s2))
print(s1.__eq__(s3))

print('****************string space removal**********************')
s1=' python is easy '
#print(s1.strip())
#print(s1.split())
s2=s1.split()
for i in range(0,len(s2)):

    print(s2[i],end='')


print(s1.find('m'))
print(s1.index('e'))
print(s1.index('x'))

print('****************find c/cs in a string**********************')

s1='singaporejihugvjhs'
print(s1.find('s',2))'''


print('****************reverse string**********************')
s1='python is easy'
s2=''
s=s2.join(reversed(s1))
print(s)  #ysae si nohtyp
s3='java is easy'
s4='selenium is easy'
ss=s3+s4
print(ss)

#second way

s5=s3.split()
s6=''
for i in range(len(s5)-1,-1,-1):

    s6=s6+s5[i]
print('s6=',s6) #easyisjava
#3rd way
s1=' python is easy '
#print(s1.strip())
#print(s1.split())
s2=s1.split()
for i in range(len(s2)-1,-1,-1):

    print(s2[i],end=' ') #easy is python

#4th way
original_string = "C# is easy to learn"
words = original_string.split()
reversed_string = " ".join(reversed(words))
print("Original String:", original_string)
print("Reverse String:", reversed_string) # learn to easy is C#


#Program to reverse a string
gfg = "geeksforgeeks"
print(gfg[::-1])

'''print('****************revrse using method string**********************')

s1="automation is easy"
def reversed(s1):
    s2=''
    for i in s1:

        s2=i+s2
    print(s2)
s1="automation is easy"
reversed(s1) #ysae si noitamotua

print('****************Update string**********************')
s="Hello Kitty"
l=list(s)
print(l)
print(s.find('p'))
#or`    
print(s.index
.32+6('o'))
l[3]='p'
print(l)
sf=''.join(l)
print(sf)
#method 2

s1=s[0:3]+'p'+s[4:]
print(s1)


print('****************delete c/cs in string**********************')
s="Hello Kitty"
sf=s[0:4]+s[6:]
print(sf)'''


print('****************Format string**********************')
s="Hello cat Kitty"
s1='{}{}{}'.format("Hello", "cat","Kitty") #HellocatKitty
print(s1)

s2='{2}{0}{1}'.format("Hello", "cat"," Kitty") #KittyHellocat
print(s2)

s3='{K}{c}{H}'.format(H="Hello", c="cat",K=" Kitty") #KittycatHello
print(s3)

print('****************slicing string**********************')

String = 'ASTRING'

# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5,2)
s3 = slice(-1, -12, -2)

print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])

print('****************revrse using method string**********************')

s5="automation is easy"
s5=s5.split()  #['automation', 'is', 'easy'] else with out this line o/p will- b ysae si noitamotua
print(s5)
s6=''
for i in range(len(s5)-1,-1,-1):

    s6=s6+s5[i]
print(s6)  #easyisautomation

print("****************************O/P=Hello--- Today is a good day-,*************************************")
str= "Hello!!!--- Today is a good day!!-,"
s1=""

for i in str:

    if i!='!':
        s1=s1+i
print(s1)  #Hello--- Today is a good day-,



















