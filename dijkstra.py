from dataclasses import dataclass

class Graph:
    """
    Graph is an object that contains:
        i: list of from's
        j: list of to's
        d: dictionary of distances accessed by tuple [i,j]
        n: number of tubles [i,j]
    """
    def __init__(self, d: dict):
        i = []
        j = []
        n = 0
        for key in d.keys():
            i.append(key[0])
            j.append(key[1])
            n += 1
        self.i = i
        self.j = j
        self.n = n
        self.d = d

    def __str__(self):
        s = ''
        for edge in zip(self.i,self.j):
            i = edge[0]
            j = edge[1]
            s += f'[{i},{j}] {self.d[i,j]}\n' 
        return s.strip()

class Tag:
    """
    Tag is an object that contains:
        d_j: shortest known path distance from node 1 to j
        i: lists of from nodes with distance d_j
    """
    def __init__(self, d_j, i):
        self.d_j = d_j
        self.i = [i]

    def __str__(self):
        s = ''
        for i in self.i:
            s += f'[{self.d_j},{i}]\n\t'
        return s.strip()

# To print the final table
def str_table(table: dict[Tag]):
    s = 'Node --- Tag\n'
    for j in table.keys():
        s += f'{j} --- ' + str(table[j]) + '\n'
    return s

# Algorithm
def iteration(table: dict[Tag], g: Graph, it_i: set):
    """
    A single dijskstra iteration
    Args:
        table: las iteration version
        g: graph to work in
        it_i: the i's that have to be added to the table
    Returns:
        table: updated
        new_it_i: the i's for the next iteration
    """
    new_it_i = set()
    for idx in range(g.n):
        i = g.i[idx]
        if i in it_i:
            j = g.j[idx]
            if j not in table.keys():
                new_it_i.add(j)
            # d_j = d_1i + d_ij 
            d_j = table[i].d_j + g.d[i,j]
            if j not in table.keys() or d_j < table[j].d_j:
                table[j] = Tag(d_j, i)
            elif d_j == table[j].d_j:
                table[j].i.append(i)
    return table, new_it_i

def dijskstra(g: Graph, start: int, it_max: int = 10):
    # it_max: for debugging
    table = {start : Tag(0,0)}
    it_i = [start]
    it = 0
    while len(it_i) > 0 and it < it_max:
        table, it_i = iteration(table, g, it_i)
        it += 1
    return table

if __name__ == '__main__':
    # Testing with class exercises
    d1 = {
        (1,2):100,
        (1,3):30,
        (2,3):20,
        (3,4):10,
        (3,5):60,
        (4,2):15,
        (4,5):50,
    }
    d2 = {
        (1,2):9,
        (1,3):10,
        (2,3):1,
        (2,4):6,
        (2,5):5,
        (3,6):3,
        (4,7):4,
        (5,7):8,
        (6,5):2,
        (6,7):7
    }
    
    g1 = Graph(d=d1) # transform dict of tuples to graph object
    print(g1)
    table = dijskstra(g1,1) # compute algorithm
    print('table:')
    print(str_table(table))
    print('---'*3)
    g2 = Graph(d=d2)
    print(g2)
    table = dijskstra(g2,1)
    print('table:')
    print(str_table(table))