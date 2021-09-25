class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def add_to_head(self, value):
        # create new node
        new_node = ListNode(value)

        new_node.next = self
        return new_node

    def add_to_tail(self, value):
        # create new node
        new_node = ListNode(value)

        # find the last node
        last_node = self
        while(last_node.next != None):
            last_node = last_node.next
        last_node.next = new_node

        return self

    def add_to_index(self, value, index):
        # create new node 
        new_node = ListNode(value)

        if (index == 0):
            return self.add_to_head(value)

        count = 0
        current_node = self
        while(current_node != None):
            if count == index:
                new_node.next = current_node.next
                current_node.next = new_node
            
            count+=1
            current_node = current_node.next
        
        return self

    def remove_at_head(self):
        self = self.next
        return self

    def remove_at_last(self):
        last_node = self
        prev_node = None

        while(last_node.next!=None):
            prev_node = last_node
            last_node = last_node.next
        
        prev_node.next = None
        return self

    def remove_at_index(self, index):
        if (index==0):
            return self.remove_at_head()
        
        count = 0
        current_node = self
        prev_node = None
        while(current_node != None):
            if (count == index):
                prev_node.next = current_node.next
                break

            count += 1
            prev_node = current_node
            current_node = current_node.next
        return self


def print_ListNode(head):
    while(head!=None):
        print(str(head.val) + '->', end='')
        head = head.next
    print()

if __name__ == "__main__":
    l1 = ListNode(0)
    l2 = ListNode(1)
    l3 = ListNode(2)

    l1.next = l2
    l2.next = l3
    # new_node = l1.add_to_head(4)
    # print_ListNode(new_node)

    # new_node_2 = l1.add_to_tail(7)
    # print_ListNode(new_node_2)

    new_node_3 = l1.add_to_index(5, 2)
    print_ListNode(new_node_3)

    # new_node_4 = new_node_3.remove_at_head()
    # print_ListNode(new_node_4)

    # new_node_5 = new_node_4.remove_at_last()
    # print_ListNode(new_node_5)

    new_node_6 = new_node_3.remove_at_index(4)
    print_ListNode(new_node_6)