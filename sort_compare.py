#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Intakes a list and sorts the list"""

import time


def insertion_sort(a_list):
    """insertion_sort Function - intakes a list of objects and sorts the list.
    Args:
        a_list (list): A list of objects to be sorted
    Output: a_list sorted and the time it took to sort 
    Example:
        test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        insertion_sort(test_list)
        >>>([0, 1, 2, 8, 13, 17, 19, 32, 42], .000015)
    """
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            a_list[position] = current_value
    end_time = time.time()
    total_time = end_time - start_time
    return (a_list, total_time)

def shell_sort(a_list):
    """Shell Short Function - intakes a list of objects and sorts the list.
    Args:
        a_list (list): A list of objects to be sorted
    Output: a_list sorted and the time it took to sort 
    Example:
        test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        shell_sort(test_list)
        >>>([0, 1, 2, 8, 13, 17, 19, 32, 42], .000015)
    """
    start_time = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end_time = time.time()
    total_time = end_time - start_time
    return (a_list, total_time)

def gap_insertion_sort(a_list, start, gap):
    """gap_insertion_sort Function - intakes a list of objects sorts them
    Args:
        a_list (list): A list of objects to be searched
        start (int): starting position
        gap(int): the gap position of the sort
    Output: a sorted list
    Example:
        test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        gap_insertion_sort(test_list, 3, 2)
        >>>[0, 1, 2, 8, 13, 17, 19, 32, 42,]
    """
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value
    return (a_list)

def python_sort(mycmp):
    """Convert a cmp= function into a key= function

    """
    start_time = time.time()
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    end_time = time.time()
    total_time = end_time - start_time
    return (K, total_time)

def binary_search_recursive(a_list, item):
    """binary_search_recursive Function - intakes a list of objects sorts them
    Args:
        a_list (list): A list of objects to be searched
        item (int): An int that will be compared against a_list
    Output: A sorted list 
    Example:
        test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        binary_search_recursive(test_list, 3)
        >>>[0, 1, 2, 8, 13, 17, 19, 32, 42,]
    """
    start_time = time.time()
    if len(a_list) == 0:
        end_time = time.time()
        total_time = end_time - start_time
        return (False, total_time)
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        end_time = time.time()
        total_time = end_time - start_time
        return (True, total_time)
    else:
        if item < a_list[midpoint]:
            end_time = time.time()
            total_time = end_time - start_time
            return ((binary_search_recursive(a_list[:midpoint], item)
                    , total_time))
        else:
            end_time = time.time()
            total_time = end_time - start_time
            return ((binary_search_recursive(a_list[midpoint + 1:], item)
                    , total_time))
          
def main():
    """Main Function - Tests search and sort functions to identify Bio-O logic.
    Args:
    Output: Facts about the parsed Big-O testing data. 
    Example:
        $ python sort_compare.py
        >>>'Insertion Sort on average took  0.0000675 seconds to run 500 records
        0.0001135 to run 1000 records, and  0.0002669 to run 2500 records...
        """
    test_list500 = ([[number+1 for number in range(500)]
                     for group in range(100)])
    insertion_sort_500 = []
    shell_sort_500 = []
    python_sort_500 = []
    
    test_list1000 = ([[number+1 for number in range(1000)]
                     for group in range(100)])
    insertion_sort_1000 = []
    shell_sort_1000 = []
    python_sort_1000 = []
    
    test_list2500 = ([[number+1 for number in range(2500)]
                      for group in range(100)])
    insertion_sort_2500 = []
    shell_sort_2500 = []
    python_sort_2500 = []
    
    for i in test_list500:
        insertion_sort_500.append(insertion_sort(i))
        shell_sort_500.append(shell_sort(i))
        python_sort_500.append(python_sort(i))
    insertion_sort_avg_500 = ((sum([i[1] for i in insertion_sort_500])) /
                    (len(insertion_sort_500)))
    shell_sort_avg_500 = ((sum([i[1] for i in shell_sort_500]))
                            / (len(shell_sort_500)))
    python_sort_avg_500 = ((sum([i[1] for i in python_sort_500]))
                              / (len(python_sort_500)))

    for i in test_list1000:
        insertion_sort_1000.append(insertion_sort(i))
        shell_sort_1000.append(shell_sort(i))
        python_sort_1000.append(python_sort(i))
    insertion_sort_avg_1000 = ((sum([i[1] for i in insertion_sort_1000])) /
                    (len(insertion_sort_1000)))
    shell_sort_avg_1000 = ((sum([i[1] for i in shell_sort_1000])) /
                    (len(shell_sort_1000)))
    python_sort_avg_1000 = ((sum([i[1] for i in python_sort_1000])
                                ) / (len(python_sort_1000)))

    for i in test_list2500:
        insertion_sort_2500.append(insertion_sort(i))
        shell_sort_2500.append(shell_sort(i))
        python_sort_2500.append(python_sort(i))
    insertion_sort_avg_2500 = ((sum([i[1] for i in insertion_sort_2500])) /
                    (len(insertion_sort_2500)))
    shell_sort_avg_2500 = ((sum([i[1] for i in shell_sort_2500])) /
                    (len(shell_sort_2500)))
    python_sort_avg_2500 = ((sum([i[1] for i in python_sort_2500])
                                ) / (len(python_sort_2500)))
    print ("Insertion Sort on average took %10.7f seconds to run 500 records"
           "%10.7f to run 1000 records, and %10.7f to run 2500 records."
           %(insertion_sort_avg_500, insertion_sort_avg_1000
             , insertion_sort_avg_2500))
    print ("Shell Sort on average took %10.7f seconds to run"
           "500 records, %10.7f to run 1000 records"
           ", and %10.7f to run 2500 records."
           %(shell_sort_avg_500, shell_sort_avg_1000,
             shell_sort_avg_2500))
    print ("Python Sort on average took %10.7f seconds to run"
           "500 records, %10.7f to run 1000 records"
           ", and %10.7f to run 2500 records."
           %(python_sort_avg_500, python_sort_avg_1000,
             python_sort_avg_2500))
 
main()
