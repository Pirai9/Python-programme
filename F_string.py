person="Piraichselvan"
coins=3

####################
#previous %s formating

message="/n%s has %s coins left." %(person,coins)
print(message)

####################
#previous string.format() method

message="/n{} has {} coins left.".format(person,coins)
print(message)