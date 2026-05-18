# LeetCode Question No. 199: Right view of a binary tree

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from question No. 199 on LeetCode: Right view of a binary tree. The difficulty level of the questions is Medium, and the current pass rate is 57.5%.

### Title description

Given a binary tree, imagine yourself standing on the right side of it, and return the node values ​​that can be seen from the right side in order from top to bottom.

**Example:**

```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
explain:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

### Question analysis

Similar to the previous [Level traversal of binary trees](https://xiaozhuanlan.com/topic/8579460312), this problem requires the use of **queue**,

- Create a queue
- When traversing the nodes of each layer, store the nodes of the next layer into the queue.
- Whenever starting to traverse a new layer of nodes, first store the value of the last node of the new layer into the result.



### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/i2nzo.gif)

### Code implementation

```
class Solution {
public:
    vector<int> rightSideView(TreeNode *root) {
        vector<int> res;
        if (!root) return res;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            res.push_back(q.back()->val);
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                TreeNode *node = q.front();
                q.pop();
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return res;
    }
};
```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/afv89.gif)