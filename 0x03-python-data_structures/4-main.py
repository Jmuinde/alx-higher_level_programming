#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 7,3,4,6,9,10]
idx = 4
new_element = 50
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
