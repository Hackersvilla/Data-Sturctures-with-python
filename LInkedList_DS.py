# Data sturcture
# Singular linked list

class Node:

    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:

    def __int__(self):
        self.head = None
    # to add element at the head position on the linked list
    def first_add(self , element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    # to add element at middle of each element
    def add_middle(self , element , position):
        currentNode = self.head
        currentPosition = 0
        while True:
            # to take the value of the current node

            #if user position is equal to the position we get from the loop
            if currentPosition == position :
                newNode = Node(element)
                prevNode.next = newNode
                newNode.next = currentNode
                break
            # after the loop
            prevNode = currentNode
            currentNode  = currentNode.next()
            currentPosition += 1

    # to add element at the end of the linked list
    def last_add(self , element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node

    # tp find the lenght of the linked list
    def lenght_linked_list(self):
        count  = 0
        temp = self.head
        while temp:
            count+=1
            temp = temp.next
        print("The lenght of linked list is ",count)

    ################Delet node in linked list##########
    ## 4 cases deletion
    ## 1- deleting head node
    ## 2- deleting middle node
    ## 3- deleting last node
    ## 4- deleting element search

    ##this one is 4
    def delete(self, key):
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # Unlink the node from linked list
        prev.next = temp.next
        temp = None
    # to print linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':

    list = LinkedList()
    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    list.head.next = second
    second.next  = third

    list.delete(2)
    list.display()
