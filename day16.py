from utils import get_input
import re
import numpy as np

def get_graph(data):
    d, fr = {}, {}
    for line in data:
        _, node, _, flow_rate, _, neighbors= re.split('Valve | has|=|;|valves |valve ',line)
        ns = re.split(', ', neighbors)
        d[node] = (ns,[1 for x in ns])
        fr[node] = int(flow_rate)
    return simplify_graph(d, fr)

def simplify_graph(d, fr):
    nodes = list(d.keys())

    while np.sum(np.array(list(fr.values()))==0)>1:
        for node in nodes:
            if fr[node]==0 and node!="AA":
                neighbors, weights = d[node][0], d[node][1]

                for i in range(len(neighbors)):
                    idx_i = d[neighbors[i]][0].index(node)
                    prev_weight = d[neighbors[i]][1][idx_i]

                    for j in range(i+1,len(neighbors)):
                        idx_j = d[neighbors[j]][0].index(node)

                        # update connections
                        d[neighbors[i]][0].append(neighbors[j])
                        d[neighbors[j]][0].append(neighbors[i])

                        # update weights
                        new_weight = prev_weight+d[neighbors[j]][1][idx_j]
                        d[neighbors[i]][1].append(new_weight)
                        d[neighbors[j]][1].append(new_weight)

                    d[neighbors[i]][0].pop(idx_i)
                    d[neighbors[i]][1].pop(idx_i)

                del[d[node]]
                del[fr[node]]
            
    return d, fr

def get_adjacency_matrix(d):
    mat = np.zeros((len(d.keys()), len(d.keys())))
    nodes = sorted(d.keys())
    for i, node in enumerate(nodes):
        for n, w in zip(*d[node]):
            mat[i,nodes.index(n)] = w
            mat[nodes.index(n), i] = w
    return mat

def upper_bound_score(fr, d, current_node, current_time_left, open_valves, current_score):
    upper_bound = current_score
    time_left = current_time_left

    for neighbor in fr:
        #print(min(d[neighbor][0]))
        if neighbor not in open_valves:
            if time_left - 1 > 1:
                upper_bound += fr[neighbor]*(time_left-1)
                time_left -= (1 + min(d[neighbor][1]))
    return upper_bound


def part1(data):
    d, fr = get_graph(data)
    mat = get_adjacency_matrix(d)
    nodes = sorted(d.keys())
    fr = dict(sorted(fr.items(), key=lambda item: -item[1]))

    minutes = 30
    possible_paths = [("AA", 30, [], 0)]
    best_score = 0

    while possible_paths:

        current_node, time_left, open_valves, current_score = possible_paths.pop()
        
        if time_left<=1:
            best_score = max(best_score, current_score)
            continue

        if upper_bound_score(fr, d, current_node, time_left, open_valves, current_score) < best_score:
            continue

        for neighbor, distance in zip(*d[current_node]):
            # move to neighbor
            candidate = (neighbor, time_left-distance, 
            open_valves, current_score)
            possible_paths.append(candidate)

        if fr[current_node]!=0 and current_node not in open_valves:
            # open valve
            candidate = (current_node, time_left-1, open_valves+[current_node], 
                current_score+(time_left-1)*fr[current_node])
            possible_paths.append(candidate)

    return best_score

def upper_bound_score_part2(fr, d, current_time, current_e_time, open_valves, current_score):
    upper_bound = current_score
    time = current_time
    e_time = current_e_time

    for node in fr:
        # advance 2!!!
        if node not in open_valves:
            if time >= 0 and e_time >= 0:
                if time >= e_time:
                    upper_bound += max(0,fr[node]*(time-1))
                    time -= 3
                else:
                    upper_bound += max(0,fr[node]*(e_time-1))
                    e_time -= 3
    return upper_bound

