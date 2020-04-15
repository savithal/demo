#num=int(input("Enter the number:"))
num=123
rev =0
while(num>0):
    reminder=num%10
    rev=(rev*10)+reminder
    num=num//10

print(rev)
print(r'c:\docs\navin')
name='my name'
print(len(name))
nums=[2,14,25,36,95]
nums.pop(2)
print(nums)
fru=['aaaad','bdsss','cssffg']
print(fru[-1][-1])


a=10
print(id(a))
b=a
print(id(b))
a=2
print(a,b)

a=5
b=int(a)
k=float(b)
print(type(b),k)
a,b=5,6
print(a,b)

n=7
x=3
print(n==x)
print("----")
print(10<<5)
if False:
    print("hi")
name='sav'
print("************")
for i in range(44,11,2):
    print("&&&")
    print(i)
