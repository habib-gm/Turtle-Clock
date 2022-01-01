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
