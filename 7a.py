import re
import sys

line_pattern = re.compile(r'^(\w+ \w+) bags contain (no other bags|(\d+ \w+ \w+ bags?,? ?)+)\.$')
contents_pattern = re.compile(r'(\d+) (\w+ \w+) bag')
# child: [parent]
tree = {}
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        line_match = line_pattern.match(line)
        parent_color = line_match.groups()[0]
        contents = line_match.groups()[1]
        if contents == 'no other bags':
            continue
        contents_match = contents_pattern.findall(contents)
        for (count, color) in contents_match:
            if not color in tree:
                tree[color] = []
            tree[color].append(parent_color)

def parents_set(color):
    all_ = set()
    if color in tree:
        for parent in tree[color]:
            all_.add(parent)
            all_.update(parents_set(parent))
    return all_

print(len(parents_set('shiny gold')))