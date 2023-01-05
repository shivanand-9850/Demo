s = 'shivanand'
s1 = ''
# print(s[::-1])
l = len(s) - 1
while l >= 0:
    s1 = s1 + s[l]
    l -= 1

print(s1)

s = 'jadhav'
s1 = 'shivanand'
i, j = 0, 0
out = ''
while i < len(s) or j < len(s1):
    if i < len(s):
        out = out + s[i]
        i += 1
    if j < len(s1):
        out = out + s1[j]
        j += 1

print(out)

s = 'S1B2C4F5'


# a=[]
# b=[]
# for ch in s:
#     if ch .isalpha():
#         a.append(ch)
#
#     else:
#         b.append(ch)

# a=' '.join(sorted(a))
# b=' '.join(sorted(b))
# print(a)

# a=''
# b=''
# out1=''
# for ch in s:
#     if ch .isalpha():
#         a=ch
#
#     else:
#         b
#         b=int(ch)
#
#         out1=out1+a * b
# print(out1)

# s='aaaabbdddcceer'
# """i<lem(s)"""
# pre=s[0]
# out=''
# c=1
# i=1
# while i<len(s):
#     if s[i]==pre:
#         c=c+1
#
#     else:
#         out=out+str(c)+pre
#         pre=s[i]
#         c=1
#
#     if i==len(s)-1:
#         out=out+str(c)+pre
#     i=i+1
# print(out)
#
# n=int(input('n:'))
# if n<0:
#     print("enter the positive Number")
# else:
#     sum=0
#     while(n>0):
#         sum+=n
#         n-=1
#     print(sum)
#
# list_even=[i for i in range(0,20)if i%2==0]
# print(list_even)
# list1=[0, 2, 22, 6, 8, 10, 27, 14, 16, 18]
# list2=[0, 2, 20, 6, 15, 10, 12, 14, 16, 19]
# print(set(list2) | set(list1))
# list3=list1+list2
# list4=[]
# for i in range(0,len(list3)):
#     for j in range(0,len(list3)):
#         if list3[i] not in list3:
#             list4.append(list[i])
#
#             print(list4)


class A:
    def __init__(self, Name, ID, Add):
        self.Name = Name
        self.ID = ID
        self.Add = Add

    def Epm1Info(self):
        print(self.Name)
        print(self.ID)
        print(self.Add)
a = A('shivanand', 102, 'Pune')
a.Epm1Info()


class B:
    def __init__(self):
        self.shiv = "Shivanand"
    def printva(self):
        print(self.shiv)
b = B()
b.printva()


class A:
    def func1(self):
        print("print func1 A")

    def func2(self):
        print("print Func2 A")

class B(A):
    def func1(self):
        print('print Func1 B')

    def func2(self):
        print('print func2 B')

b=B()
b.func2()



# def add(datatype, *args):
#     global ans
#     if datatype==int:
#         ans=0
#
#     if datatype==str:
#         ans=''
#     for s in args:
#         ans=ans + s
#     print(ans)
#
#
# a=add('str','23','24')


# Function to take multiple arguments
def add(datatype, *args):
    if datatype == 'int':
        answer = 0
    if datatype == 'str':
        answer = ''
    for x in args:
        answer = answer + x
    print(answer)
# Integer
add('int', 5, 6)
# String
add('str', 'Hi ', 'Geeks')


print("Hello world")
