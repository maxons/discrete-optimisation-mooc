#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from operator import attrgetter

from numpy import *
import pandas

Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm
    #return input_data
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])+1
    capacity = int(firstLine[1])+1

    items = []

    for i in range(1, item_count):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    x = zeros(item_count * capacity)
    x = reshape(x, (item_count, capacity))
    
    for ii in range(1, item_count):
        item = items[ii-1]
        for jj in range(capacity):
            if item.weight <= jj :                
                x[ii][jj] = max(x[ii-1][jj], x[ii-1][jj-item.weight]+item.value)
            else : 
                x[ii][jj] = x[ii-1][jj]
    
    best_result = x[item_count-1][capacity-1]
    
    ii = item_count-1
    jj = capacity-1
    ref_val = x[ii][jj]
    
    taken = [0]*len(items)

    in_bag = []
    while ii != 0:
        if ref_val == x[ii-1][jj]:
            ii = ii-1
        else :
            taken[ii-1] = 1
            ref_val = ref_val - items[ii-1].value
            jj = max(where(x[ii-1] == ref_val)[0])    
    
    # prepare the solution in the specified output format
    output_data = str(best_result) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))

    print("item_count: "+str(item_count))
    print("capacity: "+str(capacity))
    print(items)

    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')


