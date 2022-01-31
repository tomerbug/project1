import random


#create the file
file = open(r"C:\Users\Tomer\OneDrive\Desktop\Devops\file.txt", "w")
# count = the length of the line
limit = 67
count = 0
for num in range(1, 10):
    ran = int(random.randint(1, 20))
    for i in range(ran):
        if count == limit:
            file.write("\n")
            count = 0
        file.write(f"{num}")
        count += 1
file.write("TREASURE")
count += 5
for numD in range(9, 0, -1):
    ran = int(random.randint(1, 20))
    for i in range(ran):
        if count == limit:
            file.write("\n")
            count = 0
        file.write(f"{numD}")
        count += 1

file.close()
# function that give the player to move forward or backwards
def playerTurn():
    while True:
        move = input("Where you want to move? [1- forward 2-backwards] ")
        if move not in ["1","2"]:
            continue
        leap = input("how many chracters? ")
        try:
             leap = int(leap)
        except:
            print("please enter a number")
            continue
        return  move , leap

with open(r"C:\Users\Tomer\OneDrive\Desktop\Devops\file.txt" , "r") as treasureMap:
    # pos = point of start
    # eof = end of treasureMap
    #moveCount = counts how many tries it took to reach one of the letters in treasure
    pos = 0
    eof = treasureMap.seek(0,2)
    moveCount = 0
    while True:
        move, leap = playerTurn()
        moveCount+= 1
        # checks limits
        if move == "1":
            if (pos +leap)>eof:
                treasureMap.seek((pos + leap) - eof - 1)
                pos = treasureMap.tell()
            else:
                treasureMap.seek(pos +leap)
                pos = treasureMap.tell()
        else:
            if (pos -leap)<0:
                treasureMap.seek(eof - (leap - pos) - 1)
            else:
                treasureMap.seek(pos - leap)
                pos = treasureMap.tell()
        hit = treasureMap.readline(1)
        pos =treasureMap.tell() - 1
        if hit == "T" or hit == "R" or hit == "E" or hit == "A" or hit == "S" or hit == "U" or hit == "R" or hit == "E":
            print(f"you landed on the letter: {hit}")
            print("you win")
            print(f"total moves: {moveCount}")
            break
        else:
            print(f"you hit {hit}")
            print("… again … until hit one of the “TREASURE” letters…")
        treasureMap.seek(pos)