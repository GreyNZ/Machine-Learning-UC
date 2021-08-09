
def decode(code):
    """
    :param code: 4-tuple of integers representing rectangle in 2D space
    (x1,y1,x2,y2)  first two and the last two elements of each tuple are
    the coordinates of two opposing corners (across a diagonal) of a rectangle.
    :return: corresponding hypothesis funct
    """
    def hypoth_funct(coords):
        x, y = coords
        x1 = min(code[0], code[2])
        y1 = min(code[1], code[3])
        x2 = max(code[0], code[2])
        y2 = max(code[1], code[3])
        result = x1 <= x <= x2 and y1 <= y <= y2
        return result
    return hypoth_funct



import itertools
h = decode((-1, -1, 1, 1))

for x in itertools.product(range(-2, 3), repeat=2):
    print(x, h(x))
x


# (-2, -2) False
# (-2, -1) False
# (-2, 0) False
# (-2, 1) False
# (-2, 2) False
# (-1, -2) False
# (-1, -1) True
# (-1, 0) True
# (-1, 1) True
# (-1, 2) False
# (0, -2) False
# (0, -1) True
# (0, 0) True
# (0, 1) True
# (0, 2) False
# (1, -2) False
# (1, -1) True
# (1, 0) True
# (1, 1) True
# (1, 2) False
# (2, -2) False
# (2, -1) False
# (2, 0) False
# (2, 1) False
# (2, 2) False
