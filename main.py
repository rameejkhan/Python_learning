
'''
1 for snake
-1 for water
0 for gun

game logic
Snake beat Water
Water beat Gun
Gun beats Snake
'''
import random
computer = random.choice([1,-1,0])
youstr = str(input("enter your choice (s/w/g): "))
youDict = {"s" : 1,"w": -1,"g":0}
you = youDict[youstr]
print("computer choose",computer)
print("you choose",you)

if computer ==you:
    print("it's a draw")


elif(computer ==-1 and you ==1):
    print("you win!")

elif(computer ==-1 and you ==0):
    print("you lose!")

elif(computer ==1 and you ==-1):
    print("you lose!")

elif(computer ==1 and you ==0):
    print("you win!")

elif(computer ==0 and-1):
    print("you win!")

elif(computer ==0 and 1):
    print("you lose!")

else:
    print("something wrong")