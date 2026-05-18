# LeetCode Problem No. 110: Balancing Binary Trees

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 110 on LeetCode: Balancing Binary Trees.

### Title description

Given a binary tree, determine whether it is a height-balanced binary tree.

### Question analysis

Use **post-order traversal** to traverse each node of the binary tree.

Before traversing to a node, its left and right subtrees have been traversed, so as long as its depth is recorded when traversing each node (the depth of a node is equal to the length of its path to the leaf node), you can judge whether each node is balanced while traversing.

### Animation description

To be added

### Code implementation

```java
class Solution {
    private boolean isBalanced = true;
    public boolean isBalanced(TreeNode root) {
        getDepth(root);
        return isBalanced;
    }
      public int getDepth(TreeNode root) {
      if (root == null)
			return 0;
		int left = getDepth(root.left);
		int right = getDepth(root.right);
		if (Math.abs(left - right) > 1) {
			isBalanced = false;
		}
		return right > left ? right + 1 : left + 1;
      }
}
```



![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/z7w57.png)