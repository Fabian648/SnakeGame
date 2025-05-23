import pygame
import time
import random

# Initialisierung
pygame.init()

# Farben
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)

# Fenstergröße
width = 800
height = 600

# Fenster
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by Fabian648')

# Snake-Parameter
snake_block = 10
snake_speed = 13
head_pos = 1 # 1 - oben, 2 - rechts, 3 - unten, 4 - links
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(win, green, [block[0], block[1], snake_block, snake_block])

def message(msg, color):
    text = font.render(msg, True, color)
    win.blit(text, [width // 9, height // 3])

def game_loop():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2
    x_change = 0
    y_change = 0

    snake = []
    length = 1
    head_pos = 1

    score = 0
    score_increment = 10

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            win.fill(black)
            message("Game Over! Q zum Beenden oder C zum Neustarten", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if head_pos != 2 and event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                    head_pos = 4
                elif head_pos != 4 and event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                    head_pos = 2
                elif head_pos != 3 and event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                    head_pos = 1
                elif head_pos != 1 and event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0
                    head_pos = 3

        x += x_change
        y += y_change

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        win.fill(black)
        pygame.draw.rect(win, red, [food_x, food_y, snake_block, snake_block])
        snake_head = [x, y]
        snake.append(snake_head)

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        win.blit(score_text, (10, 10))

        if len(snake) > length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1
            score += score_increment

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
