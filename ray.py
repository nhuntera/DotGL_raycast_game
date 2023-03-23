import math
def vector(distance, angle):
    angle = angle*3.14/180
    dx = distance*math.cos(angle)
    dy = distance*math.sin(angle)
    return (dx, dy)

def ray_recurse(x, y, delta):
    newX = float("{:.5f}".format(x + delta[0]))
    newY = float("{:.5f}".format(y + delta[1]))
    return (newX, newY)

def ray(startX, startY, angle, distance=10, resolution=0.01):
    depth = int(distance/resolution)
    x = startX
    y = startY
    delta = vector(resolution, angle)
    chord_list = []
    for i in range(depth):
        new_chords = ray_recurse(x, y, delta)
        x = new_chords[0]
        y = new_chords[1]
        chord_list.append(new_chords)
    return chord_list
