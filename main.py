import turtle
import winsound

wn=turtle.Screen() #window
wn.title("Pong by @zkakhetelidze")
wn.bgcolor("black") #bg=background
wn.setup(width=800, height=600) #changing the size of the window, pixels
wn.tracer() #This function is used to turn turtle animation on or off and set a delay for update drawings


#Score
score_a = 0
score_b = 0


#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0) #speed of the animation, sets the speed to the max
paddle_a.shape("square") #gives paddle a shape
paddle_a.color("white") #gives paddle a color
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #width and length
paddle_a.penup() #Picks the pen up so the turtle does not draw a line as it moves
paddle_a.goto(-350,0) #coordinates (x,y), goto=This method is used to move the turtle to the said position


#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0) #speed of the animation, sets the speed to the max
paddle_b.shape("square") #gives paddle a shape
paddle_b.color("white") #gives paddle a color
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #width and length
paddle_b.penup() #Picks the pen up so the turtle does not draw a line as it moves
paddle_b.goto(350,0) #coordinates (x,y), goto=This method is used to move the turtle to the said position


#Ball
ball=turtle.Turtle()
ball.speed(0) #speed of the animation, sets the speed to the max
ball.shape("square") #gives paddle a shape
ball.color("white") #gives paddle a color
ball.penup() #Picks the pen up so the turtle does not draw a line as it moves
ball.goto(0,0) #coordinates (x,y), goto=This method is used to move the turtle to the said position
ball.dx=6 #the amount by which the turtle's xcor or ycor would change
ball.dy=-6


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal")) #align=This function is used to write text at the current turtle position.

#Function
def paddle_a_up():
    y=paddle_a.ycor() #ycor=returns the y coordinate
    y+=20 #adds 20 pixels to the y coordinate
    paddle_a.sety(y) #sets y to the new y

def paddle_a_down():
    y=paddle_a.ycor() #ycor=returns the y coordinate
    y-=20 #adds 20 pixels to the y coordinate
    paddle_a.sety(y) #sets y to the new y 

def paddle_b_up():
    y=paddle_b.ycor() #ycor=returns the y coordinate
    y+=20 #adds 20 pixels to the y coordinate
    paddle_b.sety(y) #sets y to the new y

def paddle_b_down():
    y=paddle_b.ycor() #ycor=returns the y coordinate
    y-=20 #adds 20 pixels to the y coordinate
    paddle_b.sety(y) #sets y to the new y        
    

# Keyboard binding
wn.listen() #listnes to keyboard input 
wn.onkeypress(paddle_a_up,"w") #when user presses "w" key, it calls the paddle_a_up function
wn.onkeypress(paddle_a_down,"s") #when user presses "s" key, it calls the paddle_a_up function
wn.onkeypress(paddle_b_up,"Up") #when user presses "Up" key, it calls the paddle_a_up function
wn.onkeypress(paddle_b_down,"Down") #when user presses "Down" key, it calls the paddle_a_up function


#Main game loop
while True: #the loop that keeps the game running
    wn.update()

    #Move the ball
    ball.setx(ball.xcor()+ball.dx) #The ball is going to move by 2 pixels up and diagonally, because x and y are positive
    ball.sety(ball.ycor()+ball.dy)

    #Border checking

    #Top and bottom
    if ball.ycor()>290:
        ball.sety(290) #sets y to 290
        ball.dy*=-1 #reverses the direction of the ball
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    

    elif ball.ycor()<-290:
        ball.sety(-290) #sets y to 290
        ball.dy*=-1 #reverses the direction of the ball
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)    


    #Left and right
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear() #clears what was previously on the screen
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("winning.wav",winsound.SND_ASYNC) 

    elif ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear() #clears what was previously on the screen
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("winning.wav",winsound.SND_ASYNC) 
 


    #Paddle and ball collisions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40): 
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    elif (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40): 
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)    
    