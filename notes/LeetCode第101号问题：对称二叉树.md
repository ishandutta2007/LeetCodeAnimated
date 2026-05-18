# LeetCode Problem No. 101: Symmetric Binary Tree

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from LeetCode Problem No. 101: Symmetric Binary Tree.

### Title description

Given a binary tree, check whether it is mirror symmetric.

For example, the binary tree `[1,2,2,3,4,4,3]` is symmetric.

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

### Question analysis

It's easier to do it with recursion: a tree is symmetrical **equivalently** to the fact that its left subtree and right subtree are symmetrical, and the problem becomes determining whether the two trees are symmetrical.

### Code implementation

```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if(root == null) return true;
        //Change the problem into determining whether two trees are symmetrical
        return isSym(root.left, root.right);
    }
    //Judge whether the two trees with root nodes r1 and r2 are symmetrical
    public boolean isSym(TreeNode r1, TreeNode r2){
        if(r1 == null && r2 == null) return true;
        if(r1 == null || r2 == null) return false;
        //The conditions that need to be met for these two trees to be symmetrical:
        //1. The two root nodes are equal. 2. The left subtree of tree 1 and the right subtree of tree 2, and the left subtree of tree 2 and the right subtree of tree 1 must be symmetrical.
        return r1.val == r2.val && isSym(r1.left, r2.right) 
                            && isSym(r1.right, r2.left);
    }
}
```

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/kbvfp.gif)