import sys
import re

def rotate_ccw(tile):
    return tuple(tuple(line[i] for line in tile) for i in reversed(range(len(tile))))
def flip_h(tile):
    return tuple(tuple(reversed(line)) for line in tile)

remaining = set()
# one edge -> [id, rest of edges]
edge1 = {}
# two consecutive edges -> (id, remaining edge)
edge2 = {}

N = None
with open(sys.argv[1]) as file:
    tiles = file.read().split('\n\n')
    N = int(len(tiles) ** 0.5)

    for tile in tiles:
        tile = tile.split('\n')
        id_ = int(tile[0][5:-1])
        remaining.add(id_)
        tile = tile[1:]

        edges = []
        edges.append(tuple(tile[0]))# top edge
        edges.append(tuple(line[-1] for line in tile)) # right edge
        edges.append(tuple(reversed(tile[-1]))) # bottom edge
        edges.append(tuple(line[0] for line in tile[::-1])) #left edge

        middle = tuple(line[1:-1] for line in tile[1:-1])
        # middle = tuple(tuple(c
        #     if x == 0 or y == 0 or x == len(tile) - 1 or y == len(tile) - 1
        #     else '^' if x == 2 and y == 1 
        #     else ' '
        #     for x, c in enumerate(line)
        # ) for y,line in enumerate(tile))

        for i in range(4):
            key = (edges[i], )
            edge_list = edge1.get(key, [])
            edge_list.append((id_, (edges[(i+1) % 4], edges[(i+2) % 4], edges[(i+3) % 4]), middle))
            edge1[key] = edge_list
            middle = rotate_ccw(middle)
        for i in range(4):
            key = (edges[i], edges[(i+1) % 4])
            edge_list = edge2.get(key, [])
            edge_list.append((id_, (edges[(i+2) % 4], edges[(i+3) % 4]), middle))
            edge2[key] = edge_list
            middle = rotate_ccw(middle)
        edges = [tuple(reversed(edge)) for edge in edges[::-1]]
        middle = flip_h(rotate_ccw(rotate_ccw(rotate_ccw(middle))))
        for i in range(4):
            key = (edges[i], )
            edge_list = edge1.get(key, [])
            edge_list.append((id_, (edges[(i+1) % 4], edges[(i+2) % 4], edges[(i+3) % 4]), middle))
            edge1[key] = edge_list
            middle = rotate_ccw(middle)
        for i in range(4):
            key = (edges[i], edges[(i+1) % 4])
            edge_list = edge2.get(key, [])
            edge_list.append((id_, (edges[(i+2) % 4], edges[(i+3) % 4]), middle))
            edge2[key] = edge_list
            middle = rotate_ccw(middle)

def solve(N, solution, middles, this_edge, same_row, next_row, remaining):
    n = len(solution)
    if len(remaining) == 0:
        return solution, middles

    candidates = []
    if not this_edge:
        assert n == 0 # only the first tile, generate all orientations
        for top, list_ in edge1.items():
            for id_, (right, bottom, left), middle in list_:
                candidates.append((id_, left, top, right, bottom, middle))
    if len(this_edge) == 1:
        if len(edge1[this_edge]) > 1:
            pass
        for id_, edges, middle in edge1[this_edge]:
            if id_ not in remaining:
                continue
            left, top, right, bottom = (None,) * 4
            if n < N: #first row
                (left) = this_edge
                top, right, bottom = edges
                middle = rotate_ccw(middle)
            elif n % N == 0: #first column
                (top) = this_edge
                right, bottom, left = edges
            else:
                assert "wrong position for one edge"
            candidates.append((id_, left, top, right, bottom, middle))
    if len(this_edge) == 2:
        for id_, edges, middle in edge2.get(this_edge, ()):
            if id_ not in remaining:
                continue
            left, top = this_edge
            right, bottom = edges
            middle = rotate_ccw(middle)
            candidates.append((id_, left, top, right, bottom, middle))
    
    for i, (id_, left, top, right, bottom, middle) in enumerate(candidates):
        next_row_sub = next_row + (bottom[::-1],)
        same_row_sub = same_row
        this_edge_sub = None
        if n % N == N-1: #last column
            same_row_sub = next_row_sub[1:]
            this_edge_sub = next_row_sub[0:1]
            next_row_sub = ()
        else:
            this_edge_sub = (right[::-1],) + same_row_sub[0:1]
            if n >= N:
                same_row_sub = same_row_sub[1:]
        result = solve(
            N,
            solution + (id_,),
            middles + (middle,),
            this_edge_sub,
            same_row_sub,
            next_row_sub,
            remaining - set((id_,)))
        if result != None:
            return result
    return None

solution, middles = solve(N, (), (), (), (), (), remaining)

image = []
for y in range(N):
    for i in range(len(middles[0][0])):
        for x in range(N):
            image.extend(middles[N*y + x][i])
        image.append('\n')

def color_monsters(image):
                  # 
#    ##    ##    ###
 #  #  #  #  #  # 
    w = image.index('\n') + 1
    count = 0
    # monster shape
    js = (0,
        w - 18, w - 18 + 5, w - 18 + 6, w - 18 + 11, w - 18 + 12, w - 18 + 17, w - 18 + 18, w - 18 + 19,
        2*w - 18 + 1, 2*w - 18 + 4, 2*w - 18 + 7, 2*w - 18 + 10, 2*w - 18 + 13, 2*w - 18 + 16)
    # expected newlines
    nls = ((1, w - 18), (w - 18 + 20, 2*w - 18 + 1))
    for i in range(len(image) - max(js)):
        all = True
        for j in js:
            if not (image[i+j] == '#' or image[i+j] == 'O'):
                all = False
        for start, end in nls:
            try:
                image.index('\n', i + start, i + end)
            except ValueError:
                all = False
        if all:
            count += 1
            for j in js:
                image[i+j] = 'O'
    if count:
        return count

def rotate_image(image):
    w = image.index('\n') + 1
    rotated = []
    for x in range(w-1):
        for y in reversed(range(len(image) // w)):
            rotated.append(image[y*w + x])
        rotated.append('\n')
    return rotated

# ew. better hope there are monsters!
rotations = 0
while not color_monsters(image):
    image = rotate_image(image)
    rotations += 1
    if rotations == 4:
        image = list(reversed(image))[1:] + ['\n']

print(''.join(image))

count = 0
for i in range(len(image)):
    if image[i] == '#':
        count += 1

print(count)