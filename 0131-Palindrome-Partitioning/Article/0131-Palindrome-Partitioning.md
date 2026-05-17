# LeetCode Problem No. 131: Splitting a Palindrome

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 131 on LeetCode: Split palindrome strings. The difficulty level of the questions is Medium, and the current pass rate is 45.8%.

### Title description

Given a string *s*, split *s* into substrings such that each substring is a palindrome.

Return *s* all possible splitting options.

**Example:**

```yaml
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
```

### 

### Question analysis

First of all, for the division of a string, it is definitely necessary to traverse all division situations to determine whether it is a palindrome. Just because **abba** is a palindrome string, it does not mean that all its substrings are palindromes.

Since all segmentation methods need to be found, DFS (depth first search) or BFS (breadth first search) must be used.

During the splitting process, each string can be divided into two parts: a palindrome string on the left and a substring on the right. For example, "abc" can be divided into "a" + "bc". Then the "bc" segmentation is still the same, divided into "b" + "c".

When processing, give priority to finding shorter palindrome strings, then backtrack to find slightly longer palindrome string segmentation methods, and continue to backtrack and segment until all segmentation methods are found.

For example: Split "aac".

1. Divide into a + ac
2. Divide it into a + a + c. After the division, get a set of results, and then go back to a + ac
3. a + ac in ac is not a palindrome string, continue to trace back to aac
4. Split into a slightly longer palindrome string, split into aa + c. After the split is completed, a set of results is obtained, and then traced back to aac
5. aac is not a palindrome, search is over



### Animation description

![](../Animation/Animation.gif)

### Code implementation

```java
class Solution {
    List<List<String>> res = new ArrayList<>();
    
    public List<List<String>> partition(String s) {
        if(s==null||s.length()==0)
            return res;
        dfs(s,new ArrayList<String>(),0);
        return res;
    }
    
    public void dfs(String s,List<String> remain,int left){
        if(left==s.length()){ //Determine the termination condition
            res.add(new ArrayList<String>(remain)); //Add to the result
            return;
        }
        for(int right=left;right<s.length();right++){ //Start from left and determine whether left->right is a palindrome string
            if(isPalindroom(s,left,right)){ //Determine whether it is a palindrome string
                remain.add(s.substring(left,right+1)); //Add the current palindrome string to the list
                dfs(s,remain,right+1); //Continue recursion from right+1 to find the palindrome string
                remain.remove(remain.size()-1); //Backtrack to find a longer palindrome string
            }
        }
    }
    /**
    * Determine whether it is a palindrome string
    */
    public boolean isPalindroom(String s,int left,int right){
        while(left<right&&s.charAt(left)==s.charAt(right)){
            left++;
            right--;
        }
        return left>=right;
    }
}
```

![](../../Pictures/qrcode.jpg)