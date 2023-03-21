import DotGL
import time
import math
import world
import keyboard
player_speed = 0
level = world.Level("map.txt")
player_angel = 0

def raycast(dist=5):
    pass
def rotate_player(amount):

    player_angel = player_angel + amount
    if player_angle > 360:
        player_angle = player_angle - 360 
    if player_angle < 0:
        player_angle = 360 - player_angle
 
def player_move(player_speed):
    
    new_pos_x = level.player_chords[0] + player_speed*math.cos(player_angel)
    new_pos_y = level.player_chords[1] + player_speed*math.sin(player_angel)

    level.player_chords[0] = new_pos_x
    level.player_chords[1] = new_pos_x

def get_keys():
    try:
        if keyboard.is_pressed('w'):  # if key 'q' is pressed 
            player_speed = 1
        else:
            player_speed = 0
        if keyboard.is_pressed('s'):  # if key 'q' is pressed 
            player_speed = -1
        else:
            player_speed = 0
        if keyboard.is_pressed('d'):  # if key 'q' is pressed 
            rotate_player(5)
        if keyboard.is_pressed('a'):  # if key 'q' is pressed 
            rotate_player(-5)
    except:
        pass

#set up the screen
draw = DotGL.Screen(180, 52, False)
while True:
    player_move(player_speed)
    for n in level.tile_chords:
        draw.pixel(n[0],n[1])
    if level.player_chords[0] < 180 and level.player_chords[0] > -1 and level.player_chords[1] < 52 and level.player_chords[1] > -1:
        draw.pixel(round(level.player_chords[0]),round(level.player_chords[1]),"@")
    draw.update()
    time.sleep(0.1)
    get_keys()
    print(level.player_chords)
    print(player_angel)