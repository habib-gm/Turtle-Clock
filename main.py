#I wrote comments where i think is important to say something

import turtle
import datetime

#create time object
time_now = datetime.datetime.now()

#getting hours, minutes and seconds now (time now) in integer
Hours = int(time_now.strftime("%I"))
Minutes = int(time_now.strftime("%M"))
Seconds = int(time_now.strftime("%S"))

#creating Turtle object and setting it's property for second ---> I used arrow
tsecond = turtle.Turtle("arrow")
tsecond.shapesize(0.2, 16)
tsecond.color("orange")
second_angle = 90

#creating Turtle object and setting it's property for minute ---> I used arrow
tminute = turtle.Turtle("arrow")
tminute.shapesize(0.3, 12)
tminute.color("grey")
minute_angle = 90

#creating Turtle object and setting it's property for hour ---> I used arrow
thour = turtle.Turtle("arrow")
thour.shapesize(0.55, 9)
thour.color("black")
hour_angle = 90

DELAY = 990 # to be used later (time in milli-second)

def screen(): # function to set up our screen and alter it
    sc = turtle.Screen()
    img = "bg.png"
    sc.title("CLOCK")
    sc.bgcolor("orange")


def clock_dashes_and_dots(): #function to create small dashs and dots in our clock

    #creating turtle object and setting it's property for dashs and dots
    tcircle = turtle.Turtle()
    tcircle.speed(0)
    tcircle.pensize(3)
    tcircle.hideturtle()

    for i in range(1, 61):
        tcircle.penup()
        tcircle.goto(0, 0)
        tcircle.rt(6)
        if bool(i%5): #Create dots in clock (i%5 =>  since we need to create 12 dashes)
            tcircle.fd(211)
            tcircle.pendown()
            tcircle.dot(8,"black")
        else: #create dashes in clock (if i is divisible by five)
            if i == 15 or i== 30 or i== 45 or i== 60: # making dashes at 12, 3, 6 and 9 diffrent color and pensize
                tcircle.pensize(5)
                tcircle.color("orange")
            tcircle.fd(195)
            tcircle.pendown()
            tcircle.fd(25)

            tcircle.pensize(3) #setting back properties altered in above if statement
            tcircle.color("black")

def border_and_fill(): # function to create a border and fill color inside our clock

    fl = turtle.Turtle() #creating turtle object and setting it's property to border and fill color inside our clock
    fl.speed(0)
    fl.pensize(15)
    fl.setpos(0, -230) #to make 230 rad circle and centered at (0,0)
    fl.begin_fill()
    fl.fillcolor("white")
    fl.circle(230)
    fl.end_fill()
    fl.hideturtle()

def small_circle (): #small circle in the middle of the clock
    small_circle = turtle.Turtle()  # creating small circle(dot) in the middle of the clock as the same color as hour stick
    small_circle.dot(25, "black")
    small_circle.hideturtle()

    small_circle2 = turtle.Turtle()  # creating small circle(dot) in the middle of the clock in the color of second stick
    small_circle2.dot(10, "orange")
    small_circle2.hideturtle()

def write(): # Function to write numbers from 1 to 12 on our clock
    twrite = turtle.Turtle()
    twrite.speed(0)
    twrite.penup()
    twrite.goto(3, 165)
    twrite.lt(180)
    hour = 12
    for i in range(1,13):
        twrite.write(hour, align="center", font=("Ravie", 17, "normal"))
        hour -= 1
        twrite.circle(180, 30)
    twrite.hideturtle()

def logo():
    # creating Turtle object and setting it's property for the logo of clock
    tlogo = turtle.Turtle()
    tlogo.color("black")
    tlogo.hideturtle()
    tlogo.penup()
    tlogo.goto(0, 120)
    tlogo.write("HB clocks", move=True ,align="center", font=("Blackadder ITC", 14, "normal"))
    tlogo.goto(0, 103)
    tlogo.write("Time is precious!", move=True ,align="center", font=("Matura MT Script Capitals", 13, "normal"))

    tlogo.goto(0, 50)
    tlogo.write("HB clocks", align="center", font = ("Old English Text MT", 5, "normal"))
def move_hour(angle=6): #Function to move hour stick in our clock
    global Hours, hr, hour_angle
    hour_angle -= angle
    thour.setheading(hour_angle)
    Hours += 1
    if Hours == 13:
        Hours = 1

def move_min(angle=6):
    global min, Minutes, minute_angle
    minute_angle -= angle
    tminute.setheading(minute_angle)

    if Minutes == 60: #to call hour function  and move hour stick
        move_hour()
        Minutes = 0 # since there is no 61 minute and we add 1 to minute later in this function
    Minutes += 1
    small_circle() # calling small circle

def move_second(angle=6):
    global sec, Seconds, second_angle

    second_angle -= angle
    tsecond.setheading(second_angle)

    if Seconds == 60:#to call hour function  and move hour stick
        move_min()
        Seconds = 0 # since there is no 61 minute and we add 1 to minute later in this function
    Seconds += 1

    turtle.ontimer(move_second, DELAY)# to move seconds by 1000(DELAY) interval by calling itself after 1000 milli seconds( almost 1 second)

def starter(): #to start the clock to move after setting up all screens and turtles
    global Hours, Minutes, Seconds
    second_angle = (Seconds * 6) # angle the second stick should turn (1 second =6 degree))
    minute_angle = Minutes * 6 # angle the minute stick should turn (1 minute =6 degree))
    hour_angle = ((Hours * 30) + (Minutes // 2)) # angle the hour stick should turn (1 hour =30 degree plus minute's degree divided by two))
    move_hour(hour_angle) #calling an hour to update hour to now (to set hour stick degree to now)
    move_min(minute_angle) #calling an minute to update minute to now (to set minute stick degree to now)
    move_second(second_angle) #calling an second to update second to now (to set second stick degree to now)


screen() #frist calling screen function
border_and_fill() #calling border_and_fill() function to make border and color of our clock
clock_dashes_and_dots() #calling dashes and dots function to make small dashes and dots behind the number in the clock
logo() #write logo name on my clock
write() #writting number on our clock
starter() #start the clock
turtle.done()



