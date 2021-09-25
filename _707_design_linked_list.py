class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        count = 0
        curNode = self.head

        while (curNode != None):
            if (count == index):
                return curNode.value

            count+=1
            curNode = curNode.next
        
        
        return -1
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        lastNode = self.head
        if (lastNode == None):
            self.addAtHead(val)
            return

        while(lastNode.next != None):
            lastNode = lastNode.next
        
        lastNode.next = newNode


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if(index == 0):
            self.addAtHead(val)
            return
        
        newNode = Node(val)
        count = 0
        curNode = self.head
        preNode = None

        while(curNode != None):
            count+=1
            if (count == index):
                newNode.next = curNode.next
                curNode.next = newNode
                return 

            curNode = curNode.next
        
        # if (count+1 == index):
        #     self.addAtTail(val)
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        count = 0
        curNode = self.head
        preNode = None

        while(curNode != None):
            if (count == index):
                if preNode is None:
                    self.head = curNode.next
                    return
                
                preNode.next = curNode.next

            count +=1
            preNode = curNode
            curNode = curNode.next
        
def print_linked_list(head):
    while (head != None):
        print(str(head.value) + "->", end='')
        head = head.next
    print()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

if __name__ == "__main__":
    my_list = MyLinkedList()
    my_list.addAtHead(1)
    my_list.addAtTail(3)
    my_list.addAtIndex(1,2)
    print_linked_list(my_list.head)
    # print(my_list.get(1))
    my_list.deleteAtIndex(1)
    print_linked_list(my_list.head)
    my_list.addAtIndex(2, 4)
    # print(my_list.get(1))
    print_linked_list(my_list.head)
    my_list.deleteAtIndex(2)
    print_linked_list(my_list.head)