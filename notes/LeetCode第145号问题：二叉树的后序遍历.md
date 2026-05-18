# LeetCode Question No. 145: Post-order traversal of binary trees

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 145 on LeetCode: Post-order traversal of a binary tree. The difficulty of the questions is Hard, and the current passing rate is 25.8%.

### Title description

Given a binary tree, return its *postorder* traversal.

**Example:**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3 

Output: [3,2,1]
```

**Advanced:** The recursive algorithm is simple, can you do it with an iterative algorithm?

### Question analysis

Use the stack idea to deal with problems.

The order of post-order traversal is **left-right-root**, and the specific algorithm is:

- First push the root node onto the stack, and then define an auxiliary node head
- The condition of the while loop is that the stack is not empty
- In the loop, first take out the top node t of the stack
- If the top node of the stack has no left or right child nodes, or its left child node is head, or its right child node is head. We add the value of the top node of the stack to the result res, move the top element off the stack, and then point head to the top element of the stack
- Otherwise, if the right child node is not empty, add it to the stack
- If the left child node is not empty, add it to the stack



### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/y7nxo.gif)

### Code implementation

```
public class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
    List<Integer> res = new ArrayList<Integer>();
    if(root == null)
        return res;
    Stack<TreeNode> stack = new Stack<TreeNode>();
    stack.push(root);
    while(!stack.isEmpty()){
        TreeNode node = stack.pop();
        if(node.left != null) stack.push(node.left);//Unlike traditional pre-order traversal, the left node is pushed onto the stack first
        if(node.right != null) stack.push(node.right);//Then push the right node onto the stack
        res.add(0,node.val); //Add node values ​​in reverse order
    }     
    return res;
   }
}
```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/8yuu3.png)