#import math
from math import pi  # it means math => only must (pi)

import random as rdm # it means "random" module name change to "rdm"

print(pi)

#print(dir(rdm))
for item in dir(rdm):
    print(item) 

 #https://docs.python.org/3.13/py-modindex.html

import game  #game module file insert the enother file or module
print(game.__name__)
