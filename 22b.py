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

prefix = ''
def recursive_combat(decks):
    global prefix
    game_winner = None
    history = set()
    while True:
        # print(prefix, decks)
        if hash(tuple(tuple(deck) for deck in decks)) in history:
            game_winner = 0
            break
        history.add(hash(tuple(tuple(deck) for deck in decks)))

        cards = [deck.popleft() for deck in decks]
        winner = None
        if all(c <= dl for c, dl in zip(cards, (len(d) for d in decks))):
            sub_decks = [deque(d for i, d in enumerate(deck) if i < c) for deck, c in zip(decks, cards)] # inefficient, would rather have a take()
            # print(prefix, 'subgame(')
            prefix = '    ' + prefix
            winner, _ = recursive_combat(sub_decks)
            prefix = prefix[4:]
            # print(prefix, ')')
        else:
            winner = cards.index(max(cards))
        cards = [cards[winner]] + cards[:winner] + cards[winner + 1:]
        decks[winner].extend(cards)

        if any(len(deck) == 0 for deck in decks):
            game_winner = decks.index(max(decks, key=lambda d: len(d)))
            break
    return game_winner, decks
    
game_winner, decks = recursive_combat(decks)
print(sum(c*v for c, v in zip(decks[game_winner], range(len(decks[game_winner]), 0, -1))))