# LeetCode Problem No. 124: Maximum sum of paths in a binary tree

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 124 on LeetCode: Maximum path sum in a binary tree. The difficulty of the questions is Hard, and the current passing rate is 39.9%.


<br>


### Title description

Given a non-empty binary tree, return its maximum path sum.

In this question, a path is defined as a sequence starting from any node in the tree and reaching any node. The path contains at least one node and does not necessarily pass through the root node.

**Example 1:**

```
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
```

**Example 2:**

```
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```

<br>

### Question analysis

Binary tree problem, the question requires finding the maximum path sum of a binary tree. The path sum is to add up the values ​​of the nodes on a path. The difficulty of this question is that the direction of the path is not fixed. As long as the path between any two points is considered a valid path, if a reasonable plan is not listed in advance, this question will be impossible to start. Generally speaking, recursion is required to solve tree problems. **Search on a tree is essentially a depth-first search**. However, there are two ways to consider it. One is **bottom-up divide and conquer**, that is, entering recursion. It does not do any calculations or processing on the nodes at the beginning, and directly enters the next level of recursion until it reaches the bottom layer. Then it starts to calculate and return the answer, and then recurses the upper tree nodes. The function will receive the result returned by the lower layer. The advantage of this is that a node can know the local answer of its subtree; the other is **top-down traversal search**, which is completely opposite to the previous idea, that is, the content of the current node is processed first, and then it goes to the next level node. This method generally does not have a return value, but there is usually a global or reference variable to record the content during the traversal process.

Let's go back to this question. During the recursive traversal process, for the current node, it can be the end of the path, the head of the path (assuming the path is from top to bottom, in fact, in this question, there is no concept of head and tail), or it can be a node in the path. So how to judge? At this time we need information about the left and right subtrees of the current node, so we can consider using the **bottom-up** divide and conquer mentioned before. With the current node and the maximum path from the left and right subtrees to the current node, we can look at several situations here. I use **root** to represent the current node, **left** to represent the maximum sum path from the left subtree to the root, and **right** to represent the maximum sum path from the right subtree to the root:
* root and left and right paths form a path (left - root - right)
* root and left path form path (left - root)
* root and right path form path (root - right)
* root self-contained path (root)

You can see that all four cases take the current node into account and we can update the maximum value here. However, it should be noted that when we return, the first case cannot be returned, because it cannot form a valid path for the upper layer node, so we only need to return the maximum value among 2, 3, and 4. Of course, when updating the global answer, these four cases need to be taken into account.

<br>

### Code implementation

```java
private int maximum = Integer.MIN_VALUE;

public int maxPathSum(TreeNode root) {
    if (root == null) {
        return 0;
    }
    
    helper(root);
    
    return maximum;
}

private int helper(TreeNode root) {
    if (root == null) {
        return 0;
    }
    // If the maximum path value returned by the left and right subtrees is less than 0
    // Set the value to 0 directly, that is, the corresponding path is not considered
    int leftMax = Math.max(0, helper(root.left));
    int rightMax = Math.max(0, helper(root.right));
    
    maximum = Math.max(root.val + leftMax + rightMax, maximum);
    
    return Math.max(leftMax + root.val, rightMax + root.val);
}
```

<br>

### Animation description

![](../Animation/124.gif)

![](../../Pictures/qrcode.jpg)