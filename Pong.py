#This is the first version of the bat and ball code, up to the end of page 80 (that is, step 19).

#page 72, steps 1 and 2
import tkinter
#The line below is a bug fix for versions of python that are newer than 3.5.2
from tkinter import messagebox
import time

canvasWidth = 750
canvasHeight = 500
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="Black")
canvas.pack()

#p73, step 3
bat = canvas.create_rectangle(0, 0, 40, 10, fill="blue")
ball = canvas.create_oval(0, 0, 10, 10, fill="green")

#step 4
windowOpen = True
def main_loop():
    while windowOpen == True:
        move_bat()
        move_ball()
        window.update()
        time.sleep(0.02)
        if windowOpen == True:
            check_game_over()
#p74, step 5
leftPressed = 0
rightPressed = 0
def on_key_press(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1

#step 6        
def on_key_release(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0

#step 7
batSpeed = 6 
def move_bat():
    batMove = batSpeed*rightPressed - batSpeed*leftPressed
    #p75, step 8
    (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
    #p76, step 9 
    if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
        canvas.move(bat, batMove, 0)

#p77, step 10
ballMoveX = 4
ballMoveY = -4 
setBatTop = canvasHeight-40
setBatBottom = canvasHeight-30

#step 11
def move_ball():
    global ballMoveX, ballMoveY
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    #step 12
    if ballMoveX > 0 and ballRight > canvasWidth:
        ballMoveX = -ballMoveX
    if ballMoveX < 0 and ballLeft < 0:
        ballMoveX = -ballMoveX
    if ballMoveY < 0 and ballTop < 0:
        ballMoveY = -ballMoveY
    #p78, step 13
    if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
        (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
        if ballRight > batLeft and ballLeft < batRight:
            ballMoveY = -ballMoveY
    #step 14
    canvas.move(ball, ballMoveX, ballMoveY)

#step 15    
def check_game_over():
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballTop > canvasHeight:
        playAgain = tkinter.messagebox.askyesno(message="Do you want to play again?")
        if playAgain == True:
            reset()
        else:
            close()

#step 16
def close():
    global windowOpen
    windowOpen = False
    window.destroy()

#step 17
def reset():
    global leftPressed, rightPressed
    global ballMoveX, ballMoveY
    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY = -4
    canvas.coords(bat, 10, setBatTop, 50, setBatBottom)
    canvas.coords(ball, 20, setBatTop-10, 30, setBatTop)

#step 18
window.protocol("WM_DELETE_WINDOW", close)
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)

#step 19
reset()
main_loop()
                
                
        
                
        



    
    
