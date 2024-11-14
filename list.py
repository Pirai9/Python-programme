#list

grocery_list=['apple','bannana','orange']

print('apple' in grocery_list)

data=[12,'kamal','yellow']

print(data[0])
print(data[-1])
print(grocery_list.index('apple'))
print(grocery_list[0:])
print(data[1:3])


print(len(data)) 


# add the list items
grocery_list.append('pottato')
print(grocery_list)

grocery_list +=['rice']
print(grocery_list)

print("")
grocery_list.extend(['fish','chicken'])
print(grocery_list)