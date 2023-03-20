class Level:
    
    size = 100
    origin = (0, 0)

    def __init__(self, map_txt_file):
        map_loader(map_txt_file)
        self.level_map = [[False for i in range(self.size)] for j in range(self.size)]

    def map_loader(self, map_txt_file):
        f = open(map_txt_file)
        for y in f:
            level_map.append([])
            for x in y:
