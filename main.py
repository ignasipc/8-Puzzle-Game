from Puzzle import Puzzle
import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

images_table = ()

def main():
    window = pygame.display.set_mode((120, 120))
    window.fill(pygame.Color(WHITE))
    pygame.display.set_caption("8-Puzzle Game")




    dimension = (3,3)   # 3x3 Puzzle
    combination = (3,7,2,5,4,1,6,8,0)
    starting_puzzle_state = Puzzle(dimension, combination)

    Puzzle(dimension, )

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()