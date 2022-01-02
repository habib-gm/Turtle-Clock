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
