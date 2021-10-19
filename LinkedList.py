#  File: TestLinkedList.py

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 11/05/2020

#  Date Last Modified: 11/08/2020
class Link(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next


class LinkedList(object):
    # create a linked list
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        curr = self.first
        linkCount = 0

        if curr is None:
            return 0
        else:
            while curr.next != None:
                linkCount += 1

                curr = curr.next

            #account for last link curr.next = None
            linkCount += 1
            return linkCount


    # add an item at the beginning of the list
    def insert_first(self, data):

        curr = self.first
        newFirst = Link(data)

        if curr is None:
            self.first = newFirst
        else:
            newFirst.next = curr
            self.first = newFirst


    # add an item at the end of a list
    def insert_last(self, data):

        curr = self.first
        newLast = Link(data)

        if curr is None:
            self.first = newLast
            return
        else:

            while curr.next != None:
                curr = curr.next
            curr.next = newLast

    # add an item in an ordered list in ascending order
    ###############REDO######################################
    def insert_in_order(self, data):

        curr = self.first
        prev = self.first
        newLink = Link(data)

        if curr == None or data < curr.data:
            self.first = newLink
            return

        while data < curr.data:
            prev = curr
            curr = curr.next
        prev.next = newLink
        newLink.next = curr
        return

        # elif curr.data > data:
        #     newLink.next = curr
        #     self.first = newLink
        #
        # else:
        #     while curr.data < newLink.data:
        #         prev = curr
        #         curr = curr.next
        #     prev.next = newLink
        #     newLink.next = curr


    # search in an unordered list, return None if not found
    def find_unordered(self, data):

        curr = self.first
        # newLink = Link(data)

        if curr is None:
            return None
        else:
            while curr.next is not None:
                if curr.data == data:
                    return data
                curr = curr.next

            #last link next is none, check that
            if curr.data == data:
                return data
            return None

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):

        curr = self.first:

        if curr is None:
            return None
        else:
            while curr.data != data and curr.next != None:
                curr = curr.next

            #check last link whoel .next is None
            if curr.data == data:
                return data
            return None


    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):

        # curr = self.first
        #
        # if curr is None:
        #     return None
        #
        # else:
        #     while curr.data != data and curr.next != None:
        #         prev = curr
        #         curr = curr.next
        #
        #     if curr.data == data:
        #         prev.next = curr.next
        #         curr.next = None
        #         return curr
        #     return None

        current = self.first
        previous = self.first

        if (current is None):
            return None

        while (current.data is not data):
            if (current.next is None):
                return None
            else:
                previous = current
                current = current.next

        if (current == self.first):
             self.first = self.first.next
        else:
            previous.next = current.next

        return current


    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):

        current = self.first
        if (current == None):
            return None

        while current.next != None:

            for i in range(1, 11):
                if current != None:

                    if current.next == None:
                        print(current.data)
                        return ('')
                    else:

                        if i == 10:
                            print(current.data)
                            current = current.next
                        else:
                            print(current.data, '  ', end='')
                            current = current.next

    # Copy the contents of a list and return new list
    def copy_list(self):

        copy = LinkedList()
        curr = self.first

        while curr is not None:
            copy.insert_last(curr.data)
            curr = curr.next
        return copy


    # Reverse the contents of a list and return new list
    def reverse_list(self):

        last = None
        curr = self.first

        while (curr != None):

            next = curr.next
            curr.next = last

            last = curr
            curr = next

        self.first = last
        return



    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):

        curr = self.first
        copy = LinkedList()

        if curr is None or self.is_empty():
            return copy
        while curr.next != None:
            copy.insert_in_order(curr.data)
            curr = curr.next
        #last link
        copy.insert_in_order(curr.data)
        return copy


    ##########redo
    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):

        curr = self.first

        while curr != None and curr.next != None and curr.data < curr.next.data:
            curr = curr.next

        #checks last link
        if curr.data > curr.next.data:
            return False
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):

        if self.first == None:
            return True
        return False

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):

        curr = self.first
        otherCurr = other.first

        mergedList = self.copy_list()
        mergedList = self.sort_list()

        if self.is_empty():
            if other.is_empty():
                return mergedList
            mergedList = other.copy_list()
            return mergedList
        elif other.is_empty():
            mergedList = other.copy_list()
            return mergedList

        else:
            while otherCurr != None and otherCurr.next != None:
                    mergedList.insert_in_order(otherCurr.data)
                    otherCurr = otherCurr.next

            #last link
            mergedList.insert_in_order(otherCurr.data)
            return mergedList




    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):

        curr = self.first
        otherCurr = other.first

        if curr == None or otherCUrr == None:
            return False
        else:
            while curr.data == otherCurr.data and curr.next != None and otherCUrr.next != None:
                curr = curr.next
                otherCurr = otherCurr.next

            if curr.next != None or otherCurr.next != None:
                return False
            return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):

        newList = LinkedList()
        cheatList = []

        curr = self.first

        if curr is None:
            return
        while curr != None:
            cheatList.append(curr.data)

        #removes duplicates
        cheatList = set(cheatList)
        cheatList = list(cheatList)

        for i in cheatList:
            newList.insert_last(i)

        return newList




