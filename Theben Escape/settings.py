WIDTH, HEIGHT = 1400, 800
FPS = 100
GAP_SIZE = 125
OBSTACLE_SPACING = 100
OBSTACLE_WIDTH = 175
BIRD_SCALE = 0.25
OBSTACLE_SPEED = 20


def generate_FPS(setting):
    if setting == 0:
        return 65
    elif setting == 1:
        return 75
    elif setting == 2:
        return 100
    else:
        return 120


def generate_Gs(setting):
    if setting == 0:
        return 150
    elif setting == 1:
        return 125
    elif setting == 2:
        return 70
    else:
        return 70


def generate_Ob(setting):
    if setting == 0:
        return 200
    elif setting == 1:
        return 175
    elif setting == 2:
        return 75
    else:
        return 50


def generate_speed(setting):
    if setting == 0:
        return 15
    elif setting == 1:
        return 22
    elif setting == 2:
        return 37
    else:
        return 50
