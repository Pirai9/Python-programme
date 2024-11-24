# error
x=2
try:
    print(x)
except NameError:
    print("NameError means something is probably undefined")
except ZeroDivisionError:
    print("Please donot divide by zero")
except Exception as error:
    print(error)
else:
    print("No error")
finally:
    print("I'm going to print with or without an error")
