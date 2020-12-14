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
