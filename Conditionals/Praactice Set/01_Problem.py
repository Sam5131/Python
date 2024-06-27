a = int(input("enter a number "))
b = int(input("enter a number "))
c = int(input("enter a number "))
d = int(input("enter a number "))

if(a>b and a>c and a>d):
    print("Greatest number is: ",a)
elif(b>a and b>c and b>d):
    print("Greatest number is: ",b)
elif(c>a and c>b and c>d):
    print("Greatest Number is: ",c)
elif(d>a and d>b and d>c):
    print("Greatest number is: ",d)