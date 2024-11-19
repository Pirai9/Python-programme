#Scope2
name="Piraichselvan"
age=25
def another():
    global age
    age +=2
    color='green'
    def greeting(name):
        print(age)
        color='red'
        print(color)
        print(name)
    greeting("Mr_Pirai")

another()
greeting()#Not work