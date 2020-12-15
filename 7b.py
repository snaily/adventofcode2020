import re
import sys

line_pattern = re.compile(r'^(\w+ \w+) bags contain (no other bags|(\d+ \w+ \w+ bags?,? ?)+)\.$')
contents_pattern = re.compile(r'(\d+) (\w+ \w+) bag')
# parent: [(count, child)]
tree = {}
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        line_match = line_pattern.match(line)
        parent_color = line_match.groups()[0]
        contents = line_match.groups()[1]
        if contents == 'no other bags':
            continue
        tree[parent_color] = contents_pattern.findall(contents)

def child_sum(color):
    count = 0
    if not color in tree:
        return 0
    for (child_count, child) in tree[color]:
        child_count = int(child_count)
        count += child_count * (1 + child_sum(child))
    return count

print(child_sum('shiny gold'))