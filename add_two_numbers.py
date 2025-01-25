from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return str(result)

    @classmethod
    def from_list(cls, elements):
        dummy = cls(0)
        current = dummy
        for element in elements:
            current.next = cls(element)
            current = current.next
        return dummy.next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        carry = 0

        dummy = ListNode(0)
        current = dummy

        while c1 or c2:
            total = (c1.val if c1 else 0) + (c2.val if c2 else 0) + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None

        if carry != 0:
            current.next = ListNode(carry)

        return dummy.next


if __name__ == '__main__':
    solution = Solution()

    l1 = ListNode.from_list([2, 4, 3])
    l2 = ListNode.from_list([5, 6, 4])
    print(solution.add_two_numbers(l1, l2))

    l1 = ListNode.from_list([0])
    l2 = ListNode.from_list([0])
    print(solution.add_two_numbers(l1, l2))

    l1 = ListNode.from_list([9, 9, 9, 9, 9, 9, 9])
    l2 = ListNode.from_list([9, 9, 9, 9])
    print(solution.add_two_numbers(l1, l2))
