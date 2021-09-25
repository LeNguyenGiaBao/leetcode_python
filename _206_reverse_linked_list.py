# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if (head == None): 
        return None
    
    currentNode = head
    while(currentNode.next!=None):
        nextNode = currentNode.next
        currentNode.next = nextNode.next
        nextNode.next = head
        head = nextNode

    return head

def printLinkedNode(head):
    while(head!=None):
        print(str(head.val)+'->', end='')
        head = head.next
    print()

if __name__ == "__main__":
    l1 = ListNode(0)
    l2 = ListNode(1)
    l3 = ListNode(2)

    l1.next = l2
    l2.next = l3

    printLinkedNode(l1)
    rev = reverseList(l1)
    printLinkedNode(rev)

