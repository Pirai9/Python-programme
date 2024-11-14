#function

def module():
    print("Hello world")

module()


def sum(num1,num2):
    return num1+num2

total=sum(7,2)
print(total)


def sum(num1=0,num2=0):
    if (type(num1) is not int or type(num2)is not int):
        return("Sorry you can't enter the number")

    return num1+num2

#total1=sum("balashanthiran",2)
total1=sum()
print(total1)

#multible item input parameter

def multible_item(*args):
    print(args)
    print(type(args)) #truble

multible_item("dave","john","Sara")

def multible_item1(*args):
    print(args)
    print(type(args)) #truble

multible_item(["dave","john","Sara"])

#number sum in loop 
def add(*num):
    sum=0
    for n in num:
        sum=sum+n
    print("SUM:",sum)

add(2,5,10) 

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Pirai",last="Pirathee")



