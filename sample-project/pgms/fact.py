def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
num=int(input("Enter input for fact:"))
fact(num)

