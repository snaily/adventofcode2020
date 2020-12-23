import sys

labels, rounds = sys.argv[1:]
rounds = int(rounds)
labels = [int(label) for label in labels]
label_max = max(labels)

nodes = {}
tail = None
head = None
while labels:
    label = labels.pop()
    head = [label, head]
    if not tail:
        tail = head
    nodes[label] = head
for label in range(label_max + 1, 1_000_001):
    tail[1] = [label, None]
    tail = tail[1]
    nodes[label] = tail

def move(head, tail):
    current, head = head, head[1]
    one, head = head, head[1]
    two, head = head, head[1]
    three, head = head, head[1]

    dest_label = current[0] - 1 if current[0] - 1 > 0 else 1_000_000
    while dest_label in (one[0], two[0], three[0]):
        dest_label = dest_label - 1 if dest_label - 1 > 0 else 1_000_000
    
    dest = nodes[dest_label]
    dest_next = dest[1]
    three[1] = dest_next
    if dest_next is None:
        tail = three
    two[1] = three
    one[1] = two
    dest[1] = one

    current[1] = None
    tail[1] = current
    tail = current

    return head, tail

for i in range(rounds):
    if not i % 100_000:
        print(i//100_000)
    head, tail = move(head, tail)

# lets hope cup 1 isn't right at the end of the list...
print(nodes[1][1][0] * nodes[1][1][1][0])