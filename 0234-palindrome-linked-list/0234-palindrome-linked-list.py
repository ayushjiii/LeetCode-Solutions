# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        
        ## we will use total 3 algorithms here :
        # 1. tortoise and heir (slow-fast pointer)
        # 2. reverse LL 
        # 3. Two pointers (left-right)


        ## declaring the pointers
        fast,slow = head,head

        ## moving the pointers until fast reaches to the end
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next       
        

        ## reverse the linked list from the middle
        prev = None
        while slow :
            tmp = slow.next 
            slow.next = prev
            prev = slow
            slow = tmp

        ## checking if palindrome or not -> (True or False)
        left,right = head,prev
        while right :
            if left.val != right.val :
                return False
            left = left.next
            right = right.next

        return True




