from collision import *
STATIC = 1  # Velocity below which an object is considered to be static
MIN_FORCE = 500
MAX_FORCE = 34000


BOARD_SIZE = 800
BOARD_DAMPING = 0.95  # Velocity fall per second

BOARD_WALLS_SIZE = BOARD_SIZE * 2 / 75
WALLS_ELASTICITY = 0.7

COIN_MASS = 1
COIN_RADIUS = 15.01
COIN_ELASTICITY = 0.5

STRIKER_MASS = 2.8
STRIKER_RADIUS = 20.6
STRIKER_ELASTICITY = 0.7

POCKET_RADIUS = 22.51

STRIKER_COLOR = [65, 125, 212]
POCKET_COLOR = [0, 0, 0]
BLACK_COIN_COLOR = [43, 43, 43]
WHITE_COIN_COLOR = [169, 121, 47]
RED_COIN_COLOR = [169, 53, 53]
BOARD_WALLS_COLOR = [56, 32, 12]
BOARD_COLOR = [242, 209, 158]


# Array of initial coin positions
INITIAL = [(399, 368+100), (437, 420+100), (372, 424+100), (336, 366+100), (400, 332+100), (463, 367+100), (464, 434+100), (400, 468+100), (337, 433+100), (400, 400+100), (401, 432+100), (363, 380+100), (428, 376+100),  (370, 350+100), (430, 346+100),
           (470, 400+100), (430, 450+100), (370, 454+100), (330, 400+100), (400, 142+100)]

coins = [
# def __init__(self, mass, pos, radius, color = (0, 0, 0), acceleration = 0, velx = 0, vely = 0, e = 1, number = None):
    obj(10*3, INITIAL[0], 15.01*1.15, (169, 121, 47), 0, 0, 0, 0.5, 0),
    obj(10*3, INITIAL[1], 15.01*1.15, (169, 121, 47), 0, 0, 0, 0.5, 1),
    obj(10*3, INITIAL[2], 15.01*1.15, (169, 121, 47), 0, 0, 0, 0.5, 2),
    obj(10*3, INITIAL[3], 15.01*1.15, (169, 121, 47), 0, 0, 0, 0.5, 3),
    obj(10*3, INITIAL[4], 15.01*1.15, (169, 121, 47), 0, 0, 0, 0.5, 4),
    obj(10*3, INITIAL[5], 15.01*1.15, (169, 121, 47), 0, 0, 0, 0.5, 5),
    obj(10*3, INITIAL[6], 15.01*1.15, (169, 121, 47), 0, 0, 0, 0.5, 6),
    obj(10*3, INITIAL[7], 15.01*1.15, (169, 121, 47), 0, 0, 0, 0.5, 7),
    obj(10*3, INITIAL[8], 15.01*1.15, (169, 121, 47), 0, 0, 0, 0.5, 8),
    obj(10*3, INITIAL[9], 15.01*1.15, (169, 53, 53), 0, 0, 0, 0.5, 9),
    obj(10*3, INITIAL[10], 15.01*1.15, (43, 43, 43), 0, 0, 0, 0.5, 10),
    obj(10*3, INITIAL[11], 15.01*1.15, (43, 43, 43), 0, 0, 0, 0.5, 11),
    obj(10*3, INITIAL[12], 15.01*1.15, (43, 43, 43), 0, 0, 0, 0.5, 12),
    obj(10*3, INITIAL[13], 15.01*1.15, (43, 43, 43), 0, 0, 0, 0.5, 13),
    obj(10*3, INITIAL[14], 15.01*1.15, (43, 43, 43), 0, 0, 0, 0.5, 14),
    obj(10*3, INITIAL[15], 15.01*1.15, (43, 43, 43), 0, 0, 0, 0.5, 15),
    obj(10*3, INITIAL[16], 15.01*1.15, (43, 43, 43), 0, 0, 0, 0.5, 16),
    obj(10*3, INITIAL[17], 15.01*1.15, (43, 43, 43), 0, 0, 0, 0.5, 17),
    obj(10*3, INITIAL[18], 15.01*1.15, (43, 43, 43), 0, 0, 0, 0.5, 18),
    obj(28*1.25, INITIAL[19], 20.6*1.15, (65, 125, 212), 0, 0, 0, 0.7, 19),
]

INITIAL_STATE = {
                 'white': [coins[0], coins[1], coins[2], coins[3], coins[4], coins[5], coins[6], coins[7], coins[8]],
                 'red': [coins[9]],
                 'score': [0,0,0,0],
                 'black': [coins[10], coins[11], coins[12], coins[13], coins[14], coins[15], coins[16], coins[17], coins[18]]
                }
