def rotateRight(self, head, k):
    if head is None:
        return head
    lis = []
    t = head
    while(t is not None):
        lis.append(t)
        t = t.next

    k = k % len(lis)
    out_lis = []
    for i in range(len(lis)-k, len(lis)):
        out_lis.append(lis[i])

    for i in range(0,len(lis)-k):
        out_lis.append(lis[i])

    r = ListNode(0)
    p = r
    p.next = out_lis[0]
    p = p.next
    for i in range(0,len(out_lis)-1):
        p.next = out_lis[i+1]
        p = p.next
    p.next = None
    return r.next

