from utils import get_input
import numpy as np
import tqdm

def upper_bound_geodes(robots, cost, resources, time_left):
    return resources[-1] + robots[-1]*time_left + ((time_left-1)*(time_left)*(time_left+1))//6

def part1(costs, geode_costs):

    quality = 0
    for bp in tqdm.tqdm(range(len(costs))):
        minutes = 24
        robots = np.array([1,0,0,0])
        resources = np.array([0,0,0,0])
        possible_paths = [(robots, resources, minutes, [])]
        max_geodes = 0
        max_costs = [np.max(np.stack(cost), axis=0) for cost in costs]
        total_costs = np.sum(costs[bp],axis=0)

        while possible_paths:

            robots, resources, time, history = possible_paths.pop()
            
            if time<=0:
                max_geodes = max(max_geodes, resources[-1])
                continue

            if upper_bound_geodes(robots, costs[bp], resources, time) < max_geodes:
                continue

            # create new robots
            for i in range(0,4):
                # check if needed robots to create resources
                if np.all((robots>0)|(costs[bp][i]==0)) and not (i!=3 and robots[i] >= max_costs[bp][i]):
                    new_robots = robots.copy()
                    new_resources = resources.copy()
                    new_time = time
                    # while not enough resources, simulate minutes
                    while not (np.all((new_resources-costs[bp][i])>=0)): 
                        new_time -= 1
                        new_resources += new_robots
                        if new_time <= 0:
                            possible_paths.append(
                            (new_robots, new_resources, new_time,
                                history+[(new_robots,new_resources)]))
                            break
                    # enough resources => create robot
                    else:
                        new_robots[i] += 1
                        possible_paths.append(
                            (new_robots, new_resources+robots-costs[bp][i], new_time-1,
                                history+[(new_robots,new_resources)]))
                
        quality += max_geodes*(bp+1)
 
    return quality

def part2(costs, geode_costs):

    geode_list = []
    for bp in tqdm.tqdm(range(3)):

        minutes = 32
        robots = np.array([1,0,0,0])
        resources = np.array([0,0,0,0])
        possible_paths = [(robots, resources, minutes, [])]
        max_geodes = 0
        max_costs = [np.max(np.stack(cost), axis=0) for cost in costs]
        total_costs = np.sum(costs[bp],axis=0)

        while possible_paths:

            robots, resources, time, history = possible_paths.pop()
            
            if time<=0:
                max_geodes = max(max_geodes, resources[-1])
                continue

            if upper_bound_geodes(robots, costs[bp], resources, time) < max_geodes:
                continue

            # create new robots
            for i in range(0,4):
                if np.all((robots>0)|(costs[bp][i]==0)) and not (i!=3 and robots[i] >= max_costs[bp][i]):
                    new_robots = robots.copy()
                    new_resources = resources.copy()
                    new_time = time
                    while not (np.all((new_resources-costs[bp][i])>=0)): 
                        new_time -= 1
                        new_resources += new_robots
                        if new_time <= 0:
                            possible_paths.append(
                            (new_robots, new_resources, new_time,
                                history+[(new_robots,new_resources)]))
                            break
                    else:
                        new_robots[i] += 1
                        possible_paths.append(
                            (new_robots, new_resources+robots-costs[bp][i], new_time-1,
                                history+[(new_robots,new_resources)]))
                

        geode_list.append(max_geodes)
        print(max_geodes)
 
    return np.prod(np.array(geode_list))

def parse_costs(data):
    costs, geode_costs = [], []
    for line in data:
        l = line.split()
        costs.append((np.array([l[6],0,0,0],int),
            np.array([l[12],0,0,0],int),
            np.array([l[18],l[21],0,0],int),
            np.array([l[27],0,l[30],0],int)))
    return costs, geode_costs


if __name__ == "__main__":
    day = 19
    data = get_input(day)
    print(part1(*parse_costs(data)))
    print(part2(*parse_costs(data)))

