num=int(input("Enter Number To Print Fibbonacci: "))
print(num)
a=0
b=1
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b
