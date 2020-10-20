import Blackjack
import Roulette
import Slot_Machine
from os import system, name

#used to clear screen
def clear():
    if name == 'nt': 
        _ = system('cls')

chips = 10000

while chips > 0:
    chips = int(chips)
    print('')
    print(f"You have {chips} chips left")
    print('We have Blackjack, Roulette, and Slot Machines.')
    game = input("What game would you like to play? ")
    game.casefold()
    if game == 'dev_yeet':
        chips **= chips
    while game == 'blackjack':
        if chips > 0:
            bet = int(input("Place your bet: "))
            if bet < 1:
                print("Bets need to be 1 or more chips")
            elif bet <= chips:
                chips -= bet
                result = Blackjack.game()
                if result == 'win':
                    chips += (bet * 2)
                elif result == 'tie':
                    chips += bet
                elif result == 'bj':
                    chips += (bet * 2.5)
                if chips > 0:
                    print(f"You have {chips} chips left")
                    again = input("Would you like to play again? [Y/N] ")
                    again.casefold()
                    if again == 'y':
                        game = 'blackjack'
                    else:
                        game = ''
                    clear()
            else:
                print("You do not have that many chips")
        else:
            game = ''

    while game == 'roulette':
        if chips > 0:
            rou_results = Roulette.game()
            rou_bets = rou_results[1]
            rou_res = rou_results[0]
            chips -= sum(rou_bets)
            b_index = 0
            for r in rou_res:
                if r == 'Number win':
                    b_index = rou_res.index('Number win')
                    chips += rou_bets[b_index] * 36
                elif r == '2to1 win':
                    b_index = rou_res.index('2to1 win')
                    chips += rou_bets[b_index] * 3
                elif r == '12 win':
                    b_index = rou_res.index('12 win')
                    chips += rou_bets[b_index] * 3
                elif r == 'Half-board win':
                    b_index = rou_res.index('Half-board win')
                    chips += rou_bets[b_index] * 2
                elif r == 'E-O win':
                    b_index = rou_res.index('E-O win')
                    chips += rou_bets[b_index] * 2
                elif r == 'Color win':
                    b_index = rou_res.index('Color win')
                    chips += rou_bets[b_index] * 2
            if chips > 0:
                    print(f"You have {chips} chips left")
                    again = input("Would you like to play again? [Y/N] ")
                    again.casefold()
                    clear()
                    if again == 'y':
                        game = 'roulette'
                    else:
                        game = ''
        else:
            game = ''

    while game == 'slot machines':
        if chips > 0:
            bet = int(input("How many chips? "))
            if bet < 1:
                print("Bets need to be 1 or more chips")
            elif bet <= chips:
                chips -= bet
                result = Slot_Machine.game()
                if result == '1 cherry':
                    chips += bet // 4
                elif result == '2 cherry':
                    chips += bet // 3
                elif result == '2':
                    chips += bet // 2
                elif result == '2 7':
                    chips += bet
                elif result == 'cherry':
                    chips += bet // 0.8
                elif result == 'orange':
                    chips += bet // 0.7
                elif result == 'bell':
                    chips += bet // 0.6
                elif result == 'grape':
                    chips += bet * 2
                elif result == 'bar':
                    chips += bet * 3
                elif result == '7':
                    chips += bet * 10
                chips = int(chips)
                if chips > 0:
                    print(f"You have {chips} chips left")
                    again = input("Would you like to play again? [Y/N] ")
                    again.casefold()
                    if again == 'y':
                        game = 'slot machines'
                    else:
                        game = ''
                    clear()
            else:
                print("You do not have that many chips")
        else:
            game = ''

print("You are out of chips. Get out of the Casino")
input()