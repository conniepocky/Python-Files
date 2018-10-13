import string
import random
alpha = list(string.ascii_lowercase)

length = len(alpha)

code = ""



for i in range(0, length):
    code1 = alpha[random.randint(1,length)]
    code += code1
print(code)
