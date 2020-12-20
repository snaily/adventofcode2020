import sys

remaining = set()
# one edge -> [id, rest of edges]
edge1 = {}
# two consecutive edges -> (id, remaining edge)
edge2 = {}

N = None
with open(sys.argv[1]) as file:
    tiles = file.read().split('\n\n')
    N = int(len(tiles) ** 0.5)
    print(N)

    for tile in tiles:
        tile = tile.split('\n')
        id_ = int(tile[0][5:-1])
        remaining.add(id_)
        tile = tile[1:]

        edges = []
        edges.append(tuple(tile[0],))# top edge
        edges.append(tuple(line[-1] for line in tile)) # right edge
        edges.append(tuple(reversed(tile[-1]))) # bottom edge
        edges.append(tuple(line[0] for line in tile[::-1])) #left edge

        for i in range(4):
            key = (edges[i], )
            edge_list = edge1.get(key, [])
            edge_list.append((id_, (edges[(i+1) % 4], edges[(i+2) % 4], edges[(i+3) % 4])))
            edge1[key] = edge_list
        for i in range(4):
            key = (edges[i], edges[(i+1) % 4])
            edge_list = edge2.get(key, [])
            edge_list.append((id_, (edges[(i+2) % 4], edges[(i+3) % 4])))
            edge2[key] = edge_list
        edges = [tuple(reversed(edge)) for edge in edges[::-1]]
        for i in range(4):
            key = (edges[i], )
            edge_list = edge1.get(key, [])
            edge_list.append((id_, (edges[(i+1) % 4], edges[(i+2) % 4], edges[(i+3) % 4])))
            edge1[key] = edge_list
        for i in range(4):
            key = (edges[i], edges[(i+1) % 4])
            edge_list = edge2.get(key, [])
            edge_list.append((id_, (edges[(i+2) % 4], edges[(i+3) % 4])))
            edge2[key] = edge_list

def solve(N, solution, this_edge, same_row, next_row, remaining):
    n = len(solution)
    if n == N*N - 1:
        print(solution, this_edge, same_row, next_row, remaining)
    if len(remaining) == 0:
        return solution

    candidates = []
    if not this_edge:
        assert n == 0 # only the first tile, generate all orientations
        for left, list_ in edge1.items():
            for id_, (top, right, bottom) in list_:
                candidates.append((id_, left, top, right, bottom))
    if len(this_edge) == 1:
        if len(edge1[this_edge]) > 1:
            pass
        for id_, edges in edge1[this_edge]:
            if id_ not in remaining:
                continue
            left, top, right, bottom = (None,) * 4
            if n < N: #first row
                (left) = this_edge
                top, right, bottom = edges
            elif n % N == 0: #first column
                (top) = this_edge
                right, bottom, left = edges
            else:
                assert "wrong position for one edge"
            candidates.append((id_, left, top, right, bottom))
    if len(this_edge) == 2:
        if n == N*N - 1:
            print(edge2.get(this_edge, ()))
        for id_, edges in edge2.get(this_edge, ()):
            if id_ not in remaining:
                continue
            left, top = this_edge
            right, bottom = edges
            candidates.append((id_, left, top, right, bottom))
    
    for i, (id_, left, top, right, bottom) in enumerate(candidates):
        print(f'{n}: {i} of {len(candidates)}: trying {id_} on {solution}')
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
            this_edge_sub,
            same_row_sub,
            next_row_sub,
            remaining - set((id_,)))
        if result != None:
            return result
    return None

solution = solve(N, (), (), (), (), remaining)
print(solution[0] * solution[N-1] * solution[-N] * solution[-1])