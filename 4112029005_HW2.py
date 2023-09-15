# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 21:21:30 2023

@author: USER
"""

def memory_addressing(page_table,page_size,local_address):
    page_number,offset=divmod(local_address,page_size)
    if page_number in page_table:
        frame_number=page_table[page_number]
        physical_address=frame_number*page_size+offset
        print(f"The physical address is {physical_address}")
    else:
        print("Invalid page number,address translation failed.")

page_table={0:5,1:9,2:14}
page_size = 4096
variable=int(input("邏輯位址為:"))
logical_address = variable
memory_addressing(page_table, page_size, logical_address)
