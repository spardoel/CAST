# This will be a linked list object containing Element Objects. 
from element import Element

class Routine:
    def __init__(self, first_element:Element = None):
        self._head = None

        if first_element != None:
            self.insertAtBegin(first_element) # could just set directly


        # TODO allow routine to be built all at once?


    def insertAtBegin(self, new_element:Element = None):
        # TODO consider whether to unpack the dictionary or make a function in the Eleemnt class that unpacks it (probbably best)
        if self._head is None:
            self._head = new_element
            return
        else:
            # new element points to the old head, and the new head is the new element
            new_element.next = self._head
            self._head = new_element


    def insertAtEnd(self, new_element:Element = None):
        # TODO consider whether to unpack the dictionary or make a function in the Eleemnt class that unpacks it (probbably best)
        if self._head is None:
            self.insertAtBegin(new_element)
            return
        
        #starting from head, find the last node
        current_node = self.head
        while(current_node.next is not None):
            current_node = current_node.next

        current_node.next = new_element



    def insertAtIndex(self, new_element:Element, index:int=0):

        if (index == 0):
            self.insertAtBegin(new_element)
            return

        position = 0
        current_element = self._head
        # loop until we get to the node before the index
        while (current_element != None and position+1 != index):
            position = position+1
            current_element = current_element.next

        # add the new node at the index
        if current_element != None:
            new_element.next = current_element.next
            current_element.next = new_element
        else:
            print("Index not present")

    def remove_first_element(self):
        if(self._head == None):
            return
        # point head to the next node (ignores the first node, which will be deleted by the garbage collector)
        self._head = self._head.next

    def remove_element(self, element_to_remove):
        current_node = self._head

        # Check if the head node is the one to be removed
        if current_node is not None and current_node.id == element_to_remove.id:
            self.remove_first_element()  # This would handle removal of the first element
            return

        # Search for the node to be removed.
        while current_node is not None and current_node.next is not None:
            # While the current node exists and is not the last
            if current_node.next.id == element_to_remove.id:
                # bypass the node, effectively deleting it from the list
                current_node.next = current_node.next.next
                return
            current_node = current_node.next # increment to the next node

        # If node is not found in the linked list
        return  # element not found in list


    def printRoutine(self):
        print("Routine is:")
        current_element = self._head
        while current_element != None:
            current_element.printElement()
            current_element = current_element.next

