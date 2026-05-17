# LeetCode Question No. 104: Maximum depth of a binary tree

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The topic shared today comes from question No. 104 on LeetCode: The maximum depth of a binary tree. The difficulty level of the questions is Easy.

### Title description

Given a binary tree, find its maximum depth.

The depth of a binary tree is the number of nodes on the longest path from the root node to the furthest leaf node.

**Description:** Leaf nodes refer to nodes that have no child nodes.

**Example:**

Given a binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

Returns its maximum depth of 3 .

### Question Analysis - DFS

The most direct way is to use the DFS (depth first search) strategy to calculate the height of the tree. The specific algorithm process is as follows:

- **Termination condition:**The current node is empty
- **Return value:**
  - When the node is empty, so 0 is returned
  - When the node is not empty, return the maximum value of the height of the left and right subtrees + 1

### Animation description

![](../Animation/Animation1.gif)

### Code implementation

```javascript
/**
 * JavaScript description
 * DFS
 */
var maxDepth = function(root) {
    if (root == null) {
        return 0;
    }
    let leftHeight = maxDepth(root.left);
    let rightHeight = maxDepth(root.right);
    return Math.max(leftHeight, rightHeight) + 1;
};
```

**Lite version**

```javascript
var maxDepth = function(root) {
    return !root ? 0 : Math.max(maxDepth(root.left) + 1, maxDepth(root.right) + 1) ;
};
```

### Complexity analysis

- Time complexity: **O(n)**, we only visit each node once, so the time complexity is O(N)
- Space complexity:
  - In the worst case, the tree is completely unbalanced, for example, each node has only the left child node, and the recursion will be called N times (the height of the tree), so the storage to maintain the call stack will be O(N).
  - In the best case (the tree is perfectly balanced), the height of the tree will be log(N). So the space complexity in this case will be O(log(N))



### Question Analysis - BFS

Finding the depth of a binary tree means finding how many levels there are in the binary tree. The BFS (breadth-first search) strategy is used to traverse the binary tree layer by layer.

To implement BFS, a 'first in, first out' queue is used. The specific algorithm flow is as follows:

- Traverse the binary tree nodes and queue the current node and its left and right child nodes in sequence.
- Dequeue in turn, and repeat the previous step for the sub-nodes that are dequeued.

### Animation description

![](../Animation/Animation2.gif)

### Code implementation

```javascript
/**
 * JavaScript description
 * BFS
 */
var maxDepth = function(root) {
    let level = 0;
    if (root == null) {
        return level;
    }
    let queue = [root];
    while (queue.length) {
        let len = queue.length;
        while (len--) {
            let curNode = queue.pop();
            curNode.left && queue.unshift(curNode.left);
            curNode.right && queue.unshift(curNode.right);
        }
        level++;
    }
    return level;
};
```

### Complexity analysis

- Time complexity: **O(n)**
- Space complexity: **O(N)**

![](../../Pictures/qrcode.jpg)