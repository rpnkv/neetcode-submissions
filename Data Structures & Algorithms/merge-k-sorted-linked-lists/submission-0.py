class Solution:

    @staticmethod
    def linked_list_generator(head):
        current = head
        while current is not None:
            yield current.val
            current = current.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        i = heapq.merge(*
            [Solution.linked_list_generator(l) for l in lists]
        )

        head = tail = ListNode()

        while True:
            try:
                v = next(i)
                tail.next = ListNode(v)
                tail = tail.next
            except StopIteration:
                break

        return head.next
