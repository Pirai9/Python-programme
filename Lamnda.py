#lamda
squared=lambda num:num * num
print(squared(3))

add_tow=lambda num:num+2
print(add_tow(10))
# def add_tow(num):
#     return num+2
# print(add_tow(7))


sum_total=lambda a,b:a+b #two variable 
print(sum_total(5,7))

#*****************************************************
print("***************Plase blow like higher order function*****************")

def funcBulder(X):
    return lambda num:num+X

add_ten=funcBulder(10)
add_twenty=funcBulder(20)
 
print(add_ten(10))
print(add_twenty(10))

#****************************************************

print("***************higher order function*****************")
number=[3,2,6,5,8,9]
squred_nums=map(lambda num:num*num,number)
print(list(squred_nums))  #[9, 4, 36, 25, 64, 81]


Odd_nums=filter(lambda num:num%2 !=0,number)
print(list(Odd_nums)) #[3, 5, 9]

from functools import reduce
numbers=[1,2,3,4,5,6,7]
total=reduce(lambda acc,curr:acc+curr,numbers)
print(total)
# print(sum(numbers))  ***same function ******

names=['Piraichselvan','Sorubaraj','Parththee','Yush']
char_count=reduce(lambda acc,curr:acc+len(curr),names,0)
print(char_count)


# end*******************************higher orderfunction*******/