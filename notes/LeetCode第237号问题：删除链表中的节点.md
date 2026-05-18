# LeetCode Question No. 237: Deleting nodes in a linked list

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 237 on LeetCode: Delete nodes in a linked list. The difficulty of the questions is Easy, and the current passing rate is 72.6%.

### Title description

Please write a function that deletes a given (non-end) node in a linked list. You will only be given the node to be deleted.

There is an existing linked list -- head = [4,5,1,9], which can be expressed as:

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/uv8bw.png)

 

**Example 1:**

```
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: Given the second node in your linked list with value 5, after calling your function, the linked list should become 4 -> 1 -> 9.
```

**Example 2:**

```
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: Given the third node in your linked list with value 1, after calling your function, the linked list should become 4 -> 5 -> 9.
```

 

**illustrate:**

- The linked list contains at least two nodes.
- The values ​​of all nodes in the linked list are unique.
- The given node is a non-last node and must be a valid node in the linked list.
- Don't return any results from your function.

### Question analysis

The important point to note in this question is that we are not given the starting point of the linked list, but only a node to be deleted, which is slightly different from the previous situations.

**The solution to this problem is to first overwrite the value of the current node with the value of the next node, and then we can delete the next node**

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/1navy.gif)

### Code implementation

```
class Solution {
public:
    void deleteNode(ListNode* node) {
        if (node == NULL) return;
        if (node->next == NULL) {
            delete node;
            node = NULL;
            return;
        }
        node->val = node->next->val;
        ListNode *delNode = node->next;
        node->next = delNode->next;
        
        delete delNode;
    }
};
```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/f5g8p.png)