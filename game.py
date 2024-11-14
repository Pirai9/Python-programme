import sys
import random
from enum import(Enum)


class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)

PlayerChoos=input("enter the Number \n 1 for ROck \n2 for Paper \n3 for Scissors \n\n")
player=int(PlayerChoos)



Computerchoos=random.choice("123")
computer=int(Computerchoos)

if player <1 or player>3:
    sys.exit("You must Enter the 1,2 or 3  ")

print("Player Choos "+str(RPS(player)).replace("RPS."," ")+"    ")
print("computer Choos "+str(RPS(player)).replace("RPS."," ")+"    ")

if player==1 and computer==3:
    print("You are win🏆")
elif player==2 and computer==1:
    print("You are win🏆")
elif player==3 and computer==2:
    print("You are win🏆")
elif player==computer:
    print("Tie game😊")
else:
    print("COmputer win 🏏👌🏆")

