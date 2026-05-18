# Use fast and slow pointers to solve "circular linked list" so easy!

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The topic shared today comes from question No. 141 on LeetCode: Circular Linked List. The difficulty of the questions is Easy, and the current passing rate is 40.4%.

Use fast and slow pointers to solve **so easy**!

### Title description

Given a linked list, determine whether there is a cycle in the linked list.

To represent a cycle in a given linked list, we use the integer `pos` to represent the position in the linked list where the tail of the linked list is connected (indexing starts from 0). If `pos` is `-1`, there is no cycle in the linked list.

**Example 1:**

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a ring in the linked list, the tail of which is connected to the second node.
```

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/vweoq.png)

**Example 2:**

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a ring in the linked list, the tail of which is connected to the first node.
```

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/kxbrz.png)

**Example 3:**

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/w3vsg.png)

**Advanced:**

Can you solve this problem with O(1) (i.e., constant) memory?

### Question analysis

This question is a **classic application** of fast and slow pointers.

Set up two pointers, a **slow pointer** that takes one step at a time and a **fast pointer** that takes two steps at a time.

* If there is no cycle, the faster pointer will eventually encounter null, indicating that the linked list does not contain a cycle.
* If there is a ring, the fast pointer will exceed the slow pointer by one circle and meet the slow pointer, indicating that the linked list contains a ring.

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/mj4qo.gif)

### Code implementation

```java
//author:Programmer Xiao Wu
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}
```

