#from microbit import *
import math

# Great Digital Race Fibonacci challenge
# How far through the sequence can a micro:bit get in 15 seconds?

targetTime = 15  # Seconds
fib1 = 0
fib2 = 1
fibSum = 0
iterations = 2  # Initial starting numbers are the first 2
secs = 0

# Set the display so we can do a reverse countdown
#countdown = Image("55555:55555:55555:00000:00000:")
#display.show(countdown)

while True:

    # Calculate the next number in the sequence
    fibSum = fib1 + fib2
    fib1 = fib2
    fib2 = fibSum
    iterations += 1

    # Check the countdown and update the display
    secs = math.floor(targetTime / 1000)
    if secs > 0:
        #display.set_pixel((15 - secs) % 5, math.floor((15 - secs) / 5), 0)
        if secs >= targetTime:
            break
# Show result on LEDs and console
result = str(iterations) + " " + str(len(str(fibSum))) + " " + str(fibSum)
print(result)
#display.scroll(str(result))
