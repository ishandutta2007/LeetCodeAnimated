# LeetCode Problem No. 92: Reverse Linked List II

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 92 on LeetCode: Reverse Linked List II. The difficulty level of the questions is Medium, and the current pass rate is 43.8%.

### Title description

Reverse the linked list from position *m* to *n*. Please use one scan to complete the reversal.

**illustrate:**
1 ≤ *m* ≤ *n* ≤ linked list length.

**Example:**

```
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
```

### Question analysis

An extended question of **[Reverse Linked List](https://xiaozhuanlan.com/topic/7513064892)**.

You can consider taking out the small segment of the linked list that needs to be reversed, and then inserting it into the original linked list after reversing it.

**Take this question as an example:**

The three points that are transformed are 2, 3, and 4. Then we can first take out 2 and use the front pointer to point to 2. Then when taking out 3, we add 3 in front of 2 and move the front pointer forward to 3, and so on, and stop after reaching 4. In this way, we get a new linked list 4 -> 3 -> 2, and the front pointer points to 4.

For the original linked list, the positions of two points are very important and need to be recorded with pointers, which are 1 and 5 respectively. The positions of these two points are needed when inserting the new linked list.

- Use the pre pointer to record the position of 1
- When node 4 is removed, the position of node 5 needs to be recorded.
- In this way we can add the inverted short section of the linked list to the original linked list



### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/rjjr0.gif)

### Code implementation

```
class Solution {
public:
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        ListNode *dummy = new ListNode(-1);
        dummy->next = head;
        ListNode *cur = dummy;
        ListNode *pre, *front, *last;
        for (int i = 1; i <= m - 1; ++i) cur = cur->next;
        pre = cur;
        last = cur->next;
        for (int i = m; i <= n; ++i) {
            cur = pre->next;
            pre->next = cur->next;
            cur->next = front;
            front = cur;
        }
        cur = pre->next;
        pre->next = front;
        last->next = cur;
        return dummy->next;
    }
};
```



![](../../Pictures/qrcode.jpg)