import pygame
import sys
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

images_table = {
    1: "1.png",
    2: "2.png",
    3: "3.png",
    4: "4.png",
    5: "5.png",
    6: "6.png",
    7: "7.png",
    8: "8.png",
}

class Puzzle:
    # Class variables
    window = pygame.display.set_mode((3*40 + 4*5, 3*40 + 4*5))  # 3*3 puzzle + 5 pixels between pieces and board margins
    window.fill(pygame.Color(0,0,0))
    pygame.display.set_caption("8-Puzzle Game")

    pygame.init()


    # Constructor
    def __init__(self, dimension, combination, solution_combination):
        self.dimension = dimension
        self.combination = combination
        self.solution = solution_combination

        moves = ["DOWN", "LEFT", "UP", "LEFT", "UP", "RIGHT", "DOWN", "DOWN"]
        move_index = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if move_index < len(moves):
                self.draw_movement(moves[move_index])
                move_index += 1


    def draw_movement(self, movement):
        empty_space_pos = self.combination.index(0) # Search for the empty space
        animation_time = 2.0    # Time in seconds of the animation
        moving_piece_pos = None

        # We suppose the movement is valid
        moving_number = None
        match movement:
            case "UP":
                moving_number = self.combination[empty_space_pos-3]
                moving_piece_pos = empty_space_pos-3
            case "RIGHT":
                moving_number = self.combination[empty_space_pos+1]
                moving_piece_pos = empty_space_pos+1
            case "DOWN":
                moving_number = self.combination[empty_space_pos+3]
                moving_piece_pos = empty_space_pos+3
            case "LEFT":
                moving_number = self.combination[empty_space_pos-1]
                moving_piece_pos = empty_space_pos-1
            case "NOTHING":
                moving_number = self.combination[empty_space_pos]
                moving_piece_pos = empty_space_pos


        img_moving_piece = pygame.image.load(images_table[moving_number])

        initial_pos_x = (moving_piece_pos % self.dimension[0]) * 45 + 5
        initial_pos_y = (moving_piece_pos // self.dimension[1]) * 45 + 5

        final_pos_x = (empty_space_pos % self.dimension[0]) * 45 + 5
        final_pos_y = (empty_space_pos // self.dimension[1]) * 45 + 5

        start_time = time.time()
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            t = (time.time() - start_time) / animation_time
            if t >= 1:
                break

            # Lineal interpolation: pos = start + (end - start) * t
            x = initial_pos_x + (final_pos_x - initial_pos_x) * t
            y = initial_pos_y + (final_pos_y - initial_pos_y) * t

            # Draw puzzle except for the moving peace
            self.window.fill((0, 0, 0))
            for i, tile in enumerate(self.combination):
                if tile != 0 and tile != moving_number:
                    px = (i % self.dimension[0] * 45) + 5
                    py = (i // self.dimension[1] * 45) + 5
                    self.window.blit(pygame.image.load(images_table[tile]), (px, py))

            # Draw moving peace
            self.window.blit(img_moving_piece, (x, y))

            pygame.display.flip()
            clock.tick(60)  # 60 FPS

        # Logical move of the peace
        combination_list = list(self.combination)
        combination_list[empty_space_pos] = moving_number
        combination_list[moving_piece_pos] = 0
        self.combination = tuple(combination_list)


    i = 0 + 1


















