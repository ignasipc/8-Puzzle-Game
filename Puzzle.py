import pygame
import sys

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


        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #if event == movement -> draw movement


    def draw(self):
        img = []
        for i in range(self.dimension[0]*self.dimension[1]):
            if self.combination[i] != 0:
                img.append(pygame.image.load(images_table[self.combination[i]]))
            else:
                img.append(None)

        displacement_row = 5
        for row in range(self.dimension[0]):
            displacement_col = 5
            for column in range(self.dimension[1]):
                try:
                    self.window.blit(img[column+row*3], (column*40 + displacement_col, row*40 + displacement_row))
                except Exception:
                    continue
                displacement_col += 5
            displacement_row += 5

        pygame.display.flip()


    def draw_movement(self, movement):
        empty_space_pos = self.search_empty_space()
        animation_time = 2.0    # Time in seconds of the animation
        img_moving_piece = None
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


        img_moving_piece = pygame.image.load(images_table[moving_number])

        initial_pos_x = moving_piece_pos % self.dimension[0] * 45 + 5
        initial_pos_y = moving_piece_pos // self.dimension[1] * 45 + 5





    3,7,2,5,4,0,6,8,1

    3,7,2
    5,4,0
    6,8,1



    def search_empty_space(self) -> int :
        """
        :return: Position of empty space in puzzle array
        """
        return self.combination.index(0)





















