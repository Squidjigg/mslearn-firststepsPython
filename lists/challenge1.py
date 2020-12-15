import random

# define variables
suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []

for suit in suits:
    for rank in ranks:
        #print(f'{rank} of {suit}')     # debug
        card = rank +' of '+ suit
        deck.append(card)

#print(cards)                           # debug
print(f'There are {len(deck)} cards in the deck')
#print(deck)                            # debug

hand = []

# deal out card for hand
while len(hand) < 5:
    hand = random.choices(deck, k=5)
    
    # remove cards dealt from main deck
for card_in_hand in hand:
    deck.remove(card_in_hand)

print('\nDealing...\n')
print(f'There are {len(deck)} in the deck.')
print('Player has the following cards in their hand:')
print(f'{hand}\n')
#print(deck)                            # debug
