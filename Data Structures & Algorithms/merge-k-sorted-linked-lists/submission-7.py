# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        curr = dummy

        for ls in lists:
            if ls:
                heapq.heappush(heap, NodeWrapper(ls))
        
        while heap:
            node = heapq.heappop(heap)
            curr.next = node.node
            curr = curr.next
            if node.node.next:
                heapq.heappush(heap, NodeWrapper(node.node.next))
        
        return dummy.next
        