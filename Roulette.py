import random
import time
from os import system, name

#used to clear screen
def clear():
    if name == 'nt': 
        _ = system('cls') 

def game():
    spots = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', 
        '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', 
        '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '00', 
        '2TO1(T)', '2TO1(M)', '2TO1(B)', '1ST12', '2ND12', '3RD12', '1TO18', 
        'EVEN', 'RED', 'BLACK', 'ODD', '19TO36', 'C'
    ]
    colors = [
        'N', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'B', 'R', 'B', 'R', 
        'B', 'R', 'B', 'R', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'B', 
        'R', 'B', 'R', 'B', 'R', 'B', 'R'
    ]
    d = [
        '0', '1R', '2B', '3R', '4B', '5R', '6B', '7R', '8B', '9R', '10B', '11B', 
        '12R', '13B', '14R', '15B', '16R', '17B', '18R', '19R', '20B', '21R', 
        '22B', '23R', '24B', '25R', '26B', '27R', '28B', '29B', '30R', '31B', 
        '32R', '33B', '34R', '35B', '36R', '00', '2TO1(T)', '2TO1(M)', '2TO1(B)', 
        '1ST12', '2ND12', '3RD12', '1TO18', 'EVEN', 'RED', 'BLACK', 'ODD', '19TO36'
    ]

    placements = []
    result = []
    bets = []

    placement = ''
    exit_bets = False

    while not exit_bets:
        clear()
        print(f"""
 __________________________________________________________
|  | {d[3]}| {d[6]}| {d[9]}|{d[12]}|{d[15]}|{d[18]}|{d[21]}|{d[24]}|{d[27]}|{d[30]}|{d[33]}|{d[36]}|{d[38]}|
|{d[37]}|---+---+---+---+---+---+---+---+---+---+---+---+-------|
|--| {d[2]}| {d[5]}| {d[8]}|{d[11]}|{d[14]}|{d[17]}|{d[20]}|{d[23]}|{d[26]}|{d[29]}|{d[32]}|{d[35]}|{d[39]}|
|{d[0]} |---+---+---+---+---+---+---+---+---+---+---+---+-------|
|  | {d[1]}| {d[4]}| {d[7]}|{d[10]}|{d[13]}|{d[16]}|{d[19]}|{d[22]}|{d[25]}|{d[28]}|{d[31]}|{d[34]}|{d[40]}|
'--+---------------+---------------+---------------+-------'
   |     {d[41]}     |     {d[42]}     |     {d[43]}     |
   |---------------+---------------+---------------|
   | {d[44]} |  {d[45]} |  {d[46]}  | {d[47]} |  {d[48]}  |{d[49]} |
   '-----------------------------------------------'
    """)
        print(f"You have {sum(bets)} chips in play")
        placement = input("Bets are open. Type c to confirm bets\n")
        placement = placement.upper()
        if placement not in spots:
            print("Spelling Error")
            input()
        elif placement != 'C':
            bet = int(input("How much? "))
            if bet > 0:
                bets.append(bet)
                placements.append(placement)
                place_index = spots.index(placement)
            else:
                print("Bets need to be 1 or more chips")
                input()
                continue
            d[place_index] = 'X'.center(len(d[place_index]))
        else:
            exit_bets = True

    if len(placements) < 1:
        print("No bets placed")
        input()
        exit()

    print("Rolling...")
    time.sleep(1)
    roll = random.randint(0, 38)
    if roll == 38:
        roll = '00'
    print(roll, "\n")

    for placement in placements:
        if placement == str(roll):
            result.append('Number win')
        elif placement == '2TO1(T)':
            if roll in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
                result.append('2to1 win')
            else:
                result.append('Lost')
        elif placement == '2TO1(M)':
            if roll in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
                result.append('2to1 win')
            else:
                result.append('Lost')
        elif placement == '2TO1(B)':
            if roll in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
                result.append('2to1 win')
            else:
                result.append('Lost')
        elif placement == '1ST12':
            if roll in range(1, 13):
                result.append('12 win')
            else:
                result.append('Lost')
        elif placement == '2ND12':
            if roll in range(13, 25):
                result.append('12 win')
            else:
                result.append('Lost')
        elif placement == '3RD12':
            if roll in range(25, 37):
                result.append('12 win')
            else:
                result.append('Lost')
        elif placement == '1TO18':
            if roll in range(1, 19):
                result.append('Half-board win')
            else:
                result.append('Lost')
        elif placement == '19TO36':
            if roll in range(19, 37):
                result.append('Half-board win')
            else:
                result.append('Lost')
        elif placement == 'EVEN':
            if roll in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]:
                result.append('E-O win')
            else:
                result.append('Lost')
        elif placement == 'ODD':
            if roll in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]:
                result.append('E-O win')
            else:
                result.append('Lost')
        elif placement == 'RED' and roll != '00':
            c_index = int(spots[roll])
            if colors[c_index] == 'R':
                result.append('Color win')
            else:
                result.append('Lost')
        elif placement == 'BLACK' and roll != '00':
            c_index = int(spots[roll])
            if colors[c_index] == 'B':
                result.append('Color win')
            else:
                result.append('Lost')
        else:
            result.append('Lost')
    time.sleep(1)

    for i, res in enumerate(result):
        print(f"{placements[i]}, {res}")

    return [result, bets]