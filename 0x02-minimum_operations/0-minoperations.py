#!/usr/bin/python3
"""a method that  calculates the fewest number of operations needed
   to result in exactly n H characters in the file."""


def minOperations(n: int) -> int:
    '''execute only two operations in
       this file: Copy All and Paste'''
    if n <= 1:
        return 0

    text = 1
    count = 0
    hold = 0
    operator = 0

    while count < n:
        if n % text == 0:
            '''copy operator : this copy all the h's
               in the text and store in hold'''
            operator += 1
            hold = text
        '''the paste operator: this paste what is copied in the text'''
        operator += 1
        text = text + hold
        count = text

    return operator
