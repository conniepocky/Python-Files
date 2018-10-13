#Imports
from random import *
#Vars
names = ["Jim", "Jeff", "Bob", "Jupiter", "Hermione", "Emily", "Clare", "Emma", "James", "Jessica", "Seamus", "Logan", "Caleb", "Ethan", "Roan", "Happy Person", "Snape"]
verbs = ["dab.", "dance.", "grin.", "code.", "build.", "run.", "read.", "sing.", "cook.", "bake.", "stare."]
adjectives = ["happily", "sadly", "villanously", "confidently", "kindly", "angrily", "tearfully"]
nouns = ["dog", "person", "turtle", "parrot", "bird", "lion", "crab", "chicken", "cat", "kitten", "puppy", "watchdog", "planet", "star", "ball"]
#Choose
namec = choice(names)
verbc = choice(verbs)
adjc = choice(adjectives)
nounc = choice(nouns)
namec2 = choice(names)
verbc2 = choice(verbs)
adj2 = choice(adjectives)
verb3 = choice(verbs)
#Print
print(namec, "Was a", nounc, "who loved to", adjc, verbc, "One day,", namec, "met", namec2, "who loved to", adj2, verbc2, "Then they started to", verb3)
