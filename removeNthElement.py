def removeNthFromEnd(self, head, n):
    if head is None:
        return None

    t = head
    lis = []

    while t is not None:
        lis.append(t.val)
        t = t.next

    del lis[-n]

    if(len(lis) != 0):
        
        res = ListNode(lis[0])
        t = res
        for i in range(1,len(lis)):
            t.next = ListNode(lis[i])
            t = t.next

        return res
    else:
