# 387. The first unique character in a string

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Synchronized blog: https://www.algomooc.com

The question comes from Question 387 on LeetCode, which mainly involves hash tables.

## Title

Given a string, find its first non-repeating character and return its index. If it does not exist, -1 is returned.

Case:

```
s = "leetcode"
Return 0.

s = "loveleetcode",
Return 2.
```

Note: You can assume that the string contains only lowercase letters.

## Question analysis

No matter what, this question requires traversing the string to ensure that the characters are unique, so our algorithm is as follows

1. When traversing, use Map to record the number of times each character appears. If this character appears for the first time, then assign the value to [i]. If it is already in the Map, then we assign the value of this character to false.
2. Traverse the Map again, find the first character whose value is not false, and then output its value.
3. If the values ​​are all false, then return -1


## Animation understanding


<video id="video" controls="" preload="none" >
      <source id="mp4" src="../Animation/387.mp4"  type="video/mp4">
  </video>

## Reference code


```javaScript
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    let map = new Map()
    for (let i = 0; i < s.length;i++) {
        if(map.has(s[i])) {
            map.set(s[i], false)
        }else {
            map.set(s[i], [i])
        }
    }
    for(let item of map){
        if (item[1]) {
            return item[1][0]
        }
　　  }
   return -1
};
```

## Complexity analysis

The time complexity of a hash table is O(n)


![](../../Pictures/qrcode.jpg)