# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        
        heap = []
        dummy = ListNode()
        curr = dummy

        while len(lists) > 1:
            merged = []
            for i in range(1, len(lists), 2):
                l1, l2 = lists[i - 1], lists[i]
                dummy = ListNode()
                curr = dummy

                while l1 and l2:
                    if l1.val < l2.val:
                        curr.next = l1
                        l1 = l1.next
                    else:
                        curr.next = l2
                        l2 = l2.next
                    curr = curr.next

                curr.next = l1 if l1 else l2
                merged.append(dummy.next)
            
            if len(lists) % 2 == 1:
                merged.append(lists[-1])
            
            lists = merged

        return lists[0]
        