# Definition for singly-linked list.

'''
head = ListNode{val: 1, next: 
       ListNode{val: 3, next: 
       ListNode{val: 4, next: 
       ListNode{val: 7, next: 
       ListNode{val: 1, next: 
       ListNode{val: 2, next: 
       ListNode{val: 6, next: None}}}}}}}
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_middle(head):
    if not head.next:
        return None
    
    prev = slow = fast = head

    while fast and fast.next:
        prev = slow
        fast = fast.next.next
        slow = slow.next

    prev.next = prev.next.next
    return head
    
def delete_middle_slow(head: [ListNode]):
    if not head.next:
        return None
    
    count = 0
    current = head
    while current:
        current = current.next
        count += 1
    
    middle = count//2
    current = head
    while middle > 1:
        current = current. next
        middle -= 1

    current.next = current.next.next

    return head

head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6, None)))))))
delete_middle_slow(head)
delete_middle(head)


