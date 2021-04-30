import heapq

"""
Rearrange characters in a string such that no two adjacent are same

Input: aaabc 
Output: abaca 


Input: aaabb
Output: ababa 


Input: aa 
Output: Not Possible


Input: aaaabc 
Output: Not Possible

"""


def rearrange_letters(input_str):
    print('Input Str ----', input_str)
    q = []
    my_dict = {}
    output_str = ''
    # making a dictionary of all characters and their frequencies
    for char in input_str:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    # print("Frequencies of char --- ", my_dict)

    # Making a max heap from the items
    for key, value in my_dict.items():
        heapq.heappush(q, (value, key))
        heapq._heapify_max(q)
    prev = (-1, '#')
    # Popping out items from max heap and forming the string
    while q:
        next_item = heapq._heappop_max(q)
        # print("Popping items from Max heap --- ", next_item)
        next_char = next_item[1]
        output_str += next_char
        next_frequency = next_item[0] - 1

        if prev[0] > 0:
            heapq.heappush(q, prev)
            heapq._heapify_max(q)
        prev = (next_frequency, next_char)

    print('output_str', output_str)
    if len(input_str) != len(output_str):
        return print('Not Possible')
    return output_str


rearrange_letters('aaabc')
# abaca

rearrange_letters('aaabb')
# ababa
rearrange_letters('aa')
# Not Possible
rearrange_letters('aaaabc')
# Not Possible
