# from util.stack import Stack

"""
Given a array of number find the next greater no in the right of each element
Example-    Input     12 15 22 09 07 02 18 23 27
            Output    15 22 23 18 18 18 23 27 -1
"""
'''prints element and NGE pair for all elements of arr[] '''


def find_next_greater_ele_in_array(array):
    """
    complexity O(n2)
    :param array:
    :return:
    """
    temp_arr = []
    for i in range(0, len(array)):
        # if i == len(array) - 1:
        #     temp_arr.append(-1)
        nxt = -1
        for j in range(i + 1, len(array)):
            if array[i] < array[j]:
                nxt = array[j]
                break
        temp_arr.append(nxt)
    print(array)
    print(temp_arr)


class Stack(object):

    @staticmethod
    def create_stack():
        stack = []
        return stack

    @staticmethod
    def is_empty(stack):
        return len(stack) == 0

    @staticmethod
    def push(stack, x):
        stack.append(x)

    @staticmethod
    def pop(stack):
        if Stack.is_empty(stack):
            print("Error : stack underflow")
        else:
            return stack.pop()


def find_next_greater_ele_in_array_using_stack(array):
    """
    complexity O(n)
    :param array:
    :return:
    """
    stack = Stack.create_stack()
    ele = 0
    nxt = 0
    temp = []
    # push the first element to stack
    Stack.push(stack, array[0])
    # iterate for rest of the elements
    for i in range(1, len(array), 1):
        nxt = array[i]

        if not Stack.is_empty(stack):
            # if stack is not empty, then pop an element from stack
            ele = Stack.pop(stack)

            '''
            If the popped element is smaller than next, then 
            keep popping while elements are smaller and stack is not empty 
            '''
            while ele < nxt:
                temp.append(nxt)
                if Stack.is_empty(stack):
                    break
                ele = Stack.pop(stack)

            '''If element is greater than next, then push the element back '''
            if ele > nxt:
                Stack.push(stack, ele)
        '''push next to stack so that we can find next greater for it '''
        Stack.push(stack, nxt)

        '''
        After iterating over the loop, the remaining
        elements in stack do not have the next greater
        element, so print -1 for them 
        '''

    while not Stack.is_empty(stack):
        ele = Stack.pop(stack)
        nxt = -1
        temp.append(nxt)

    print(array)
    print(temp)


if __name__ == '__main__':
    arr = [12, 15, 22, 9, 7, 2, 18, 23, 27]
    find_next_greater_ele_in_array(arr)
    find_next_greater_ele_in_array_using_stack(arr)
