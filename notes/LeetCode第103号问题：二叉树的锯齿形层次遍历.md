# LeetCode Problem No. 103: Zigzag level traversal of binary trees

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 103 on LeetCode: Zigzag level traversal of a binary tree. The difficulty level of the questions is Medium, and the current pass rate is 43.8%.

### Title description

Given a binary tree, return a zigzag hierarchical traversal of its node values. (That is, first traverse the next layer from left to right, then from right to left, and so on, alternating between layers).

For example:
Given a binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

Return the zigzag level traversal as follows:

```
[
  [3],
  [20,9],
  [15,7]
]
```

### Question analysis

This problem requires the use of **Queue**, which is similar to the previous [Level Traversal of Binary Tree](https://xiaozhuanlan.com/topic/8579460312). The difference is that it needs to be flipped at the even-numbered level.

- Create a queue
- Put the root node in first, then find the left and right child nodes of the root node
- Remove the root node. At this time, the elements in the queue are all the nodes in the next layer.
- Loop through and store the results in a one-dimensional vector
- After traversing, store this one-dimensional vector into a two-dimensional vector.
- If the layer is an even-numbered layer, flip it reversely
- By analogy, layer-order traversal can be completed

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/xuoqo.gif)

### Code implementation

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/7mnmj.png)



![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/q9yt7.png)