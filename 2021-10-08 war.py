import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cardp_1 = []
cardp_2 = []
orderOfWonCards = []
rounds = 0
cardsForTheWinner = []
cardOrder = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "10":9, "J":11, "Q":12, "K":13, "A":14}
pat = 0

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1.append(input())  # the n cards of player 1
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2.append(input())  # the m cards of player 2

def card_value(card):
    if card[0] != "1":
        return cardOrder[card[0]]
    else:
        return cardOrder[card[:2]]

def wars():
    global cardp_1, cardp_2, pat
    if len(cardp_1) <= 5 or len(cardp_2) <= 5:
        print("PAT")
        pat = 1
    else:
        card1 = cardp_1[len(cardp_1)-5]
        card2 = cardp_2[len(cardp_2)-5]
        for i in range(5):
            cardsForTheWinner.append(cardp_1.pop(len(cardp_1)-1-i))
        for i in range(5):
            cardsForTheWinner.append(cardp_2.pop(len(cardp_2)-1-i))
        if card1 == card2:
            wars()
        elif card1 > card2:
            cardp_1 = cardsForTheWinner + cardp_1
            print(cardp_1, file=sys.stderr, flush=True)
        else:
            cardp_2 = cardsForTheWinner + cardp_2
            print(cardp_2, file=sys.stderr, flush=True)

while(len(cardp_1) > 0 and len(cardp_2) > 0 and pat != 1):
    print(rounds + 1, file=sys.stderr, flush=True)
    print(cardp_1, file=sys.stderr, flush=True)
    print(cardp_2, file=sys.stderr, flush=True)
    if card_value(cardp_1[len(cardp_1)-1]) == card_value(cardp_2[len(cardp_2)-1]):
        wars()
        cardsForTheWinner.clear()
    elif card_value(cardp_1[len(cardp_1)-1]) > card_value(cardp_2[len(cardp_2)-1]):
        cardp_1 = [cardp_1.pop(len(cardp_1)-1)] + cardp_1
        cardp_1 = [cardp_2.pop(len(cardp_2)-1)] + cardp_1
    else:
        cardp_2 = [cardp_2.pop(len(cardp_2)-1)] + cardp_2
        cardp_2 = [cardp_1.pop(len(cardp_1)-1)] + cardp_2
    
    rounds += 1

if pat != 1:
    winner = "2 " if len(cardp_1) == 0 else "1 "
    print(winner + str(rounds))