def part2(data):
    d, fr = get_graph(data)
    mat = get_adjacency_matrix(d)
    nodes = sorted(d.keys())
    fr = dict(sorted(fr.items(), key=lambda item: -item[1]))

    minutes = 0
    possible_paths = [("AA", 26, "AA", 26, [], 0, []),]
    best_score = 0

    while possible_paths:

        current_node, time, current_e_node, e_time, open_valves, current_score, history = possible_paths.pop()
        
        if (time<=1 and e_time<=1) or len(open_valves)==len(fr)-1:
            if best_score < current_score:
                print(best_score, len(possible_paths), time, e_time, history)
                best_score = max(best_score, current_score)
            continue

        if upper_bound_score_part2(fr, d, time, e_time, open_valves, current_score) < best_score:
            continue

        if e_time > 2 and time > 2:
            # elephant move to neighbor
            for e_neighbor, e_distance in zip(*d[current_e_node]):
                if e_distance<e_time:
                    # human move to neighbor
                    for neighbor, distance in zip(*d[current_node]):
                        if distance<time:
                            candidate = (neighbor, time-distance,
                                e_neighbor, e_time-e_distance,
                                open_valves, current_score,
                                history)
                            possible_paths.append(candidate)
                    # human open valve
                    if fr[current_node]!=0 and current_node not in open_valves:
                        candidate = (current_node, time-1,
                        current_e_node, e_time-1,
                        open_valves+[current_node],
                        current_score+(time-1)*fr[current_node],
                        history+[(27-time,current_node)])
                        possible_paths.append(candidate)

            # elephant open valve     
            if fr[current_e_node]!=0 and current_e_node not in open_valves:
                # human move to neighbor
                for neighbor, distance in zip(*d[current_node]):
                    if distance<time:
                        candidate = (neighbor, time-distance,
                            current_e_node, e_time-1,
                            open_valves+[current_e_node],
                            current_score+(e_time-1)*fr[current_e_node],
                            history+[(27-e_time,current_e_node)])
                        possible_paths.append(candidate)
                # human open valve
                if fr[current_node]!=0 and current_node not in open_valves+[current_e_node]:
                    candidate = (current_node, time-1,
                        current_e_node, e_time-1,
                        open_valves+[current_e_node,current_node],
                        current_score+(time-1)*fr[current_node]+(e_time-1)*fr[current_e_node],
                        history+[(27-e_time,current_e_node),(27-time,current_node)])
                    possible_paths.append(candidate)
        else:
            # elephant move to neighbor
            if e_time >= 2:
                for e_neighbor, e_distance in zip(*d[current_e_node]):
                    if e_distance<e_time:
                        candidate = (current_node, time,
                            e_neighbor, e_time-e_distance,
                            open_valves, current_score,
                            history)
                        possible_paths.append(candidate)
            # human move to neighbor
            if time >= 2:
                for neighbor, distance in zip(*d[current_node]):
                    if distance<time:
                        candidate = (neighbor, time-distance,
                            current_e_node, e_time,
                            open_valves, current_score,
                            history)
                        possible_paths.append(candidate)
            # human open valve
            if time >= 1:    
                if fr[current_node]!=0 and current_node not in open_valves:
                    candidate = (current_node, time-1,
                        current_e_node, e_time,
                        open_valves+[current_node],
                        current_score+(time-1)*fr[current_node],
                        history+[(27-time,current_node)])
                    possible_paths.append(candidate)
            # elephant open valve  
            if e_time >= 1:    
                if fr[current_e_node]!=0 and current_e_node not in open_valves:
                    candidate = (current_node, time,
                        current_e_node, e_time-1,
                        open_valves+[current_e_node],
                        current_score+(e_time-1)*fr[current_e_node],
                        history+[(27-e_time,current_e_node)])
                    possible_paths.append(candidate)

    return best_score


if __name__ == "__main__":
    day = 16
    example_data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()
    data = get_input(day)
    data = example_data
    print(part1(data))
    print(part2(data))

