import sys
from collections import deque

# test: 389125467 10 rounds
# input: 925176834 100 rounds

labels, rounds = sys.argv[1:]
labels = deque(int(label) for label in labels)
rounds = int(rounds)
label_max = max(labels)

def move(labels):
    current = labels.popleft()
    picked = labels.popleft(), labels.popleft(), labels.popleft()
    dest_label = current - 1 if current - 1 > 0 else label_max
    while dest_label in picked:
        dest_label = dest_label - 1 if dest_label - 1 > 0 else label_max
    dest_index = labels.index(dest_label)
    labels.insert(dest_index+1, picked[0])
    labels.insert(dest_index+2, picked[1])
    labels.insert(dest_index+3, picked[2])
    labels.append(current)
    return labels

for _ in range(rounds):
    labels = move(labels)

while labels[0] != 1:
    labels.rotate(1)

print(''.join(str(label) for i, label in enumerate(labels) if i > 0))
