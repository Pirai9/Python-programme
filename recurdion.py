#recursion
def add(num):
    if(num>=9):
        return num+1
    toatl=num+1
    print(toatl)

    return add(toatl)

my_new_total=add(0)
print(my_new_total)

