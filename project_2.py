import random
n = random.randint(1,100)
a = -1
guesses = 0
while a!=n:
    guesses +=1
    a = int(input("guess the no"))

    if (a > n):
      print("Lower no plz: ")

    else:
       print("Higher no plz: ")


print(f"you have guessed the number correctly in {guesses} attempts")