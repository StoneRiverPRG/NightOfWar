import sys
import math

# Jrke's special
# -Kill your enemy soldiers or Have more bucks than your enemy at end of game

def distance(my_x, my_y, opp_x, opp_y):
    return abs(my_x - opp_x) + abs(my_y - opp_y)

class Board:
	map_size = 0
	board = []
	def __init__(self, size):
		Board.map_size = size
		for _y in range(size):
			Board.board.append([0 for _x in range(size)])

	def SetOwnerID(self, block_owner, x, y):
		Board.board[y][x] = block_owner

	def GetOwnerID(self, x, y):
		return (Board.board[y][x])

	def PrintBoard(self):
		print("board", file=sys.stderr)
		# print(Board.board, file=sys.stderr)
		for _y in Board.board:
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
            if owner_id == Soldier._my_id:
                Soldier.my_soldiers[soldier_id] = [owner_id, x, y, level, direction]
            else:
                Soldier.opp_soldiers[soldier_id] = [owner_id, x, y, level, direction]

        print("Soldier dict", file=sys.stderr)
        print(Soldier.my_soldiers, file=sys.stderr)

    def GetSoldierDict(self):
        return Soldier.my_soldiers


class NightWar:
    my_id = int(input())
    map_size = int(input())
    board = Board(map_size)
    my_bucks = 0
    opp_bucks = 0
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


    def Game(self):
        self.Update()
        self.Action()

    def Action(self):
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        # print any of actions - WAIT | MOVE <soldierId> <direction> | ATTACK <soldierID> <soldierId to attack on> | LATER > UPGRADE <id> | DEGRADE <opponent id> | SUICIDE <id>
        print("WAIT")

        #
    def MoveEvaluate(self):
        pass

game = NightWar()

while True:
    game.Game()
