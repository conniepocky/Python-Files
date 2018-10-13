print("Welcome to the password genorator")
length = input("Please type in the length of your password")
length = int(length)
import random
password = ''
chars = 'ABCDE@FGH#IJKL!MNOPQR/STUV1WXYZ23456789+-*|?:;[]{}()&^%$£~.,<>'
for c in range(length):
  password += random.choice(chars)
print(password)
