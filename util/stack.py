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
