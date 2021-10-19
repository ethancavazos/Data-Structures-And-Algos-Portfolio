#  File: BST_Cipher.py

#  Description: A21

#  Student Name: Ethan Cavazos

#  Student UT EID: enc527

#  Partner Name: Jennah Rosas

#  Partner UT EID: jnr2324

#  Course Name: CS 313E

#  Unique Number: 50850 / 50855

#  Date Created: 11/15/2020

#  Date Last Modified: 11/16/2020

class Node (object):
    def __init__(self, data = None):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):

        self.root = None

        for chr in encrypt_str:
            if ord(chr) == 32:
                self.insert(chr)
            elif (ord(chr) >= 97 and ord(chr) <= 122):
                self.insert(chr)
        return


    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):

        newNode = Node(ch)

        if self.root is None:
            self.root = newNode

        else:

            curr = self.root
            par = self.root

            while curr != None:

                par = curr

                if ch == curr.data:
                    break

                elif ch < curr.data:
                    curr = curr.lchild
                else:
                    curr = curr.rchild

            if ch < par.data:
                par.lchild = newNode

            elif ch > par.data:
                par.rchild = newNode

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):

        curr = self.root
        path = ""

        if self.root.data == ch:
            return "*"

        while curr != None:

            if ch == curr.data:
                return path

            elif ch < curr.data:

                path += "<"
                curr = curr.lchild

            elif ch > curr.data:

                path += ">"
                curr = curr.rchild

        return path

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):

        curr = self.root

        for s in st:

            if curr != None:


                if s == "*":
                    return curr.data

                elif s == "<":
                    curr = curr.lchild

                elif s == ">":
                    curr = curr.rchild

            else:
                return ""

        return curr.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):

        st = st.lower()

        enkryptd = ""

        for s in st:

            if (ord(s) == 32 or (ord(s) >= 97 and ord(s) <= 122)):

                path2 = self.search(s)

                enkryptd += path2 + "!"
        final = enkryptd[:-1]
        return final

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):

        st = st.lower()
        dekryptd = ""

        y = st.split("!")

        for i in y:

            dekryptd += self.traverse(i)

        return dekryptd


def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    encrypt_str = encrypt_str.lower()
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
    main()