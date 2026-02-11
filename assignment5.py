# Question one
def areaofrectangle():
    length=10
    width=5
    area=length * width
    print("The area of the rectangle is", area)
areaofrectangle()    

# Question two
def numbers(x,y):
    sum=x+y
    difference=x - y
    product=x*y
    division=x/y
    print("The sum of the number is", sum)
    print("The differnce is", difference)
    print("The product is", product)
    print("The division is", division)
numbers(45,9)    
    
# Question three
number=int(input("enter number:"))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

# Question four
def sum(n):
    total=0
    for i in range(1,n+1):
       total +=i
    print("Sum of numbers from 1 to {n} is",total)
sum(10)       

# Question five
def square(n):
    i=1
    while i<=n:
        square=i**2
        print("the square of {i} is", square)
        i+=1
n=int(input["Enter a number:"])
square(n)        

   