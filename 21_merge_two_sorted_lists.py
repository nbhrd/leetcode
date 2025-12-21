class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def print_list(node, name="list"):
    """連結リストを見やすく出力"""
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(f"{name}: " + " -> ".join(vals) if vals else f"{name}: None")


def build_list(nums):
    dummy = ListNode()
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy_head = ListNode()
        current = dummy_head

        step = 0
        print("=== merge start ===")
        print_list(list1, "list1(start)")
        print_list(list2, "list2(start)")
        print("-------------------")

        while list1 and list2:
            print(f"[step {step}]")
            print(f"current.val: {current.val}")
            print_list(current.next, "current.next(before)")
            print_list(dummy_head.next, "dummy_head.next(before)")
            print_list(list1, "list1 (remaining)")
            print_list(list2, "list2 (remaining)")

            if list1.val <= list2.val:
                print(f"  take {list1.val} from list1")
                current.next = list1  # current と dummy_head は同じオブジェクトなので、ここで dummy_head.next も更新される
                list1 = list1.next
            else:
                print(f"  take {list2.val} from list2")
                current.next = list2
                list2 = list2.next

            current = current.next

            print_list(dummy_head.next, "dummy_head.next(after)")
            print()

            step += 1

        print("[finishing]")
        if list1:
            print("  attach rest of list1")
            print_list(list1, "remaining list1")
            current.next = list1
        elif list2:
            print("  attach rest of list2")
            print_list(list2, "remaining list2")
            current.next = list2

        print_list(dummy_head.next, "final dummy_head.next")
        print("=== merge done ===\n")

        return dummy_head.next


# 実行コード
l1 = build_list([1, 2, 4])
l2 = build_list([1, 3, 4])

s = Solution()
result = s.mergeTwoLists(l1, l2)

print("=== result ===")
print_list(result, "merged")

# ListNode{
#     val: 1,
#     next: ListNode{
#         val: 2,
#         next: ListNode{
#             val: 4,
#             next: None
#         }
#     }
# }