def reverseList(self, head: ListNode) -> ListNode:
        
        lis = []
        t = head

        while(t != None):
            lis.append(t)
            t = t.next
            
        if(len(lis) != 0):

            for i in range(1,len(lis)):
                lis[-i].next = lis[-i-1]

            lis[0].next = None
            return lis[-1]
        else:
            return None