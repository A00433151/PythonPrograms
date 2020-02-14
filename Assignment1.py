#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:25:42 2020
Program to Implement Stack & Queue using Python
@author: A00433151
Note: Used a slice syntax to address the issue where the same list is getting mutated across all the program
        Details issue https://stackoverflow.com/questions/35431826/why-does-my-function-overwrite-a-list-passed-as-a-parameter
"""

list_s = [1, 2, 3, 4]   # Static list passed to perform various operations
list_temp1 =list_temp2 = list_s[:]   # Temporary variable used for single operation in stack/queue to either add or remove, using shallow copy of list with slice syntax

def stack(var_list, var_fun, var_item=0):
    '''
    Function created to add or remove element from Stack
    :param var_list: List that is passed for stack function
    :param var_fun: Used to pass either operation to function as 'add' or 'remove' in stack
    :param var_item: Used to pass a new element to add in stack
    :return: returns updated stack to perform remove operation
    '''
    if var_fun == 'add':
        print ("Adding new element to the stack")
        var_list.insert(0, var_item)
        print (var_list)
        return var_list
    if var_fun == 'remove':
        print ("Removing an element from stack")
        print (var_list[1:])
        return

def queue(var_list, var_fun, var_item=0):
    '''
    Function created to add or remove element from Queue
    :param var_list: List that is passed for Queue function
    :param var_fun: Used to pass either operation to function as 'add' or 'remove' in queue
    :param var_item: Used to pass a new element to add in queue
    :return: returns updated queue to perform remove operation
    '''
    if var_fun == 'add':
         print("Adding new element to the queue")
         var_list.append(var_item)
         print(var_list)
         return var_list
    if var_fun == 'remove':
         print("Removing an element from queue")
         print(var_list[1:])
         return

list_temp1 = stack(list_s[:], 'add', 0)
stack(list_temp1, 'remove')
list_temp2 = queue(list_s[:], 'add', 5)
queue(list_temp2, 'remove')