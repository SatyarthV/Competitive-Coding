def deleteDuplicates(self, head):
        
        t = head
        if(head == None):
            return
        while(t.next != None):
            if (t.val == t.next.val):
                t.next = t.next.next
            else:
                t = t.next
        
        return head