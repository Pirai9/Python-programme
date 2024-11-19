person="Piraichselvan"
coins=3

####################
#previous %s formating

message="\n%s has %s coins left." %(person,coins)
print(message)

####################
#previous string.format() method

message="\n{} has {} coins left.".format(person,coins)
print(message)

message="\n{1} has {0} coins left.".format(coins,person)
print(message)

message="\n{person} has {coins} coins left.".format(
    coins=coins,person=person)
print(message)

#*****************************************************
player={'person':'Dave','coin':3}
message="\n{person} has {coin} coins left.".format(**player)
print(message)


###################
# f-string! This way

message=f"\n{person} has {coins} coins left."
print(message)
message=f"\n{person} has {5*2} coins left."
print(message)
message=f"\n{person.lower()} has {5*2} coins left."
print(message)

message=f"\n{player['person']} has {5*2} coins left."
print(message)

###################
# You can pass formating
num=10
message=f"\n2.25 times {num} is {2.25*num:.2f}"
print(message)

for num in range(1,11):
    print(f"2.25 times {num} is {2.25*num:.2f}\n")




for num in range(1,11):
    print(f"{num}  divided by 4.52 is {num/4.52:.2%}\n")