def main():
  # Test methods addFirst() and __str__() by adding more than 10 items to a list and printing it.
  print("Testing addFirst() & __str__().")
  test = LinkedList()
  for i in range (0, 10):
    test.addFirst(i)
  print(test)
  print("\n")

  # Test method addLast()
  print("Testing addLast().")
  for i in range (10, 20):
    test.addLast(i)
  print(test)
  print("\n")

  # Test method addInOrder()
  print("Testing addInOrder().")
  for i in range (30, 20, -1):
    test.addInOrder(i)
  print(test)
  print("\n")

  # Test method getNumLinks()
  print("Testing getNumLinks().")
  print(test.getNumLinks())
  print("\n")

  # Test method findUnordered()
  # Consider two cases - item is there, item is not there
  print("Testing findUnordered().")
  print(test.findUnordered(29))
  print (test.findUnordered(35))
  print("\n")

  # Test method findOrdered()
  # Consider two cases - item is there, item is not there
  print("Testing findOrdered().")
  print(test.findOrdered(15))
  print(test.findOrdered(36))
  print("\n")

  # Test method delete()
  # Consider two cases - item is there, item is not there
  print("Testing delete().")
  print(test.delete(1))
  print(test.delete(100))
  print("\n")

  # Test method copyList()
  print("Testing copyList().")
  print(test.copyList())
  print("\n")

  # Test method reverseList()
  print("Testing reverseList().")
  print(test.reverseList())
  print("\n")

  # Test method sortList()
  print("Testing sortList().")
  print(test.sortList())
  print("\n")

  # Test method isSorted()
  # Consider two cases - list is sorted, list is not sorted
  print("Testing isSorted().")
  print(test.isSorted())
  test2 = LinkedList()
  test2.addFirst(50)
  test2.addFirst(45)
  print(test2)
  print("\n")

  # Test method isEmpty()
  print("Testing isEmpty().")
  test3 = LinkedList()
  print(test.isEmpty())
  print("test3: " + str(test3.isEmpty()))
  print("\n")

  # Test method mergeList()
  print("Testing method mergeList().")
  test4 = LinkedList()
  for i in range (35, 45, 2):
    test4.addLast(i)
  test5 = LinkedList()
  for i in range (40, 50, 2):
    test5.addLast(i)

  merged = test4.mergeList(test5)
  print(merged)
  print("\n")

  # Test method isEqual()
  # Consider two cases - lists are equal, lists are not equal
  print("Testing isEqual().")
  print(test4.isEqual(test4))
  print(test4.isEqual(test5))
  print("\n")

  # Test removeDuplicates()
  print("Testing removeDuplicates().")
  test6 = LinkedList()
  for i in range (1, 10):
    test6.addLast(1)
    test6.addLast(2)
  removed = test6.removeDuplicates()
  print(removed)
  print("\n")

main()    main()
