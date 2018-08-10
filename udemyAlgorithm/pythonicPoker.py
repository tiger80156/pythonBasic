from frenchdeck import FrenchDeck, Card

beerCard = Card('7','diamonds')

deck = FrenchDeck()

print(len(deck))

for card in reversed(deck):
    print(card)

# from testing import poker

# y = poker()

# for item in y:
#     print(item)