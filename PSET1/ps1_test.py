###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit= 20):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    new_cows = list(cows.items())
    cows_Copy = []

    while new_cows:
        minimum = new_cows[0]
        for i in new_cows: 
            if i[1] < minimum[1]:
                minimum = i
        cows_Copy.append(minimum)
        new_cows.remove(minimum)        

    cows_Copy.reverse()
    cows_copy_vals = []
    cows_copy_keys = []
    
    for copy in cows_Copy:    
        cows_copy_vals.append(copy[1])
        cows_copy_keys.append(copy[0])
    
    total_trip = []
    
    while len(cows_copy_vals) > 0:
        if cows_copy_vals[-1] <= limit:
            trip_items = []
            trip_vals = []
            trip_keys = []
            
            for item in cows_Copy:
                if sum(trip_vals) + item[1] <= limit:
                    trip_vals.append(item[1])
                    trip_keys.append(item[0])
                    trip_items.append(item)
            
            for key in trip_items:
                if key[0] in cows_copy_keys:
                    cows_Copy.remove(key)
                    cows_copy_vals.remove(key[1])
                    cows_copy_keys.remove(key[0])
                    
            total_trip.append(trip_keys)
            
    else:
        return total_trip


# Problem 2
def brute_force_cow_transport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    possible_combinations = []
    
    for partition in get_partitions(cows.keys()):
        possible_combinations.append(partition)
    
    possible_combinations.sort(key=len)
    valid_combinations = possible_combinations.copy()

    for partition in possible_combinations:
        for trip in partition:
            total = sum([cows.get(cow) for cow in trip])
            if total > limit:
                valid_combinations.remove(partition)
                break

    return min(valid_combinations, key=len)

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    print("")
    print("GREEDY ALGORITHM")
    print("----------------")
    print(greedy_cow_transport(cows, limit))
    end = time.time()
    print("")
    print("time to compute:", end - start)
    print("")
    print("")
    print("BRUTE FORCE ALGORITHM")
    print("---------------------")
    start2 = time.time()
    print(brute_force_cow_transport(cows, limit))
    end2 = time.time()
    print("")
    print("time to compute:", end2 - start2)
    
    


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
# print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms()
