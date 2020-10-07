import turtle


def draw_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_flower(turtle):
    for i in range(36):
        draw_square(turtle)
        turtle.right(10)


def draw_pic():
    window = turtle.Screen()
    window.bgcolor('red')
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('white')
    draw_flower(brad)
    window.exitonclick()


if __name__ == '__main__':
    draw_pic()
