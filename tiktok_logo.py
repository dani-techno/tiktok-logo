from turtle import *

width(25)
bgcolor("white")

colors = [
  "#ff0050",
  "#00f2ea",
  "#010101"
]

positions = [
  (0, 4),
  (-4, 14),
  (0, 7)
]

# for (x, y), col in zip(positions, colors): #
for i in range(len(positions)):
  x, y = positions[i]
  col = colors[i]
  penup()
  goto(x, y)
  pendown()
  color(col)
  left(180)
  circle(50, 270)
  forward(120)
  left(180)
  circle(50, 90)

done()
