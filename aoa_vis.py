import sys
import math

import pygame

# paste your own angles here
angles = [10, 12, 11, 235, 246, 245]

# styles
class Colour:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)


class Style:
    BACKGROUND = Colour.BLACK
    CENTRE_POINT = Colour.WHITE
    OUTER_CIRCLE = Colour.WHITE
    LINE = Colour.GREEN


pygame.init()

size = width, height = 400, 400
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(Style.BACKGROUND)

    centre = [width / 2, height / 2]
    r = width / 2 - 20
    # draw angles of arrival
    for angle in angles:
        x = centre[0] + (r - 1) * math.sin(math.radians(angle))
        y = centre[1] + (r - 1) * math.cos(math.radians(angle))
        pygame.draw.line(screen, Style.LINE, centre, [x, height - y], 1)

    # draw centre point
    pygame.draw.circle(screen, Style.CENTRE_POINT, centre, 5, 0)

    # draw outer circle
    pygame.draw.circle(screen, Style.OUTER_CIRCLE, centre, r, 1)

    pygame.display.flip()

    clock.tick(60)
