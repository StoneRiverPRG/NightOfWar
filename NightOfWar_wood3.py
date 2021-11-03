import sys
import math

# Jrke's special
# -Kill your enemy soldiers or Have more bucks than your enemy at end of game

my_id = int(input())  # Your unique player Id
map_size = int(input())  # the size of map MapSize*MapSize

# game loop
while True:
    my_bucks = int(input())  # Your Money
    opp_bucks = int(input())  # Opponent Money
    for i in range(map_size):
        for j in range(map_size):
            # block_owner: The playerId of this box owned player
            # x: This block's position x
            # y: This block's position y
            block_owner, x, y = [int(k) for k in input().split()]
    active_soldier_count = int(input())  # Total no. of active soldier in the game
    for i in range(active_soldier_count):
        # owner_id: owner of the soldier
        # x: This soldier's position x
        # y: This soldier's position y
        # soldier_id: The unique identifier of soldier
        # level: Level of the soldier ignore for first league
        # direction: The side where the soldier is facing 0 = UP, 1 = LEFT , 2 = DOWN, 3 = RIGHT
        owner_id, x, y, soldier_id, level, direction = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # print any of actions - WAIT | MOVE <soldierId> <direction> | ATTACK <soldierID> <soldierId to attack on> | LATER > UPGRADE <id> | DEGRADE <opponent id> | SUICIDE <id>
    print("WAIT")
