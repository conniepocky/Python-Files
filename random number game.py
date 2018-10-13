from random import randint
print("Welcome to guess the number!")
random = randint(1,10)
guessN = input("What's my number?")
if (guessN == random) :
  print("Correct My number was ", random)
else :
  print("Incorrect my number was ", random)
