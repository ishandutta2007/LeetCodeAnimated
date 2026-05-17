# LeetCode Problem No. 22: Generate all bracket pairs

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from question No. 22 on LeetCode: Generate all bracket pairs. The difficulty level of the questions is Medium, and the current passing rate is 60.9%.

### Title description

Given a number n, it is required to use n pairs of () brackets to generate all legal combinations.

**Example**

```
3

[
"((()))",
"(()())",
"(())()",
"()(())", 
"()()()"
]
```

### Question analysis

#### Solution 1: Violence

The violent solution should be the easiest to think of, because n is certain, that is to say, there are n left brackets and n right brackets in total. It is easy to think that we can arrange and combine these 2n characters, and then filter all combinations. Just leave the ones that are legal and non-duplicate.

Pseudocode is easy to write:

```python
def brute_force(str, l, r):
    if l == n and r == n:
        ans.append(str)
    if l < n:
        brute_force(str+'(', l+1, r)
    if r < n:
        brute_force(str+')', l, r+1)
```

After writing it, judge whether it is legal based on the results, and just leave all the legal situations.

It is indeed not difficult to encode in this way, and it is easy to think of, but the complexity of calculating the permutation and combination of n characters is $O(2^n)$, which is an exponential algorithm, and the complexity is unacceptable to us. And according to the conclusion in the previous question, there are tricks when matching brackets. We actually don't need to enumerate all situations. Because for bracket matching to be legal, there must be one. For any position i in the string, there must be: the number of all left brackets in the first i character is greater than or equal to the number of right brackets.
, otherwise it is illegal.

That is to say, it must be ensured that the number of right brackets at any position is less than or equal to the number of left brackets, otherwise, the extra right brackets will never match.

#### Solution 2: Backtracking

Since the number of left brackets must be greater than the number of right brackets, we can optimize accordingly. We judge the size of l and r during recursion to ensure that l >= r at all times.

Code:

```C++
class Solution {
public:

    void dfs(int n, int l, int r, string str, vector<string>& vt) {
        if (l+r == 2 *n) {
            vt.push_back(str);
            return ;
        }
        if (l < n) dfs(n, l+1, r, str+"(", vt);
        if (r < l) dfs(n, l, r+1, str+")", vt);
    }

    vector<string> generateParenthesis(int n) {
        vector<string> vt;
        dfs(n, 0, 0, "", vt);
        return vt;
    }
};
```

#### Solution 3: Construction

This method is my original creation and is not included in the official solution.

It is more difficult when we directly solve the answer to n. At this time, we can dismantle the problem, turn the big problem into small problems, and construct the answer to the big problem through the answers to the small questions. The above two methods are essentially the same idea, but recursion splits the problem for us.

In fact, we can split the question ourselves, and when n, we suddenly don’t know the answer. We can start by simply observing the results: for example, when n==1, the answer is "()". There are two types of n==2: "()()", "(())". When n==3, there are 5 types: "((()))", "()(())", "()()()", "(()())", "(())()".

Careful readers can already sum up the rules, but it is actually not difficult to think of.

solution(n) = solution(i) + solution(n-i) + '(' solution(n-1) ')'

Explain this formula. The solution(n) here represents all the answer strings of n. That is to say, the answer strings of n brackets can be combined by answer strings less than n. For example, when n=1, the answer is (), and when n=2, there are two types. One is to splice two n=1 together, and the second is to add a bracket outside the answer of n=1:

solution(2) = [()(), (())]

Let's look at solution(3) again, which can be spliced ​​with n=1 and n=2, and all answers can be obtained by adding separate parentheses to the outer layer of n=2:

solution(3) = [()()(), ()(()), (())(), (()()), ((()))]

The first three are obtained by splicing solution(2) and solution(1), and the latter two are obtained by adding parentheses directly outside solution(2). This situation cannot be obtained by splicing. We summarize all these situations and remove duplicate situations to get the answer.

In this way we construct the result of n using all results less than n, since the cases n=0 and n=1 are known. We only need to store the intermediate results and get all the answers through recursion.

### Animation description

![](../Animation/0022-Generate_Parentheses.gif)

### Code implementation

```C++
class Solution {
public:

    vector<string> generateParenthesis(int n) {
          // store all intermediate results
        map<int, set<string>> mp;
        set<string> st;
        st.insert("()");
        mp[1] = st;

        for (int i = 2; i <= n; i++) {
              // Use set to remove duplicates
            set<string> cur;
            for (int j = 1; j <= i-1; j++) {
                  // Get all solution(j) and solution(i-j)
                set<string> vj = mp[j];
                set<string> vk = mp[i-j];
                for (string str:vj) {
                    for (string stj : vk) {
                        cur.insert(str + stj);
                    }
                }
            }
              // Solution(i-1) puts parentheses on the outermost layer
            set<string> vj = mp[i-1];
            for (string str : vj) {
                cur.insert("(" + str + ")");
            }
              // get solution(i)
            mp[i] = cur;
        }
        vector<string> vt;
        st = mp[n];
        for (string str : st) vt.push_back(str);
        return vt;
    }
};
```

![](../../Pictures/qrcode.jpg)