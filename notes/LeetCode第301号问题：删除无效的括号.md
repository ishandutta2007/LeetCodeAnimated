# LeetCode Issue No. 301: Remove invalid brackets

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from LeetCode question No. 301: Remove invalid brackets. A friend left a message in the background saying that this question was a computer-based test question for the Sun Yat-sen University computer postgraduate entrance examination.

### Title description

Removes the minimum number of invalid parentheses to make the input string valid, returning all possible results.

**Note:** The input may contain characters other than `(` and `)`.

**Example 1:**

```
Input: "()())()"
Output: ["()()()", "(())()"]
```

**Example 2:**

```
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
```

**Example 3:**

```
Input: ")("
Output: [""]
```



### Question analysis

The so-called valid brackets mean that the number of left and right brackets in the string should be the same, and there must be a corresponding left bracket to the left of each right bracket. It is easy to think of using a stack to simulate the matching process. '(' is pushed into the stack and ')' is popped out of the stack. If the stack is empty, it means that the string is consistent with the meaning of the question.

First, delete the brackets. By traversing from front to back, you can delete the non-conforming ')' brackets. By traversing from back to front, you can delete the non-conforming '(' brackets. Through BFS, continuously perform checkLeft and checkRight operations on the strings in the queue. If true is encountered, it means that the current string is already the optimal solution to delete the least invalid brackets, and then check other strings in the queue.
The animation of this question is very similar to LeetCode Question No. 20 - Valid Parentheses. Here it is used for reference and understanding. The difference lies in the addition of traversal and hash storage.

### Animation description

To be added

### Code implementation

```

public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        queue.offer(s);
        vis.add(s);
        boolean flag=false;
        List<String> ans=new ArrayList<String>();
        while (!queue.isEmpty()){
            String cur=queue.poll();
            if(flag){
                check(cur,ans);
            }else{
                flag=checkLeft(cur,ans)||checkRight(cur,ans);
            }
        }
        if(ans.size()==0){
            ans.add("");
        }
        return new ArrayList<String>(ans);
    }

    Set<String> vis=new HashSet<String>();
    Queue<String> queue=new LinkedList<String>();

    public void check(String s,List<String> ans){ //Check whether it is correct
        Stack<Character> st=new Stack<Character>();
        for(char c:s.toCharArray()){
            if(c=='('){
                st.push(c);
            }
            if(c==')'){
                if(st.isEmpty()){
                    return;
                }
                st.pop();
            }
        }
        if(st.isEmpty()){
            ans.add(s);
        }
    }

    public boolean checkLeft(String s,List<String> ans){ //Check left
        //delete right
        Stack<Character> st=new Stack<Character>();
        for(int i=0;i<s.length();++i){
            if(s.charAt(i)=='('){
                st.push(s.charAt(i));
            }else if(s.charAt(i)==')'){
                if(st.isEmpty()){
                    for(int j=i;j>=0;--j){ //Delete inconsistent ')' in various situations
                        if(s.charAt(j)==')'){
                            String s1=s.substring(0,j)+s.substring(j+1);
                            if(!vis.contains(s1)){
                                vis.add(s1);
                                queue.offer(s1);
                            }
                        }
                    }
                    return false;
                }else{
                    st.pop();
                }
            }
        }
        if(st.isEmpty()){
            ans.add(s);
            return true;
        }
        return false;
    }

    public boolean checkRight(String s,List<String> ans){ //Check the right
        //delete right
        Stack<Character> st=new Stack<Character>();
        st.clear();
        for(int i=s.length()-1;i>=0;--i){
            if(s.charAt(i)==')'){
                st.push(s.charAt(i));
            }else if(s.charAt(i)=='('){
                if(st.isEmpty()){
                    for(int j=i;j<s.length();++j){
                        if(s.charAt(j)=='('){ //Delete inconsistent '(' multiple situations
                            String s1=s.substring(0,j)+s.substring(j+1);
                            if(!vis.contains(s1)){
                                vis.add(s1);
                                queue.add(s1);
                            }
                        }
                    }
                    return false;
                }else{
                    st.pop();
                }
            }
        }
        if(st.isEmpty()){
            ans.add(s);
            return true;
        }
        return false;
    }
}


```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/syhz6.png)