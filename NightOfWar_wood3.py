import sys
import math

# Jrke's special
# -Kill your enemy soldiers or Have more bucks than your enemy at end of game

def distance(my_x, my_y, opp_x, opp_y):
    return abs(my_x - opp_x) + abs(my_y - opp_y)

class Board:
    map_size = 0
    board = []
    soldierxy = []
    def __init__(self, size):
        Board.map_size = size
        for _y in range(size):
            Board.board.append([0 for _x in range(size)])
            Board.soldierxy.append([0 for _x in range(size)])

    def SetOwnerID(self, block_owner, x, y):
        Board.board[y][x] = block_owner

    def GetOwnerID(self, x, y):
        return (Board.board[y][x])

    def isMovable(self, x, y):
        Move = False
        if 0 <= x < Board.map_size and 0 <= y < Board.map_size:
            if Board.soldierxy[y][x] != 1:
                Move = True
        return Move

    def SetSoldierXY(self, XYList):
        Board.soldierxy = [[0 for _ in range(Board.map_size)] for _ in range(Board.map_size)]
        if len(XYList):
            for tp in XYList:
                x, y = tp
                Board.soldierxy[y][x] = 1



    def PrintBoard(self):
        print("board", file=sys.stderr)
        # print(Board.board, file=sys.stderr)
        for _y in Board.board:
            print(_y, file=sys.stderr)
        for _y in Board.soldierxy:
            print(_y, file=sys.stderr)

class Soldier:
    soldier_count = 0
    _my_id = 0
    my_soldiers = {}
    opp_soldiers = {}

    def __init__(self, count, myid):
        Soldier.soldier_count = count
        Soldier._my_id = myid

    def Update(self):
        for i in range(Soldier.soldier_count):
        # owner_id: owner of the soldier
        # x: This soldier's position x
        # y: This soldier's position y
        # soldier_id: The unique identifier of soldier
        # level: Level of the soldier ignore for first league
        # direction: The side where the soldier is facing 0 = UP, 1 = LEFT , 2 = DOWN, 3 = RIGHT
            owner_id, x, y, soldier_id, level, direction = [int(j) for j in input().split()]
            # my と opp でdict 振り分け
            if owner_id == Soldier._my_id:
                Soldier.my_soldiers[soldier_id] = [owner_id, x, y, level, direction]
            else:
                Soldier.opp_soldiers[soldier_id] = [owner_id, x, y, level, direction]

        print("Soldier dict", file=sys.stderr)
        print(Soldier.my_soldiers, file=sys.stderr)
        print(Soldier.opp_soldiers, file=sys.stderr)

    def GetMySoldierDict(self):
        return Soldier.my_soldiers

    def GetOppSoldierDict(self):
        return Soldier.opp_soldiers

    def GetSoldierXYList(self):
        XYList = []
        #TODO: get xy (my and opp)
        for v in Soldier.my_soldiers.values():
            x = v[1]
            y = v[2]
            XYList.append((x, y))
        for v in Soldier.opp_soldiers.values():
            x = v[1]
            y = v[2]
            XYList.append((x, y))
        print(f"XYList {XYList}", file=sys.stderr)
        return XYList


class NightWar:
    my_id = int(input())
    map_size = int(input())
    board = Board(map_size)
    my_bucks = 0
    opp_bucks = 0
    isAttack = False
    #block_owner = 0
    active_soldier_count = 0
    turn = 1


    def __init__(self):
        print("my_id: ", NightWar.my_id, file=sys.stderr)
        print("map size: ", NightWar.map_size, file=sys.stderr)


    def Update(self):
        print("turn: ", NightWar.turn, file=sys.stderr)
        NightWar.turn += 1
        NightWar.my_bucks = int(input())  # Your Money
        NightWar.opp_bucks = int(input())  # Opponent Money
        print("my_bucks: ", NightWar.my_bucks, file=sys.stderr)
        print("opp_bucks: ", NightWar.opp_bucks, file=sys.stderr)

        # TODO: 関数化
        if NightWar.my_bucks >= 35:
            NightWar.isAttack = True

        for i in range(NightWar.map_size):
            for j in range(NightWar.map_size):
                # block_owner: The playerId of this box owned player
                # x: This block's position x
                # y: This block's position y
                block_owner, x, y = [int(k) for k in input().split()]
                NightWar.board.SetOwnerID(block_owner, x, y)
        NightWar.board.PrintBoard()

        NightWar.active_soldier_count = int(input()) # Total no. of active soldier in the game
        print("active soldier count: ", NightWar.active_soldier_count, file=sys.stderr)
        self.soldiers = Soldier(NightWar.active_soldier_count, NightWar.my_id)
        self.soldiers.Update()
        NightWar.board.SetSoldierXY(self.soldiers.GetSoldierXYList())


    def Game(self):
        self.Update()
        self.Action()

    def Action(self):
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        # print any of actions - WAIT | MOVE <soldierId> <direction> | ATTACK <soldierID> <soldierId to attack on> | LATER > UPGRADE <id> | DEGRADE <opponent id> | SUICIDE <id>

        # move random
        for mysoldid, v in self.soldiers.GetMySoldierDict().items():
            print(f"v = {v}", file=sys.stderr)
            own, x, y, lv, _dir = v
            if NightWar.board.isMovable(x, y + 1):
                print(f"MOVE {mysoldid} DOWN")
            elif NightWar.board.isMovable(x + 1, y):
                print(f"MOVE {mysoldid} RIGHT")
            elif NightWar.board.isMovable(x - 1, y):
                print(f"MOVE {mysoldid} LEFT")
            elif NightWar.board.isMovable(x, y -1):
                print(f"MOVE {mysoldid} UP")
            else:
                print("WAIT")

        #
    def MoveEvaluate(self):
        pass

    def isAttackable(self):
        pass

game = NightWar()

while True:
    game.Game()
