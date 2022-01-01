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
