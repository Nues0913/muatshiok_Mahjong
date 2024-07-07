import random
import copy
from collections import deque

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

    def __repr__(self) -> str:
        return Tile.mahjongTile[self.encode]

    def __str__(self) -> str:
        return Tile.mahjongDic[self.__repr__()]

# class Tiles:
#     def __init__(self, tiles = []):
#         self.__tiles : list[Tile] = copy.deepcopy(tiles)

#     def __len__(self) -> int:
#         return len(self.__tiles)

#     def __str__(self) -> str:
#         tileStr = str()
#         for tile in self.__tiles:
#             tileStr += str(tile)
#         return tileStr

#     def append(self, tile : Tile) -> None:
#         """append a tile to the end of the tiles"""
#         self.__tiles.append(tile)

#     def pop(self, index : int) -> Tile:
#         """remove and return item at index (default last).
#         raises IndexError if list is empty or index is out of range"""
#         return self.__tiles.pop(index)

#     def sort(self) -> None:
#         """sort the list in encode order and return None"""
#         self.__tiles.sort(key=lambda x: x.encode)

class Player:
    def __init__(self, number : int):
        self.number = number
        self.__handTiles : list[Tile] = []
        self.__meldedTiles : list[list[Tile]] = []
        self.__flowerTiles : list[Tile] = []
        self.__targetTile : Tile = None

    def getHandTiles(self) -> list[Tile]:
        """return a deep copy of player's tiles"""
        return copy.deepcopy(self.__handTiles)
    
    def getFlowerTiles(self) -> list[Tile]:
        """return a deep copy of player's flowerTiles"""
        return copy.deepcopy(self.__flowerTiles)
        
    def drawTile(self) -> None:
        while tile.encode > 34:
            self.__flowerTiles.append(tile)
            
        self.__targetTile = tile

    def sortTiles(self) -> None:
        self.__tiles.sort(key=lambda x: x.encode)
        self.__flowerTiles.sort(key=lambda x: x.encode)

class Game:
    def __init__(self, player1, player2, player3, player4):
        self.players : list[Player] = [player1, player2, player3, player4]
        self.__tileWall : deque[Tile] = deque(random.shuffle([Tile(i) for i in range(1,35) for _ in range(4)] + [Tile(i) for i in range(35,43)]))
        self.__tileDiscarded : list[Tile] = []

    def popleftTileWall(self):
        """remove the first index and return the element"""
        return self.__tileWall.popleft()
    
    def popTileWall(self):
        """remove the last index and return the element"""
        return self.__tileWall.pop()
    
    def appendTileDiscarded(self, tile):
        self.__tileDiscarded.append(tile)

    def popTileDiscarded(self):
        return self.__tileDiscarded()



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