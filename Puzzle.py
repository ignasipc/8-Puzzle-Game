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
    def __init__(self, dimension, combination):
        self.dimension = dimension
        self.combination = combination



    def draw(self):
        img = []
        for i in range(self.dimension[0]*self.dimension[1]):
            img[i]=pygame.image.load(images_table[i])
