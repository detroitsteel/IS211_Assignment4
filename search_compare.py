#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Intakes a list and searchs for a character"""

from __future__ import division
import time


def sequential_search(a_list, item):
    """sequential_search Function - intakes a list of objects and a search
    object. The search object will then be compared against the list
    objects and identify if the search object was found in the list object
    and returns True or False.
    Args:
        a_list (list): A list of objects to be searched
        item (int): An int that will be compared against a_list
    Output: True or False 
    Example:
        test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        sequential_search(test_list, 3)
        >>>False
    """
    pos = 0
    found = False
    start_time = time.time()
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end_time = time.time()
    total_time = end_time - start_time
    return (found, total_time)

def ordered_sequential_search(a_list, item):
    """ordered_sequential_search Function - intakes a list of objects
    and a search object. The search object is then  compared against the list
    objects and identify if the search object was found in the list object
    and returns True or False.
    Args:
        a_list (list): A list of objects to be searched
        item (int): An int that will be compared against a_list
    Output: True or False 
    Example:
        test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        ordered_sequential_search(test_list, 3)
        >>>False
    """
    pos = 0
    found = False
    stop = False
    start_time = time.time()
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end_time = time.time()
    total_time = end_time - start_time
    return (found, total_time)

def binary_search_iterative(a_list, item):
    """binary_search_iterative Function - intakes a list of objects and a search
    object. The search object will then be compared against the list
    objects and identify if the search object was found in the list object
    and returns True or False.
    Args:
        a_list (list): A list of objects to be searched
        item (int): An int that will be compared against a_list
    Output: True or False 
    Example:
        test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        sequential_search(test_list, 3)
        >>>False
    """
    first = 0
    last = len(a_list) - 1
    found = False
    start_time = time.time()
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end_time = time.time()
    total_time = end_time - start_time
    return (found, total_time)

def binary_search_recursive(a_list, item):
    """binary_search_recursive Function - intakes a list of objects and a search
    object. The search object will then be compared against the list
    objects and identify if the search object was found in the list object
    and returns True or False.
    Args:
        a_list (list): A list of objects to be searched
        item (int): An int that will be compared against a_list
    Output: True or False 
    Example:
        test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
        binary_search_recursive(test_list, 3)
        >>>False
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
    """Main Function - Takes a list and a search character which is comparedd
    against the list and returns True if found and False if not found.
    Args:
    Output: True or False 
    Example:
        $ python search_compare.py

        >>>Sequential Search on average took  0.0000615 seconds to run 500
        records 0.0002298 to run 1000 records,
        and  0.0005938 to run 2500 records.
    """

    test_list500 = ([sorted([number+1 for number in range(500)])
                     for group in range(100)])
    seq_results_500 = []
    ord_seq_results_500 = []
    bina_srch_iter_results_500 = []
    bina_srch_recu_results_500 = []
    
    test_list1000 = ([sorted([number+1 for number in range(1000)])
                     for group in range(100)])
    seq_results_1000 = []
    ord_seq_results_1000 = []
    bina_srch_iter_results_1000 = []
    bina_srch_recu_results_1000 = []
    
    test_list2500 = ([sorted([number+1 for number in range(2500)])
                     for group in range(100)])
    seq_results_2500 = []
    ord_seq_results_2500 = []
    bina_srch_iter_results_2500 = []
    bina_srch_recu_results_2500 = []
    
    for i in test_list500:
        seq_results_500.append(sequential_search(i, -1))
        ord_seq_results_500.append(ordered_sequential_search(i, -1))
        bina_srch_iter_results_500.append(binary_search_iterative(i, -1))
        bina_srch_recu_results_500.append(binary_search_recursive(i, -1))
    seq_time_avg_500 = ((sum([i[1] for i in seq_results_500])) /
                    (len(seq_results_500)))
    ord_seq_time_avg_500 = ((sum([i[1] for i in ord_seq_results_500]))
                            / (len(ord_seq_results_500)))
    bina_iter_time_avg_500 = ((sum([i[1] for i in bina_srch_iter_results_500]))
                              / (len(bina_srch_iter_results_500)))
    bina_recu_time_avg_500 = ((sum([i[1] for i in bina_srch_recu_results_500]))
                              / (len(bina_srch_recu_results_500)))

    for i in test_list1000:
        seq_results_1000.append(sequential_search(i, -1))
        ord_seq_results_1000.append(ordered_sequential_search(i, -1))
        bina_srch_iter_results_1000.append(binary_search_iterative(i, -1))
        bina_srch_recu_results_1000.append(binary_search_recursive(i, -1))
    seq_time_avg_1000 = ((sum([i[1] for i in seq_results_1000])) /
                    (len(seq_results_1000)))
    ord_seq_time_avg_1000 = ((sum([i[1] for i in ord_seq_results_1000])) /
                    (len(ord_seq_results_1000)))
    bina_iter_time_avg_1000 = ((sum([i[1] for i in bina_srch_iter_results_1000])
                                ) / (len(bina_srch_iter_results_1000)))
    bina_recu_time_avg_1000 = ((sum([i[1] for i in bina_srch_recu_results_1000])
                                ) / (len(bina_srch_recu_results_1000)))

    for i in test_list2500:
        seq_results_2500.append(sequential_search(i, -1))
        ord_seq_results_2500.append(ordered_sequential_search(i, -1))
        bina_srch_iter_results_2500.append(binary_search_iterative(i, -1))
        bina_srch_recu_results_2500.append(binary_search_recursive(i, -1))
    seq_time_avg_2500 = ((sum([i[1] for i in seq_results_2500])) /
                    (len(seq_results_2500)))
    ord_seq_time_avg_2500 = ((sum([i[1] for i in ord_seq_results_2500])) /
                    (len(ord_seq_results_2500)))
    bina_iter_time_avg_2500 = ((sum([i[1] for i in bina_srch_iter_results_2500])
                                ) / (len(bina_srch_iter_results_2500)))
    bina_recu_time_avg_2500 = ((sum([i[1] for i in bina_srch_recu_results_2500])
                                ) / (len(bina_srch_recu_results_2500)))
    print ("Sequential Search on average took %10.7f seconds to run 500 records"
           "%10.7f to run 1000 records, and %10.7f to run 2500 records."
           %(seq_time_avg_500, seq_time_avg_1000, seq_time_avg_2500))
    print ("Ordered Sequential Search on average took %10.7f seconds to run"
           "500 records, %10.7f to run 1000 records"
           ", and %10.7f to run 2500 records."
           %(ord_seq_time_avg_500, ord_seq_time_avg_1000,
             ord_seq_time_avg_2500))
    print ("Binary Iterative Search on average took %10.7f seconds to run"
           "500 records, %10.7f to run 1000 records"
           ", and %10.7f to run 2500 records."
           %(bina_iter_time_avg_500, bina_iter_time_avg_1000,
             bina_iter_time_avg_2500))
    print ("Binary Recursive Search on average took %10.7f seconds to run"
           "500 records, %10.7f to run 1000 records"
           ", and %10.7f to run 2500 records."
           %(bina_recu_time_avg_500, bina_recu_time_avg_1000,
             bina_recu_time_avg_2500))    
main()
