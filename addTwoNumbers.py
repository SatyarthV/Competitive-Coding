def addTwoNumbers(self, l1, l2):
    if l1.val == 0 and l1.next == None:
        return l2
    
    if l2.val == 0 and l2.next == None:
        return l1
    
    t1 = l1
    t2 = l2
    carry = (t1.val + t2.val)//10

    head3 = ListNode((t1.val + t2.val)%10)
    t3 = head3

    t1 = t1.next
    t2 = t2.next

    while(t1 != None and t2 != None):
        s = ListNode((t1.val + t2.val + carry)%10)
        t3.next = s
        t3 = t3.next
        carry = (t1.val + t2.val + carry)//10
        t1, t2 = t1.next, t2.next
    
    while(t1 != None):
        s = ListNode((t1.val + carry)%10)
        t3.next = s
        carry = (t1.val + carry)//10
        t3 = t3.next
        t1 = t1.next
    
    while(t2 != None):
        s = ListNode((t2.val + carry)%10)
        t3.next = s
        carry = (t2.val + carry)//10
        t3 = t3.next
        t2 = t2.next
    
    if(carry != 0):
        w = ListNode(carry)
        t3.next = w

    return head3