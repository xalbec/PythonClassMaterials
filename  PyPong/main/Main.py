import pygame
from Ball import Ball
from Paddle import Paddle

pygame.init()
pygame.font.init()


WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode([WIDTH, HEIGHT])

score_font = pygame.font.SysFont('arial', 50)
player1_score = 0
player2_score = 0

clock = pygame.time.Clock()


running = True

ball = Ball(WIDTH/2, HEIGHT/2, -2, 2, screen)
left_paddle = Paddle(0, HEIGHT / 2, screen)
right_paddle = Paddle(WIDTH - 10, HEIGHT / 2, screen)

# Game Loop
while running:

    # ------------------ DOODLE ZONE -----------------------

    # makes the game wait for 16 milliseconds before running the code below roughly 60 fps for simple games
    pygame.time.delay(16)

    # sets the background color
    screen.fill([0, 0, 0])

    # Display the scores for each player
    score_board = score_font.render(str(player1_score) + "               " + str(player2_score), False, (255, 255, 255))
    screen.blit(score_board, (WIDTH/3, 0))

    # Draws a line down the center of the screen
    pygame.draw.line(screen, (255, 0, 0), (WIDTH/2, 0), (WIDTH/2, HEIGHT), 1)

    # Displays the ball on the screen
    ball.display()
    ball.move()

    # Displays the Paddles
    left_paddle.display()
    right_paddle.display()

    # Clears the screen and redraws the components on the screen
    pygame.display.flip()

    # ------------------- LOGIC ---------------------------

    if ball.rect.colliderect(left_paddle.rect):
        ball.vx *= -1
    if ball.rect.colliderect(right_paddle.rect):
        ball.vx *= -1

    if ball.is_colliding_with_left_goal():
        ball.rect.x = WIDTH/2
        ball.rect.y = HEIGHT/2
        player2_score += 1

    if ball.is_colliding_with_right_goal():
        ball.rect.x = WIDTH/2
        ball.rect.y = HEIGHT/2
        player1_score += 1

    # ------------------- KEY HANDLING --------------------

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        right_paddle.move_up()
    if keys[pygame.K_DOWN]:
        right_paddle.move_down()
    if keys[pygame.K_w]:
        left_paddle.move_up()
    if keys[pygame.K_s]:
        left_paddle.move_down()

    # ------------------ QUIT --------------------------

    # Goes through the list of buttons the player has pressed
    for event in pygame.event.get():

        # Checks to see if player hits the X button on the window
        if event.type == pygame.QUIT:
            # Stops the game loop
            running = False

# Close the game window
pygame.quit()
