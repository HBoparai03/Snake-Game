import pygame
import random
from pygame.locals import *

def game_over_menu(score):
    # Custom fonts
    menu_font_title = pygame.font.Font(None, 60)  
    menu_font_button = pygame.font.Font(None, 40) 

    title_text = menu_font_title.render("Game Over", True, (255, 0, 0))
    score_text = menu_font_button.render(f"Score: {score}", True, (255, 255, 255))

    exit_button_rect = pygame.Rect(350, 550, 300, 100)
    exit_button_color = (255, 0, 0)
    exit_button_text = menu_font_button.render("Exit", True, (255, 255, 255))

    play_again_button_rect = pygame.Rect(350, 400, 300, 100)
    play_again_button_color = (0, 102, 204)
    play_again_button_text = menu_font_button.render("Main Menu", True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):
                    return 'EXIT_GAME'
                elif play_again_button_rect.collidepoint(event.pos):
                    return 'RESTART_GAME'  # Start a new game

        window.fill((0, 0, 0))

        title_rect = title_text.get_rect(center=(window_width // 2, window_height // 4))
        score_rect = score_text.get_rect(center=(window_width // 2, window_height // 3))

        window.blit(title_text, title_rect)
        window.blit(score_text, score_rect)

        pygame.draw.rect(window, exit_button_color, exit_button_rect)
        pygame.draw.rect(window, play_again_button_color, play_again_button_rect)

        window.blit(exit_button_text, (exit_button_rect.centerx - 30, exit_button_rect.centery - 20))
        window.blit(play_again_button_text, (play_again_button_rect.centerx - 80, play_again_button_rect.centery - 20))

        pygame.display.update()
        clock.tick(30)

def main_menu():
    menu_font = pygame.font.Font(None, 64)
    title_text = menu_font.render("SNAKE GAME", True, (255, 255, 255))

    menu_font_creator = pygame.font.Font(None, 36)
    creator_text = menu_font_creator.render("Creator: Harnoor", True, (255, 255, 255))
    
    start_button_rect = pygame.Rect(350, 400, 300, 100)
    start_button_color = (0, 255, 0)
    start_button_text = menu_font.render("Start", True, (0, 0, 0))
    
    exit_button_rect = pygame.Rect(350, 550, 300, 100)
    exit_button_color = (255, 0, 0)
    exit_button_text = menu_font.render("Exit", True, (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()

        window.fill((0, 0, 0))
        window.blit(title_text, (350, 100))
        window.blit(creator_text, (400, 200))
        
        pygame.draw.rect(window, start_button_color, start_button_rect)
        pygame.draw.rect(window, exit_button_color, exit_button_rect)
        
        window.blit(start_button_text, (start_button_rect.centerx - 50, start_button_rect.centery - 30))
        window.blit(exit_button_text, (exit_button_rect.centerx - 30, exit_button_rect.centery - 30))

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    pygame.init() 

    window_width, window_height = 1000, 1000
    tile_size = 50  # Size of each tile
    border_size = 50  # Size of the black border
    window = pygame.display.set_mode((window_width, window_height))

    clock = pygame.time.Clock()

    while True:
        main_menu()

        snake = [pygame.Rect(random.randint(border_size // tile_size, (window_width - border_size) // tile_size - 1) * tile_size,
                        random.randint(border_size // tile_size, (window_height - border_size) // tile_size - 1) * tile_size,
                        tile_size, tile_size)]
        direction = (0, 0)
        speed = 1
        move_delay = 200
        last_move_time = pygame.time.get_ticks()

        def generate_random_block():
            return pygame.Rect(random.randint(border_size // tile_size, (window_width - border_size) // tile_size - 1) * tile_size,
                            random.randint(border_size // tile_size, (window_height - border_size) // tile_size - 1) * tile_size,
                            tile_size, tile_size)

        random_block = generate_random_block()
        danger_block = generate_random_block()

        eye_radius = 5
        eye_offset = 10
        
        pygame.draw.circle(window, (0, 0, 0), (snake[0].left + eye_offset, snake[0].centery), eye_radius)
        pygame.draw.circle(window, (0, 0, 0), (snake[0].right - eye_offset, snake[0].centery), eye_radius)

        pygame.display.flip()

        danger_blocks = [generate_random_block()]
        score = 0

        clock = pygame.time.Clock()
        
    

        run = True
        while run:
                # Create a checkered pattern with alternating tiles
                for row in range(0, window_height, tile_size):
                    for col in range(0, window_width, tile_size):
                        if (row // tile_size + col // tile_size) % 2 == 0:
                            pygame.draw.rect(window, (3, 94, 252), (col, row, tile_size, tile_size))
                        else:
                            pygame.draw.rect(window, (52, 186, 235), (col, row, tile_size, tile_size))

                pygame.draw.rect(window, (0, 0, 0), (0, 0, window_width, border_size))
                pygame.draw.rect(window, (0, 0, 0), (0, 0, border_size, window_height))
                pygame.draw.rect(window, (0, 0, 0), (0, window_height - border_size, window_width, border_size))
                pygame.draw.rect(window, (0, 0, 0), (window_width - border_size, 0, border_size, window_height))

                current_time = pygame.time.get_ticks()
        
                if current_time - last_move_time >= move_delay:
                    # Move the snake based on the direction and speed
                    new_head = pygame.Rect(snake[0].x + direction[0] * tile_size,
                                        snake[0].y + direction[1] * tile_size,
                                        tile_size, tile_size)

                    # Check if the snake head collides with the random block
                    if new_head.colliderect(random_block):
                        random_block = generate_random_block()
                        for block in danger_blocks:  # Update positions of existing danger blocks
                            block.left = random.randint(border_size // tile_size, (window_width - border_size) // tile_size - 1) * tile_size
                            block.top = random.randint(border_size // tile_size, (window_height - border_size) // tile_size - 1) * tile_size


                        # Increase snake size by adding a new segment at the tail
                        snake.append(snake[-1])
                        score += 1

                        if score % 5 == 0:
                            for _ in range(score % 5 == 0):  # Add new danger block
                                new_danger_block = generate_random_block()
                                danger_blocks.append(new_danger_block)

                    # Check if the snake head collides with the danger block
                    if new_head.colliderect(danger_block):
                        run = False

                    # Check if the snake head collides with its own body
                    for segment in snake[1:]:
                        if new_head.colliderect(segment):
                            run = False
                            break  # Exit the loop as soon as a collision is detected

                    # If not colliding, insert the new head at the front and remove the tail of the snake
                    if run:
                        snake.insert(0, new_head)
                        snake.pop()

                        # Adjust the position if the snake head goes out of boundaries
                        if new_head.left < border_size:
                            new_head.left = window_width - border_size - tile_size
                        elif new_head.right > window_width - border_size:
                            new_head.left = border_size

                        if new_head.top < border_size:
                            new_head.top = window_height - border_size - tile_size
                        elif new_head.bottom > window_height - border_size:
                            new_head.top = border_size

                        last_move_time = current_time

                # Draw a heart for the random block
                pygame.draw.polygon(window, (255, 0, 0), [
                    (random_block.centerx, random_block.top + random_block.height // 4),
                    (random_block.left + random_block.width // 4, random_block.centery),
                    (random_block.centerx, random_block.bottom - random_block.height // 4),
                    (random_block.right - random_block.width // 4, random_block.centery)
                ])

        

                for danger_block in danger_blocks:
                    pygame.draw.rect(window, (255, 255, 0), danger_block)
                    pygame.draw.line(window, (255, 0, 0), (danger_block.left, danger_block.top),
                                (danger_block.right, danger_block.bottom), 2)
                    pygame.draw.line(window, (255, 0, 0), (danger_block.right, danger_block.top),
                                (danger_block.left, danger_block.bottom), 2)
                font = pygame.font.Font(None, 36)
                score_text = font.render(f"Score: {score}", True, (255, 255, 255))
                window.blit(score_text, (10, 10))  # Adjust the position as needed

                for segment in snake:
                    pygame.draw.rect(window, (0, 255, 0), segment)  # Draw each segment of the snake
                        
                # Draw eyes on the snake head

                eye_radius = 5
                eye_offset = 10
                
                if direction == (0, -1):  # Moving left
                    pygame.draw.circle(window, (0, 0, 0), (snake[0].left + eye_offset, snake[0].centery), eye_radius)
                    pygame.draw.circle(window, (0, 0, 0), (snake[0].right - eye_offset, snake[0].centery), eye_radius)
                elif direction == (0, 1):  # Moving right
                    pygame.draw.circle(window, (0, 0, 0), (snake[0].left + eye_offset, snake[0].centery), eye_radius)
                    pygame.draw.circle(window, (0, 0, 0), (snake[0].right - eye_offset, snake[0].centery), eye_radius)
                elif direction == (-1, 0):  # Moving up
                    pygame.draw.circle(window, (0, 0, 0), (snake[0].centerx, snake[0].top + eye_offset), eye_radius)
                    pygame.draw.circle(window, (0, 0, 0), (snake[0].centerx, snake[0].bottom - eye_offset), eye_radius)
                elif direction == (1, 0):  # Moving down
                    pygame.draw.circle(window, (0, 0, 0), (snake[0].centerx, snake[0].top + eye_offset), eye_radius)
                    pygame.draw.circle(window, (0, 0, 0), (snake[0].centerx, snake[0].bottom - eye_offset), eye_radius)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        run = False
                        menu_run = False
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            run = False
                        elif event.key in [K_a, K_LEFT]:
                            direction = (-1, 0)
                        elif event.key in [K_d, K_RIGHT]:
                            direction = (1, 0)
                        elif event.key in [K_w, K_UP]:
                            direction = (0, -1)
                        elif event.key in [K_s, K_DOWN]:
                            direction = (0, 1)

                pygame.display.update()

                clock.tick(30)
        play_again = game_over_menu(score)
        if play_again == 'EXIT_GAME':
            break  # Exit the game if the player chooses not to play again
        elif play_again == 'RESTART_GAME':
            continue

    pygame.quit()
