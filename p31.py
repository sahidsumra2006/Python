num=list((input("Enter To Reverse Number: ")))
l=list(reversed(num))
print("Your Reversed Value Is: ",end="")
for i in l:
    print(i.strip(),end="")