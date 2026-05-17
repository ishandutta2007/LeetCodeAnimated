# LeetCode Problem No. 94: In-order traversal of binary trees

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 94 on LeetCode: In-order traversal of a binary tree. The difficulty level of the questions is Medium, and the current passing rate is 35.8%.

### Title description

Given a binary tree, return its in-order traversal.

**Example:**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

**Advanced:** The recursive algorithm is simple, can you do it with an iterative algorithm?

### Question analysis

Use the stack idea to deal with problems.

The order of in-order traversal is **Left-Root-Right**, and the specific algorithm is:

- Starting from the root node, push the root node onto the stack first
- Then push all its left child nodes onto the stack, take out the top node of the stack, and save the node value
- Then move the current pointer to its right child node. If there is a right child node, all its left child nodes can be pushed onto the stack in the next loop.



### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/v17b8.gif)

### Code implementation

```
class Solution {
        public List<Integer> inorderTraversal(TreeNode root) {
            List<Integer> list = new ArrayList<>();
            Stack<TreeNode> stack = new Stack<>();
            TreeNode cur = root;
            while (cur != null || !stack.isEmpty()) {
                if (cur != null) {
                    stack.push(cur);
                    cur = cur.left;
                } else {
                    cur = stack.pop();
                    list.add(cur.val);
                    cur = cur.right;
                }
            }
            return list;
        }
}
```

![](../../Pictures/qrcode.jpg)