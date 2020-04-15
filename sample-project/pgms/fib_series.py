'''def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return(fib(num-2)+fib(num-1))

num=int(input("Enter number for the fib series:"))
for i in range(0,num):
    print(fib(i))'''


num=int(input("Enter number for the fib series:"))
first=0
sec=1
count=0
for i in range(0,num):
    if (i<=1):
        next=i
    else:
        next=first+sec
        first=sec
        sec=next
    print(next)
    count=count+next
print("sum of fib is=",count)


