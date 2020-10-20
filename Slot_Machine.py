import random
import time

def game():
    result = ''

    input("Press Enter to spin ")
    print("Spinning...")
    time.sleep(1)

    slot = [random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)]

    cherries = slot.count(0)
    oranges = slot.count(1)
    bells = slot.count(2)
    grapes = slot.count(3)
    bars = slot.count(4)
    sevens = slot.count(5)

    if slot[0] == slot[1] and slot[1] == slot[2]:
        if 0 in slot:
            result = 'cherry'
        if 1 in slot:
            result = 'orange'
        if 2 in slot:
            result = 'bell'
        if 3 in slot:
            result = 'grape'
        if 4 in slot:
            result = 'bar'
        if 5 in slot:
            result = '7'
    elif oranges == 2:
        result = '2'
    elif bells == 2:
        result = '2'
    elif grapes == 2:
        result = '2'
    elif bars == 2:
        result = '2'
    elif sevens == 2:
        result = '2 7'
    elif cherries == 2:
        result = '2 cherry'
    elif cherries == 1:
        result = '1 cherry'
    else:
        result = 'lost'

    # display logic
    for i, s in enumerate(slot):
        if s == 0:
            slot[i] = 'Cherry'
        elif s == 1:
            slot[i] = 'Orange'
        elif s == 2:
            slot[i] = 'Bell'
        elif s == 3:
            slot[i] = 'Grape'
        elif s == 4:
            slot[i] = 'BAR'
        elif s == 5:
            slot[i] = '7'

    print(".--------.--------.--------. ")
    print('| ', end='')
    for i, s in enumerate(slot):
        print(f'{s.center(6)}', end=' | ')
    print("\n'--------'--------'--------'")
    
    if result == '1 cherry':
        print("Single Cherry")
    elif result == '2 cherry':
        print("Double Cherries")
    elif result == '2':
        print("Doubles")
    elif result == '2 7':
        print("Double 7's!")
    elif result == 'cherry':
        print("Triple Cherries!")
    elif result == 'orange':
        print("Triple Oranges!")
    elif result == 'bell':
        print("Triple Bells!")
    elif result == 'grape':
        print("Triple Grapes!")
    elif result == 'bar':
        print("Triple BAR!")
    elif result == '7':
        print("Triple 7's!")
    else:
        print("You Lost")
    input()

    return result