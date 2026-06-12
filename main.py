import sys, random

deck = [
    'A', '2', '3', '4', '5',
    '6', '7', '8', '9', '10',
    'J', 'Q', 'K'
]

player_hand = []
dealer_hand = []
def deal_cards(carddeck):
    for i in range(2):
        player_hand.append(random.choice(carddeck))
        dealer_hand.append(random.choice(carddeck))

def display_hands(player,dealer):
    print("Dealer:")
    print(dealer[0] + " ?")
    print("Player:")
    print(*player)
    print('Player total: ' + str(hand_value(player_hand)))

def hand_value(hand):
    item_total = 0
    total_aces = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
           item_total += 10
        elif card == 'A':
            item_total += 11
            total_aces += 1
        else:
            item_total += int(card)
    while item_total > 21 and total_aces != 0:
            item_total -= 10
            total_aces -= 1
    else:
        return item_total

def player_turn():
    print('hit or stand')
    choice = input('>')
    if choice == 'hit':
        player_hand.append(random.choice(deck))
        print(*player_hand)
        print('Player total: ' + str(hand_value(player_hand)))
        if hand_value(player_hand) > 21:
            print('you lost!')
            sys.exit()
        while hand_value(player_hand) < 21:
            print('hit or stand')
            choice = input('>')
            if choice == 'hit':
                player_hand.append(random.choice(deck))
                print(*player_hand)
                print('Player total: ' + str(hand_value(player_hand)))
                if hand_value(player_hand) > 21:
                    print('you lost!')
                    sys.exit()
            elif choice == 'stand':
                dealer_turn(dealer_hand)
                return
    elif choice == 'stand':
        dealer_turn(dealer_hand)
    else:
        print('please pick hit or stand')



def dealer_turn(dealersdeck):
    while hand_value(dealersdeck) < 17:
        dealersdeck.append(random.choice(deck))
        print(*dealer_hand)
        print('Player total: ' + str(hand_value(player_hand)))
    determine_winner(player_hand, dealer_hand)

def determine_winner(player, dealer):
    if hand_value(player) == 21:
        print('you win!')
        sys.exit()
    elif hand_value(dealer) < hand_value(player) <= 21:
        print('you win!')
        sys.exit()
    elif hand_value(player) < hand_value(dealer) <=21:
        print('you lose!')
        sys.exit()
    elif hand_value(dealer_hand) > 21:
        print('you win!')
        sys.exit()
    elif hand_value(dealer_hand) == 21 and hand_value(player_hand) == 21:
        print('tie!')
        sys.exit()



print("Welcome to Blackjack!")
# deal cards to player and dealer
deal_cards(deck)
# display player and dealer hand, hide one of the dealer hand cards
display_hands(player_hand,dealer_hand)
# ask player hit or stand
player_turn()
