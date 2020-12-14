import random

suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
cards = []

for suit in suits:
    for rank in ranks:
        #print(f'{rank} of {suit}')     # debug
        card = rank +' of '+ suit
        #print(card)                    # debug
        cards.append(card)

#print(cards)                           # debug
print(f'There are {len(cards)} cards in the deck')
print(cards)
hand = []

while len(hand) < 5:
    hand = random.choices(cards, k=5)
    #cards.remove(hand)
    #cards.remove(hand)
    
    #cards_left = len(cards) - len(player_cards)

print('\nDealing...\n')
print(f'There are {len(cards)} in the deck.')
print('Player has the following cards in their hand:')
print(hand)
