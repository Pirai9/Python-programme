name="balashanthira" #Global variable

def greeting():
    age=10   #local scope
    print(age)
    print(name)

greeting()
# print(age) # age is not undifine 

#************************1**************************************************#

def greeting(firstname): 
    age=10   #local scope
    print(age)
    print(name)
    print(firstname)

greeting("Ramesh")

#***************************3**********************************************#

def greeting(name): 
    age=10   #local scope
    print(age)
    print(name)
    print(name)

greeting("Ramesh")

def another():
    print(" ")
    greeting("Pirai") #global function greeting 

another()


#***************************4**********************************************#

def another():
    print(" ")
    def greeting(name): #local function greeting 
        age=10   #local scope
        print(age)
        print(name)
        print(name) 

another()
#   greeting("pirai") #dont use in outside of the function