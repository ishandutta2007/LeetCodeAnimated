## LeetCode Question No. 58: Length of last word

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal blog: www.zhangxiaoshuai.fun

**This question is selected from Leetcode question 58, easy difficulty, current pass rate is 33.0%**

### Title description:
```txt
Given a string s containing only uppercase and lowercase letters and spaces ' ', return the length of its last word.
If the string is scrolled from left to right, the last word is the last word that appears.
If the last word does not exist, return 0.
Description: A word refers to the largest substring consisting only of letters and not containing any space characters.

Example:
Enter: "Hello World"
Output: 5
```

### Question analysis:

Since we need to find the length of the last word, we can start directly from the end of the string;
There are two situations at the end: with spaces and without spaces

```
(1) There are spaces: We ignore the spaces from the end, and then find the first character encountered (until the first space is encountered or the entire string is traversed)
(2) No spaces: Just search forward from the end (until you encounter the first space or traverse the entire string)
```

### Animated gif demo:

![](../Animation/0058.gif)

### Code:

**The first version**

```java
public int lengthOfLastWord(String s) {
    if (s.length()==0) {
        return 0;
    }
    int index = 0;
    int temp = 0;
    int p = s.length()-1;
    while ((p-index >=0) && s.charAt(p-index) == 32) index++;
    for (int i = p-index;i >= 0;i--) {
        if (s.charAt(i) != 32){
            temp++;
            continue;
        }
        break;   
    }
    return temp;
}
```

**2.Code:**

**The second version**

```java
public int lengthOfLastWord(String s) {
    int len = 0;
    for (int i = s.length() - 1; i >= 0; i--) {
        if (s.charAt(i) != ' ') {
            len++;
        } else if (len != 0) {
            return len;
        }
    }
    return len;
}
```

