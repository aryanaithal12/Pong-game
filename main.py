import time
from turtle import Screen
from pong import Paddle, Ball, Score

# TODO: Setup the screen
screen = Screen()
screen.title('PONG')
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# TODO: Create 2 paddle

player1 = Paddle(-350)
player2 = Paddle(350)
score = Score()
screen.update()

# TODO: detect key control

screen.listen()
screen.onkeypress((lambda: player1.move_up()), 'w')
screen.onkeypress(lambda: player1.move_down(), 's')
screen.onkeypress(lambda: player2.move_up(), 'Up')
screen.onkeypress(lambda: player2.move_down(), 'Down')

# TODO: create a ball

ball = Ball()
game_is_running = True

# TODO: The game
while game_is_running:
    screen.update()
    time.sleep(ball.time)
    ball.move()
    ball.bounce()
    ball.bounce_paddle(player2, player1)
    if ball.xcor() > 380:
        score.l_player += 1
        ball.refresh()
        screen.update()
        score.score_update()
        if score.l_player >= 5:
            score.gameover('Left Player')
            game_is_running = False
        time.sleep(2)
    elif ball.xcor() < -380:
        score.r_player += 1
        ball.refresh()
        screen.update()
        score.score_update()
        if score.r_player >= 5:
            score.gameover('Right Player')
            game_is_running = False
        time.sleep(2)
screen.exitonclick()
