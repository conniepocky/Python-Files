import string

def pos(letter) :
    if letter in string.ascii_lowercase:
            print(ord(letter) - ord('a'))
            return ord(letter) - ord("a")
    elif letter in string.ascii_uppercase:
            print(ord(letter) - ord("A"))
            return ord(letter) - ord('A')
    else :
        print("That is not a letter but it might be a waffle")
        
def start() :
    hello = input("Please type a letter or a symbol!")
    
    pos(hello)

while True:

    start()
