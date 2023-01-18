from turtle import*


# we whant to paint house

#step 1:  draw a square 

speed(30)

width(7)
color("dark blue")
begin_fill()
forward (200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()

#end of square

#drawing a door

forward(70)
color("green")
begin_fill()
left(90)

forward(120)    #height of the door
right(90)

forward(60)
right(90)

forward(120)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)

end_fill()

#drawing a window

penup()

left(30)
forward(90)

pendown()


color("green")

left(90)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

penup()

forward(120)

left(90)
forward(200)

left(90)
forward(120)

pendown()

left(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)



exitonclick()