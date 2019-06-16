def getIntersectionNode(self, A, B):
    if(A == None or B == None):
        return None
    
    t = A
    while (t.next != None): 
        t = t.next
    t.next = B

    fast = A
    slow = A
    while fast and fast.next:
        #print("HI")
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            fast = A
            while fast != slow:
                slow = slow.next
                fast = fast.next
            t.next = None
            return slow

    t.next = None
    return None