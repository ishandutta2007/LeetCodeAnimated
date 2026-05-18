# LeetCode Question No. 86: Split a Linked List

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 86 on LeetCode: Splitting a linked list. The difficulty of the questions is Easy, and the current passing rate is 47.8%.

### Title description

Given a linked list and a specific value *x*, split the linked list so that all nodes less than *x* precede nodes greater than or equal to *x*.

You should preserve the initial relative position of each node in both partitions.

**Example:**

```
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
```

### Question analysis

This question requires us to divide the linked list and move all nodes smaller than a given value to the front. The order of nodes larger than the value remains unchanged, which is equivalent to a local sorting problem.

- Set two virtual nodes, `dummyHead1` is used to save the linked list less than this value, `dummyHead2` is used to save the linked list greater than or equal to this value
- Traverse the entire original linked list, place the value less than this value in `dummyHead1`, and the rest in `dummyHead2`
- After the traversal, insert `dummyHead2` after `dummyHead1`

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/t96zg.gif)

### Code implementation

```
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {

        ListNode* dummyHead1 = new ListNode(-1);
        ListNode* dummyHead2 = new ListNode(-1);
        ListNode* prev1 = dummyHead1;
        ListNode* prev2 = dummyHead2;

        for(ListNode* cur = head ; cur != NULL ;){
            if(cur->val < x){
                prev1->next = cur;
                cur = cur->next;
                prev1 = prev1->next;
                prev1->next = NULL;
            }
            else{
                prev2->next = cur;
                cur = cur->next;
                prev2 = prev2->next;
                prev2->next = NULL;
            }
        }

        prev1->next = dummyHead2->next;
        ListNode* ret = dummyHead1->next;

        delete dummyHead1;
        delete dummyHead2;
        return ret;
    }
};
```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/5a3tl.png)