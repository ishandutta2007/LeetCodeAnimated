# LeetCode Problem No. 110: Balancing Binary Trees

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 110 on LeetCode: Balancing Binary Trees.

### Title description

Given a binary tree, determine whether it is a height-balanced binary tree.

In this question, a height-balanced binary tree is defined as:

> The absolute value of the height difference between the left and right subtrees of a binary tree *each node* does not exceed 1.

**Example 1:**

```
    3
   / \
  9  20
    /  \
   15   7
```

Return `true` .

**Example 2:**

Given a binary tree `[1,2,2,3,3,null,null,4,4]`

```
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```

Return `false` .

### Question analysis - top to bottom

This question can be regarded as a full use of recursion. Each subtree is a subproblem.

According to the meaning of the question, the intuitive idea is to calculate the height difference between the left and right subtrees of the current node. The specific algorithm process is as follows:

*Definition* Method `depth(root)` calculates the maximum height of root

- **Termination condition:** When `root` is empty, that is, beyond the leaf node, height 0 is returned.
- **Return value:** Max(left subtree height, right subtree height) + 1

*Definition* Method `isBalanced(root)` determines whether the tree `root` is balanced

- **Special case processing:** If the tree root node `root` is empty, return true directly
- **Return value:** All subtrees need to satisfy the balanced tree properties, so the following three are connected using logical AND
  - `abs(depth(root.left) - depth(root.right)) < 2`: Determine whether the **current subtree** is a balanced tree
  - `isBalanced(root.left)`: Pre-order traversal recursion to determine whether the **left subtree of the current subtree** is a balanced tree;
  - `isBalanced(root.right)`: Pre-order traversal recursion to determine whether the **right subtree of the current subtree** is a balanced tree;

> Through the process, we can find that although the brute force method is easy to think of, it will produce a lot of redundant calculations, so the time complexity will be high;
>
> To avoid this, move down and look at the bottom-up approach

### Animation description

<img src="../Animation/Animation1.gif" alt="Animation1" style="zoom:150%;" />

### Reference code

```javascript
/**
 * JavaScript description
 * Top-down recursion
 */
function depth(root) {
    if (root == null) {
        return 0;
    }
    return Math.max(depth(root.left), depth(root.right)) + 1;
};
var isBalanced = function(root) {
    if (root == null) {
        return true;
    }
    return Math.abs(depth(root.left) - depth(root.right)) < 2 &&
           isBalanced(root.left) &&
           isBalanced(root.right);
};
```

### Complexity analysis

- Time complexity: **O(Nlog_2 N)**

  In the worst case, isBalanced(root) traverses all nodes of the tree, occupying O(N)O(N); determining the maximum height of each node depth(root) requires traversing all nodes of each subtree, and the complexity of the number of nodes in the subtree is O(log_2 N)

- Space complexity: **O(N)**

  In the worst case (when the tree degenerates into a linked list), system recursion requires O(N) stack space.

### Question Analysis - Bottom-up

**Top-down** There is a lot of redundancy in calculating `depth`. Every time `depth` is called, its subtree height must be calculated at the same time.

**Bottom-up** The height of each subtree is calculated only once. First recursively calculate the height of the current node's child nodes, and then use the height of the child nodes to determine whether the current node is balanced to eliminate redundancy.

**Bottom-up** is the opposite of the logic of **Top-down**. It first determines whether the subtree is balanced, and then compares the height of the subtree to determine whether the parent node is balanced. The algorithm is as follows:

*Definition* Method `recur(root):`: Determine whether the subtree is balanced | Return the current node height

- **Recursion termination condition:**
  - When crossing a leaf node, return height 0
  - When the left (right) subtree height `left== -1`, the **left (right) subtree** representing this subtree is not a balanced tree, so `-1` is returned directly
- **Recursive return value:**
  - When the height difference between the left/right subtree of node `root` is < 2: Return the maximum height of the subtree with node root as the root node Max(left, right) + 1
  - When the height difference between the left and right subtrees of node `root` is >= 2: then `-1` is returned, which means **This subtree is not a balanced tree**

*Definition* Method `isBalanced(root)`: Determine whether the current tree is balanced

- **Return value:** If `recur(root) != 1`, it means the tree is balanced and returns `true`, otherwise returns `false`

### Animation description

<img src="../Animation/Animation2.gif" alt="Animation2" style="zoom:150%;" />

### Reference code

```javascript
/**
 * JavaScript description
 * Bottom-up recursion
 */
function recur(root) {
    if (root == null) {
        return 0;
    }
    let leftHeight = recur(root.left);
    if (leftHeight == -1) {
        return -1;
    }
    let rightHeight = recur(root.right);
    if (rightHeight == -1) {
        return -1;
    }
    return Math.abs(leftHeight - rightHeight) < 2 ? 
           Math.max(leftHeight,rightHeight) + 1 : -1;
};
var isBalanced = function(root) {
    return recur(root) != -1;
};
```

### Complexity analysis

- Time complexity **O(N)**: N is the number of nodes in the tree; in the worst case, all nodes of the tree need to be traversed recursively.
- Space complexity **O(N)**: In the worst case (when the tree degenerates into a linked list), system recursion requires O(N) stack space.




![](../../Pictures/qrcode.jpg)