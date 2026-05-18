# LeetCode Question No. 24: Exchange nodes in a linked list pairwise

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The title comes from question No. 24 on LeetCode: Pairwise exchange of nodes in a linked list. The difficulty level of the questions is Medium, and the current pass rate is 45.8%.

### Title description

Given a linked list, swap adjacent nodes in pairs and return the swapped linked list.

**You can't just change the value inside the node**, but you need to actually swap the nodes.

**Example:**

```
Given 1->2->3->4, you should return 2->1->4->3.
```

### Question analysis

This question is a basic linked list operation question.

- Set a virtual head node `dummyHead`
- Set the two nodes that need to be exchanged as `node1` and `node2`, and also set the next node `next` of `node2`

##### In this round of operations

- Set next of `node2` node to `node1` node
- Set the next of the `node1` node to the `next` node
- Set next of `dummyHead` node to `node2`
- End this round of operation

Each subsequent round proceeds as described above.

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/6kpyu.gif)

### Code implementation

```
// 24. Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/description/
// Time complexity: O(n)
// Space complexity: O(1)
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {

        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;

        ListNode* p = dummyHead;
        while(p->next && p->next->next){
            ListNode* node1 = p->next;
            ListNode* node2 = node1->next;
            ListNode* next = node2->next;
            node2->next = node1;
            node1->next = next;
            p->next = node2;
            p = node1;
        }

        ListNode* retHead = dummyHead->next;
        delete dummyHead;

        return retHead;
    }
};

```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/k8lty.png)