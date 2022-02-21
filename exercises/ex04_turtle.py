"""TODO: This scene depicts a bustling midnight metropolis."""

__author__ = 730489294


from turtle import Turtle, colormode, done
import random
colormode(255)


turtle_a: Turtle = Turtle()
turtle_a.speed("fastest")
turtle_a.hideturtle()

turtle_b: Turtle = Turtle()
turtle_b.speed("fastest")
turtle_b.hideturtle()

turtle_c: Turtle = Turtle()
screen = turtle_c.getscreen()
screen.bgcolor("navy")


def draw_square(turtle: Turtle, x: float, n: float) -> None:
    """This function draws a square."""
    j: int = 0
    color_number: int = random.randint(1, 4)
    color: str = ""
    if color_number == 1:
        color = "yellow"
    elif color_number == 2:
        color = "cyan"
    elif color_number == 3:
        color = "orange"
    else:
        color = "magenta"
    turtle.fillcolor(color)
    turtle.begin_fill()
    while j < n:
        turtle.forward(x)
        turtle.right(90)
        j += 1
    turtle.end_fill()


def draw_turn(turtle: Turtle, x: float, direction: str) -> None:
    """This function draws turns."""
    turtle.forward(x)
    if direction == "right":
        turtle.right(90)
    else:
        turtle.left(90)


def draw_skyscrapers_right(turtle: Turtle, x: float, y: float) -> None:
    """This function draws skyscrapers to the right of the picture."""
    i: int = 1
    while i <= 3:
        turtle.left(90)

        draw_square(turtle, x, 4)
        draw_turn(turtle, y, "right")

        draw_square(turtle, x, 3)
        draw_turn(turtle, y, "right")

        draw_square(turtle, x, 4)
        draw_turn(turtle, y, "right")

        draw_square(turtle, x, 4)
        draw_turn(turtle, y, "right")

        draw_square(turtle, x, 3)
        draw_turn(turtle, y, "right")

        draw_square(turtle, x, 4)
        turtle.left(180)
        turtle.forward(3 * x)
        i += 1


def draw_skyscrapers_left(turtle: Turtle, x: float, y: float) -> None:
    """This function draws skyscrapers to the left of the picture."""
    turtle.left(180)
    i: int = 1
    while i <= 3:
        turtle.left(180)

        draw_square(turtle, x, 4)
        draw_turn(turtle, y, "right")

        draw_square(turtle, x, 4)
        turtle.forward(x)

        draw_square(turtle, x, 4)
        turtle.forward(x)

        draw_square(turtle, x, 4)
        draw_turn(turtle, x, "right")
        turtle.forward(x)

        draw_square(turtle, x, 4)
        draw_turn(turtle, x, "right")
        turtle.forward(x)
        
        draw_square(turtle, x, 4)
        draw_turn(turtle, y, "right")
        turtle.forward(5 * x)
        turtle.left(180)
        i += 1


def draw_skyline_right(turtle: Turtle, x: float, y: float) -> None:
    """This function draws the skyline in the background."""
    turtle.pensize(2)
    j: int = 1
    while j <= 3:
        turtle.left(90)
        draw_turn(turtle, 4 * x, "right")
        draw_turn(turtle, y, "right")
        draw_turn(turtle, y, "left")
        draw_turn(turtle, x, "right")
        draw_turn(turtle, x, "left")
        draw_turn(turtle, x, "left")
        draw_turn(turtle, y, "right")
        draw_turn(turtle, x, "right")
        draw_turn(turtle, y, "left")
        draw_turn(turtle, y, "left")
        draw_turn(turtle, 4 * x, "right")
        draw_turn(turtle, y, "right")
        draw_turn(turtle, 3 * x, "left")
        draw_turn(turtle, y, "right")
        draw_turn(turtle, y, "left")
        j += 1


def draw_skyline_left(turtle: Turtle, x: float, y: float) -> None:
    """This function draws the skyline in the background."""
    turtle.left(90)
    turtle.pensize(2)
    j: int = 1
    while j <= 3:
        turtle.right(90)
        draw_turn(turtle, y, "left")
        draw_turn(turtle, y, "right")
        draw_turn(turtle, 3 * x, "left")
        draw_turn(turtle, y, "left")
        draw_turn(turtle, 4 * x, "right")
        draw_turn(turtle, y, "right")
        draw_turn(turtle, y, "left")
        draw_turn(turtle, x, "left")
        draw_turn(turtle, y, "right")
        draw_turn(turtle, x, "right")
        draw_turn(turtle, x, "left")
        draw_turn(turtle, x, "right")
        draw_turn(turtle, y, "left")
        draw_turn(turtle, y, "left")
        draw_turn(turtle, 4 * x, "right")
        j += 1


def turtle_home(turtle: Turtle) -> None:
    """This function sends the turtle back to the origin point."""
    turtle.heading()
    turtle.pos()
    turtle.home()
    turtle.penup


def draw_moon(turtle: Turtle) -> None:
    """This function draws the moon."""
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    """This draws the skyscrapers."""
    x: float = 60.0
    y: float = (2 * x)
    turtle_a.pencolor("black")
    turtle_a.pensize(5)
    draw_skyscrapers_right(turtle_a, x, y)

    turtle_home(turtle_a)
    turtle_a.left(180)
    turtle_a.forward(3 * x)
    draw_skyscrapers_left(turtle_a, x, y)

    m: float = 0.75 * x
    n: float = 2 * m

    turtle_home(turtle_a)
    turtle_a.pencolor("black")
    turtle_a.pensize(4)
    turtle_a.forward(3 * x)
    draw_skyscrapers_right(turtle_a, m, n)

    turtle_home(turtle_a)
    turtle_a.left(180)
    turtle_a.forward(1.5 * x)
    draw_skyscrapers_left(turtle_a, m, n)

    g: float = 0.5 * x
    h: float = 2 * g

    turtle_home(turtle_a)
    turtle_a.pencolor("black")
    turtle_a.pensize(4)
    turtle_a.forward(4 * x)
    draw_skyscrapers_right(turtle_a, g, h)

    turtle_home(turtle_a)
    turtle_a.left(180)
    turtle_a.forward(5 * x)
    draw_skyscrapers_left(turtle_a, g, h)

    """This draws the skyline."""
    a: float = 0.5 * x
    b: float = 2 * a

    turtle_b.pencolor("navy")
    turtle_home(turtle_a)
    turtle_a.left(90)
    turtle_a.forward(200)
    turtle_a.right(90)
    turtle_a.pencolor("yellow")
    draw_skyline_right(turtle_a, a, b)

    turtle_b.pencolor("navy")
    turtle_b.left(90)
    turtle_b.forward(200)
    turtle_b.pencolor("yellow")
    draw_skyline_left(turtle_b, a, b)

    """This draws the moon."""
    turtle_b.pencolor("navy")
    turtle_b.goto(450, 500)
    draw_moon(turtle_b)


if __name__ == "__main__":
    main()

done()
