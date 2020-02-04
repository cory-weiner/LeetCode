# Add Two Numbers
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''.join([str(i) for i in get_linked_num(l1)[::-1]])
        num2 = ''.join([str(i) for i in get_linked_num(l2)[::-1]])
        num3 = int(num1) + int(num2)
        return num_to_linked_list(num3)

def get_linked_num(ll):
    num = []
    while True:
        num.append(ll.val)
        ll = ll.next
        if not ll: break
    return num 

def num_to_linked_list(n):
    # Get reversed array of digits in num
    l = [int(i) for i in str(n)][::-1]
    result = None
    result = ListNode(l[0])
    curr_node = result
    for i in l[1:]:
        newnode = ListNode(i)
        curr_node.next = newnode
        curr_node = newnode
    return result



a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

a.next = b
b.next = c


d = ListNode(5)
e = ListNode(6)
f = ListNode(4)

d.next = e
e.next = f 

print(Solution().addTwoNumbers(a,d))