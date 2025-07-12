#153 numer means 1's cube + 5's cube + 3's cube
num=input("Enter To Check Number Is Armstrong Or Not: ")
m1=0
for i in num:
    arm=int(i)
    m1+=arm**3
if m1==int(num):
        print("Armstrong")
else:
        print("Not Armstrong")