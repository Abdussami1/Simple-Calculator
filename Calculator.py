# Making a simple calculator

#Function for addition
def add(p,q):
    r=p+q
    return r

#Function for subtraction
def sub(p,q):
    r=p-q
    return r

#Function for multiplication
def mul(p,q):
    r=p*q
    return r

#Function for division
def div(p,q):
    if q==0:
        print("Division by zero is not possible.\n Abort!")
    else:
        r=p/q
        return r

# Main program
print("Welcome to a simple calculator!")
x=1
while x==1:
    a=int(input("Enter first number:- "))
    b=int(input("Enter second number:- "))
    print("For doing any operations between the above two numbers select operator.")
    print("\n1. Addition")
    print("\n2. Subtraction")
    print("\n3. Multiplication")
    print("\n4. Division")
    c=int(input("Enter operator number:- "))
    if c==1:
        y=add(a,b)
        print("Sum is ",y,".")
    elif c==2:
        y=sub(a,b)
        print("Difference is ",y,".")
    elif c==3:
        y=mul(a,b)
        print("Product is ",y,".")
    elif c==4:
        y=div(a,b)
        print("After dividing the result is ",y,".")
    else:
        print("Invalid input!")
    x=int(input("Do you want to do more calculations(Enter 1 for yes and any another number for no):- "))
print("Thanks for using simple calculator.")
