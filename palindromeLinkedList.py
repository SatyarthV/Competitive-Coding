def isPalindrome(self, head):

    t = head

    if(t == None):
        return True

    if(t.next == None):
        return True

    if(t.val == t.next.val and t.next.next == None):
        return True
    

    lis = []
    while(t != None):
        lis.append(t.val)
        t = t.next

    for i in range(len(lis)//2):
        if(lis[i] != lis[len(lis)-i-1]):
            return False
    return True
    