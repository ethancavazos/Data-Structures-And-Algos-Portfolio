#  File: ExpressionTree.py

#  Description: We took an expression and evaluated it using a Stack and Tree. 

#  Student's Name: Jennah Rosas

#  Student's UT EID: jnr2324

#  Partner's Name: Ethan Cavazos

#  Partner's UT EID: enc527

#  Course Name: CS 313E

#  Unique Number: 50845 & 50850

#  Date Created: 11/12/2020

#  Date Last Modified: 11/13/2020
import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check what item is on top of the stack without removing it
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class Tree(object):
    def __init__(self):
        self.root = Node(None)

    def create_tree(self, expr):
        parent = Stack()
        current = self.root
        expression = expr.split()

        for token in expression:
            if token == '(':
                parent.push(current)
                current.lChild = Node(None)
                current = current.lChild
            elif token in ['+', '-', '*', '/', '//', '%', '**']:
                current.data = token
                parent.push(current)
                current.rChild = Node(None)
                current = current.rChild
            elif token.isdigit() or '.' in token:
                current.data = token
                current = parent.pop()
            elif token == ')':
                if not parent.isEmpty():
                    current = parent.pop()
                else:
                    break

    def evaluate(self, aNode):
        # if aNode is None:
        #     return 0
        # if aNode.lChild is None and aNode.rChild is None:
        #     return int(aNode.data)

        if aNode.data == '+':
            return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
        elif aNode.data == '-':
            return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
        elif aNode.data == '*':
            return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
        elif aNode.data == '/':
            return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
        elif aNode.data == '//':
            return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
        elif aNode.data == '%':
            return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
        elif aNode.data == '**':
            return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
        elif aNode.data.isdigit() or '.' in aNode.data:
            return eval(aNode.data)

    def pre_order(self, aNode):
        if aNode is not None:
            print(aNode.data, end=' ')
            self.pre_order(aNode.lChild)
            self.pre_order(aNode.rChild)

    def post_order(self, aNode):
        if aNode is not None:
            self.post_order(aNode.lChild)
            self.post_order(aNode.rChild)
            print(aNode.data, end=' ')


def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    # evaluate the expression and print the result
    expr_tree = Tree()
    expr_tree.create_tree(expr)
    print(expr, '=', float(expr_tree.evaluate(expr_tree.root)))
    print()

    # get the prefix version of the expression and print
    print('Prefix Expression:', end=' ')
    expr_tree.pre_order(expr_tree.root)
    print('\n')

    # get the postfix version of the expression and print
    print('Postfix Expression:', end=' ')
    expr_tree.post_order(expr_tree.root)


if __name__ == "__main__":
    main()
