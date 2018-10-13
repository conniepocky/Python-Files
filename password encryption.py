import random

words = ["long", "tall", "happy", "sad", "squid", "cat", "horse", "waffle", "dog", "bear", "in", "the", "octopus", "a", "that", "I", "marvelous"]

passEncrypted = 0

word = words[random.randint(1,18)]

length = len(word) + 1

print("Here is your new password:")

print(word)

print("Here is it Encrypted:")

for c in range(1, length):

    passEncrypted += random.randint(1, length)

print(str(passEncrypted))
