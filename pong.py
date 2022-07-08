from turtle import Turtle
import random


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(location, 0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.setheading(random.randint(20, 60))
        self.time = 0.05

    def move(self):
        self.fd(10)

    def bounce(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.setheading(-(self.heading()))

    def bounce_paddle(self, r_paddle, l_paddle):
        if self.xcor() > 330 and self.distance(r_paddle) < 51:
            self.setheading(180 - self.heading())
            self.time *= 0.5
        elif self.xcor() < -330 and self.distance(l_paddle) < 51:
            self.setheading(180 - self.heading())
            self.time *= 0.5

    def refresh(self):
        self.goto(0, 0)
        self.setheading(self.heading() + 180)
        self.time = 0.05


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.r_player = 0
        self.l_player = 0
        self.score_update()
        self.draw()

    def draw(self):
        self.penup()
        self.pensize(3)
        self.goto(0, -300)
        for i in range(15):
            self.pendown()
            self.goto(0, self.ycor() + 20)
            self.penup()
            self.goto(0, self.ycor() + 20)
        self.penup()

    def score_update(self):
        self.clear()
        self.draw()
        self.goto(50, 200)
        self.write(f"{self.r_player}", move=False, align='center', font=('Arial', 15, ''))
        self.goto(-50, 200)
        self.write(f"{self.l_player}", move=False, align='center', font=('Arial', 15, ''))

    def gameover(self, player):
        self.goto(0, 0)
        self.write(f"GAME OVER!    {player} wins!", move=False, align='center', font=('Arial', 25, ''))
