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

    def __init__(self, encode : int):
        self.encode : int = encode
        self.tile : str = Tile.mahjongTile[self.encode]

class Tiles:
    def __init__(self):
        self.tiles : list[Tile] = []

    def len(self) -> int:
        return len(self.tiles)

    def copy(self) -> "Tiles":
        copyTiles = Tiles()
        for i in self.tiles:
            copyTiles.append(Tile(i.encode))
        return copyTiles

    def append(self, tile : Tile):
        self.tiles.append(tile)

    def remove(self, tile : Tile):
        for i in range(len(self.tiles)):
            if(self.tiles[i].encode == tile.encode):
                self.tiles.pop(i)
                return
        raise ValueError("tile not found")
    
    def sort(self) -> None:
        self.tiles.sort(key=lambda x: x.encode)
    
    def getTileStrs(self) -> list[str]:
        tileStr = []
        for i in self.tiles:
            tileStr.append(Tile.mahjongDic.get(i.tile))
        return tileStr

class Player:
    def __init__(self, number : int):
        self.number = number
        self.__tiles : Tiles = Tiles()
        self.__flowerTiles : Tiles = Tiles()
        self.__targetTile : Tile = None

    def getFlowerTiles(self) -> Tiles:
        return self.__flowerTiles.copy()

    def getTiles(self) -> Tiles:
        return self.__tiles.copy()
        
    def drawTile(self, tile : Tile) -> None:
        if(tile.encode > 34):
            self.__flowerTiles.append(tile)
            return
        if(self.__tiles.len() < 17):
            self.__tiles.append(tile)
            return
        self.__targetTile = tile

    def sortTiles(self) -> None:
        self.__tiles.sort()
        self.__flowerTiles.sort()

class Game:
    def __init__(self, player1, player2, player3, player4):
        self.players : list[Player] = [player1, player2, player3, player4]
    
    def shuffleAllTiles(self) -> None:
        tiles = [Tile(i) for i in range(1,35) for _ in range(4)]
        tiles.extend([Tile(i) for i in range(35,43)])
        random.shuffle(tiles)
        for player in self.players:
            while(player.getTiles().len() < 16):
                tile = tiles.pop()
                player.drawTile(tile)
            player.sortTiles()



if __name__ == "__main__":
    Peter = Player(1)
    Tom = Player(2)
    Jane = Player(3)
    John = Player(4)
    newGame = Game(Peter, Tom, Jane, John)
    newGame.shuffleAllTiles()
    print("Peter :", Peter.getTiles().getTileStrs())
    print(Peter.getFlowerTiles().getTileStrs())
    print("Tom   :", Tom.getTiles().getTileStrs())
    print(Tom.getFlowerTiles().getTileStrs())
    print("Jane  :", Jane.getTiles().getTileStrs())
    print(Jane.getFlowerTiles().getTileStrs())
    print("John  :", John.getTiles().getTileStrs())
    print(John.getFlowerTiles().getTileStrs())
    # print(Tiles.Tile.tileUsed)
    '''
    TODO: 只做拿牌，換牌還沒做，抽牌還沒做，吃碰槓胡和玩家交互還沒做
    TODO: only implemented initializing player and tiles, others didn't
    TODO: 寫Class method的Docstrings
    TODO: write methods' Docstrings for every classes
    '''