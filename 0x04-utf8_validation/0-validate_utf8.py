#!/usr/bin/python3
'''a method that determines if a given
   data set represents a valid UTF-8 encoding'''


'''def checklead(byte):
    #checks leading byte
    for i in range(8):
        if byte >> (7 - i) == 0b11111111 >> (7 - i) & ~1:
            return i
    return 8'''


def validUTF8(data) -> bool:
    '''Return: True if data is a valid
       UTF-8 encoding, else return False'''
    data = iter(data)
    for holder in data:
        lead_bit_count = bin(holder).index('1')  
        if lead_bit_count == 0:  
            length = 1
        elif lead_bit_count == 2: 
            length = 2
        elif lead_bit_count == 3:  
            length = 3
        elif lead_bit_count == 4:  
            length = 4
        else:
            return False  

        for _ in range(length - 1):
            after = next(data, 0)
            if after == 0 or after >> 6 != 0b10:
                return False  
    return True
