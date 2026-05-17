# LeetCode Issue No. 138: Copying a linked list with random pointers

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 138 on LeetCode: Copying a linked list with random pointers. The difficulty level of the questions is Medium, and the current pass rate is 40.5%.

### Title description

Given a linked list, each node contains an additional random pointer that can point to any node in the linked list or an empty node.

Requests a **deep copy** of this linked list to be returned.

**Example:**

```
enter:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

explain:
The value of node 1 is 1, and its next pointer and random pointer both point to node 2.
The value of node 2 is 2, its next pointer points to null, and the random pointer points to itself.
```

### Question analysis

1. Copy a new node after each node in the original linked list

2. Assign values ​​to the random pointers of the new nodes in sequence, and this assignment is very easy cur->next->random = cur->random->next

3. Disconnect the linked list to obtain a new linked list after deep copying

The reason why this method is more clever is that compared to the general solution (such as using Hash map), the above solution **does not require additional space**.

### Animation description

![](../Animation/Animation.gif)

### Code implementation

I find that problems with pointers are easier to describe using the C++ version, so the code implementation below is the C++ version.

```c++
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (!head) return NULL;
        RandomListNode *cur = head;
        while (cur) {
            RandomListNode *node = new RandomListNode(cur->label);
            node->next = cur->next;
            cur->next = node;
            cur = node->next;
        }
        cur = head;
        while (cur) {
            if (cur->random) {
                cur->next->random = cur->random->next;
            }
            cur = cur->next->next;
        }
        cur = head;
        RandomListNode *res = head->next;
        while (cur) {
            RandomListNode *tmp = cur->next;
            cur->next = tmp->next;
            if(tmp->next) tmp->next = tmp->next->next;
            cur = cur->next;
        }
        return res;
    }
};
```

![](../../Pictures/qrcode.jpg)

