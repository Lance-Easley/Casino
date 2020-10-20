import random
import time

def game():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

    result = ''
    hit_stay = ''
    card1 = cards.pop(random.randint(0, len(cards) - 1))
    card2 = cards.pop(random.randint(0, len(cards) - 1))
    player_cards = [card1, card2]
    score = sum(player_cards)

    if score == 21:
        print("Blackjack!")
        result = 'bj'
        input()
    while hit_stay != 's' and result == '':
        print("Your Cards:")
        print(str(player_cards))
        hit_stay = input("Hit or Stay? ")

        if hit_stay[0].casefold() == 'h':
            add_card = cards.pop(random.randint(0, len(cards) - 1))
            print("You got", add_card)
            player_cards.append(add_card)
            score = sum(player_cards)
        elif hit_stay[0].casefold() == 's':
            hit_stay = 's'
        else:
            print("Invalid Input")

        if score > 21:
            if 11 in player_cards:
                player_cards.remove(11)
                player_cards.append(1)
                score = sum(player_cards)
            else:
                print("Bust")
                result = 'lose'
                input()
    if result == '':
        print("Dealer's Turn")
        time.sleep(1)

        dealer_result = ''
        com_card1 = cards.pop(random.randint(0, len(cards) - 1))
        com_card2 = cards.pop(random.randint(0, len(cards) - 1))
        computer_cards = [com_card1, com_card2]
        com_score = sum(computer_cards)

        print("Dealer Cards:")
        print(str(computer_cards))
        time.sleep(1)

        if com_score == 21:
            print("Dealer Blackjack")
            dealer_result = 'bj'
            time.sleep(1)

        while com_score < 17 and dealer_result == '':
            if com_score < 17:
                add_com_card = cards.pop(random.randint(0, len(cards) - 1))
                print("Dealer got", add_com_card)
                computer_cards.append(add_com_card)
                com_score = sum(computer_cards)
                time.sleep(1)

        if com_score > 21:
            if 11 in computer_cards:
                computer_cards.remove(11)
                computer_cards.append(1)
                com_score = sum(computer_cards)
            else:
                print("Dealer Bust")
                dealer_result = 'lose'
                input()

        if dealer_result != 'lose':
            if score > com_score:
                print("Player Wins")
                result = 'win'
            elif score < com_score:
                print("Dealer Wins")
                result = 'lose'
            else:
                print("Tie")
                result = 'tie'
            input()
        else:
            result = 'win'
    return result

if __name__ == "__main__":
    game()