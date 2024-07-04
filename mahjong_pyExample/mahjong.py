import random

class Tile:
    mahjongTile = (
        "joker",
        "character_1", "character_2", "character_3", "character_4", "character_5", "character_6", "character_7", "character_8", "character_9",
        "dot_1", "dot_2", "dot_3", "dot_4", "dot_5", "dot_6", "dot_7", "dot_8", "dot_9",
        "bamboo_1", "bamboo_2", "bamboo_3", "bamboo_4", "bamboo_5", "bamboo_6", "bamboo_7", "bamboo_8", "bamboo_9",
        "wind_east", "wind_south", "wind_west", "wind_north",
        "dragon_red", "dragon_green", "dragon_white",
        "flower_spring", "flower_summer", "flower_autumn", "flower_winter", "flower_plum", "flower_orchid", "flower_bamboo", "flower_chrysanthemum"
    )
    mahjongDic = {
        "character_1" : "🀇", "character_2" : "🀈", "character_3" : "🀉", "character_4" : "🀊", "character_5" : "🀋",
        "character_6" : "🀌", "character_7" : "🀍", "character_8" : "🀎", "character_9" : "🀏",

        "dot_1" : "🀙", "dot_2" : "🀚", "dot_3" : "🀛", "dot_4" : "🀜", "dot_5" : "🀝",
        "dot_6" : "🀞", "dot_7" : "🀟", "dot_8" : "🀠", "dot_9" : "🀡",

        "bamboo_1" : "🀐", "bamboo_2" : "🀑", "bamboo_3" : "🀒", "bamboo_4" : "🀓", "bamboo_5" : "🀔",
        "bamboo_6" : "🀕", "bamboo_7" : "🀖", "bamboo_8" : "🀗", "bamboo_9" : "🀘",

        "wind_east" : "🀀", "wind_south" : "🀁", "wind_west" : "🀂", "wind_north" : "🀃",

        "dragon_red" : "🀄", "dragon_green" : "🀅", "dragon_white" : "🀆",

        "flower_spring" : "🀦", "flower_summer" : "🀧", "flower_autumn" : "🀨", "flower_winter" : "🀩",
        "flower_plum" : "🀢", "flower_orchid" : "🀣", "flower_bamboo" : "🀤", "flower_chrysanthemum" : "🀥"
    }
    tileUsed = {
        "character_1" : 0, "character_2" : 0, "character_3" : 0, "character_4" : 0, "character_5" : 0,
        "character_6" : 0, "character_7" : 0, "character_8" : 0, "character_9" : 0,

        "dot_1" : 0, "dot_2" : 0, "dot_3" : 0, "dot_4" : 0, "dot_5" : 0,
        "dot_6" : 0, "dot_7" : 0, "dot_8" : 0, "dot_9" : 0,

        "bamboo_1" : 0, "bamboo_2" : 0, "bamboo_3" : 0, "bamboo_4" : 0, "bamboo_5" : 0,
        "bamboo_6" : 0, "bamboo_7" : 0, "bamboo_8" : 0, "bamboo_9" : 0,

        "wind_east" : 0, "wind_south" : 0, "wind_west" : 0, "wind_north" : 0,

        "dragon_red" : 0, "dragon_green" : 0, "dragon_white" : 0,

        "flower_spring" : 0, "flower_summer" : 0, "flower_autumn" : 0, "flower_winter" : 0,
        "flower_plum" : 0, "flower_orchid" : 0, "flower_bamboo" : 0, "flower_chrysanthemum" : 0
    }

    def __init__(self, encode : int):
        self.encode : int = encode
        self.tile : str = Tile.mahjongTile[self.encode]
        self.isLegal = Tile.tileUsedPlusOne(self.tile)

    def setTile(self, encode : int) -> None:
        Tile.tileUsedMinusOne(self.tile)
        self.__init__(encode)

    def getTile(self) -> str:
        return self.tile
    
    @classmethod
    def getTileUsed(cls, encode : int) -> int:
        return cls.tileUsed.get(cls.getTile(encode))

    @classmethod
    def tileUsedPlusOne(cls, tile : str) -> bool:
        curNum = cls.tileUsed.get(tile)
        if(curNum < 4 and curNum != None):
            cls.tileUsed.update({tile : curNum+1})
            return True
        return False
    
    @classmethod
    def tileUsedMinusOne(cls, tile : str) -> bool:
        curNum = cls.tileUsed.get(tile)
        if(curNum > 0 and curNum != None):
            cls.tileUsed.update({tile : curNum-1})
            return True
        return False

class Tiles:
    def __init__(self):
        self.tiles : list[Tile] = []
        self.shuffleTiles()
    
    def sortTile(self) -> None:
        self.tiles.sort(key=lambda x: x.encode)

    def shuffleTiles(self) -> None:
        for i in range(16):
            while(True):
                tile = Tile(random.randint(1,34))
                if(tile.isLegal):
                    self.tiles.append(tile)
                    break
        self.sortTile()
    
    def getTileStrs(self) -> list[str]:
        tileStr = []
        for i in self.tiles:
            tileStr.append(Tile.mahjongDic.get(i.getTile()))
        return tileStr

class Player:
    def __init__(self, number : int):
        self.number = number
        self.tiles = Tiles()

if __name__ == "__main__":
    Peter = Player(1)
    Tom = Player(2)
    Jane = Player(3)
    John = Player(4)
    print(Peter.tiles.getTileStrs())
    print(Tom.tiles.getTileStrs())
    print(Jane.tiles.getTileStrs())
    print(John.tiles.getTileStrs())
    # print(Tiles.Tile.tileUsed)
    '''
    TODO: 只做拿牌，換牌還沒做，抽牌還沒做，吃碰槓胡和玩家交互還沒做
    TODO: only implemented initializing player and tiles, others didn't
    '''