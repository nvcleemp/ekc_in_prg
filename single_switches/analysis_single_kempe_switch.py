def print_graph(g):
    for v in g:
        print("{:2d}: {}".format(v, " ".join("{:2d}".format(n) for n in g[v])))

def visit_component(g, c1, c2, v):
    component = []
    current = v
    component.append(current)
    current = g[current][c1]
    component.append(current)
    current = g[current][c2]
    while current!=v:
        component.append(current)
        current = g[current][c1]
        component.append(current)
        current = g[current][c2]
    return component

def components(g, c1, c2):
    seen = []
    components = []
    for v in g:
        if v not in seen:
            component = visit_component(g, c1, c2, v)
            seen = seen + component
            components.append(component)
    return components

def count_perfect(g):
    k = len(g[0])
    count = 0
    for i in range(k-1):
        for j in range(i+1, k):
            if len(components(g, i, j))==1:
                count = count + 1
    return count

def copy_graph(g):
    return {key: value[:] for key, value in g.items()}

def switch_component(g, component, c1, c2):
    for v in component:
        g[v][c1], g[v][c2] = g[v][c2], g[v][c1]

def switching_overview(g):
    k = len(g[0])
    shortest_switch = {}
    for i in range(k-1):
        for j in range(i+1, k):
            comps = components(g, i, j)
            if len(comps)>1:
                for comp in comps:
                    copy = copy_graph(g)
                    switch_component(copy, comp, i, j)
                    count = count_perfect(copy)
                    print("{},{}: Switching {} gives {} perfect pairs".format(i, j, comp, count))
                    if count in shortest_switch:
                        if len(comp) < len(shortest_switch[count]):
                            shortest_switch[count] = comp
                    else:
                        shortest_switch[count] = comp
    print("Shortest switches:")
    for count in shortest_switch:
        print("{:2d}: {}".format(count, shortest_switch[count]))

def analyse(g):
    k = len(g[0])
    print("Current colouring:")
    print_graph(g)
    print("2-factors for each colour pair:")
    for i in range(k-1):
        for j in range(i+1, k):
            print("{},{}: {}".format(i,j,components(g,i,j)))

    print("Perfect pair count in original: {}".format(count_perfect(g)))

    print("Effect of single Kempe switches:")
    switching_overview(g)
    print()

import sys

g = {}

for l in sys.stdin:
    if l.startswith('From'):
       if g:
           analyse(g)
       g = {}
       continue 
    if not l.strip():
        continue
    if ":" in l:
        v, neighs = l.split(":")
        g[int(v)] = [int(n) for n in neighs.split()]
    if l.startswith('Overview'):
        break

if g:
    analyse(g)
