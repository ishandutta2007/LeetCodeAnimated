# LeetCode Question No. 19: Delete the penultimate N node of the linked list

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 19 on LeetCode: Delete the penultimate N node of the linked list. The difficulty level of the questions is Medium, and the current passing rate is 34.4%.

### Title description

Given a linked list, delete the last *n* node of the linked list and return the head node of the linked list.

**Example:**

```
Given a linked list: 1->2->3->4->5, and n = 2.

When the penultimate node is deleted, the linked list becomes 1->2->3->5.
```

**illustrate:**

The given *n* are guaranteed to be valid.

**Advanced:**

Could you try using a one-pass scan implementation?

### Question analysis

The problem can definitely be solved by double traversal, but the question requires us to solve the problem by one traversal, so our thinking needs to be divergent.

We can imagine that if double pointers `p` and `q` are set, when `q` points to `NULL` at the end, and the number of elements separated between `p` and `q` is `n`, then deleting the next pointer of `p` will complete the requirement.

- Set the virtual node `dummyHead` to point to `head`
- Set double pointers `p` and `q`, initially pointing to the virtual node `dummyHead`
- Move `q` until the number of elements between `p` and `q` is `n`
- Move `p` and `q` at the same time until `q` points to `NULL`
- Point the next node of `p` to the next node

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/r04hv.gif)

### Code implementation

```
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
     ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;

        ListNode* p = dummyHead;
        ListNode* q = dummyHead;
        for( int i = 0 ; i < n + 1 ; i ++ ){
            q = q->next;
        }

        while(q){
            p = p->next;
            q = q->next;
        }

        ListNode* delNode = p->next;
        p->next = delNode->next;
        delete delNode;

        ListNode* retNode = dummyHead->next;
        delete dummyHead;

        return retNode;
        
    }
};
```

![](../../Pictures/qrcode.jpg)