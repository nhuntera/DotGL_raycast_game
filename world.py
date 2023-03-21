class Level:
    
    size = 100
    origin = (22, 9)
    tiles = []
    tile_chords = []
    player_chords = [22,9]

    def __init__(self, map_txt_file):
        self.map_loader(map_txt_file)
        self.level_map = [[False for i in range(self.size)] for j in range(self.size)]

    def map_loader(self, map_txt_file):
        ypos = 0
        xpos = 0
        f = open(map_txt_file)
        for y in f:
            for x in y:
                if x == "#":
                    self.tiles.append("wall")
                    self.tile_chords.append((xpos,ypos))
                xpos = xpos + 1
            ypos = ypos + 1
            xpos = 0

level = Level("map.txt")
print(level.tiles, " ", level.tile_chords)