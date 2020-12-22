import sys
from collections import deque

decks = []
with open(sys.argv[1]) as file:
    deck = deque()
    decks.append(deck)  
    for line in file:
        if line == '\n':
            deck = deque()
            decks.append(deck)
            continue
        if line.startswith('Player'):
            continue
        deck.append(int(line))

while not any(len(deck) == 0 for deck in decks):
    cards = [deck.popleft() for deck in decks]
    winner = cards.index(max(cards))
    cards.sort(reverse=True)
    decks[winner].extend(cards)

print(decks)
decks.sort(key=lambda d: len(d))
print(decks)
print(sum(c*v for c, v in zip(decks[-1], range(len(decks[-1]), 0, -1))))