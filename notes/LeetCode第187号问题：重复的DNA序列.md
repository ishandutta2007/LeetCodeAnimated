#LeetCode Issue 187: Repeated DNA Sequences

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from Question No. 187 on LeetCode: Repeated DNA Sequences.

### Title description

All DNA is made up of a series of nucleotides abbreviated A, C, G and T, for example: "ACGAATTCCG". When studying DNA, it can sometimes be very helpful to identify repeating sequences in DNA.

Write a function that finds all 10-letter sequences (substrings) that occur more than once in a DNA molecule.

### Question analysis

First, first represent the ASCII codes of A, C, G, and T in binary:

A: 0100 0**001**　　C: 0100 0**011**　　G: 0100 0**111**　　T: 0101 0**100**

Through observation, it is found that the last three characters of each character are different, so the three characters at the end can be used to distinguish these four characters.

The question requirement is to find a 10-letter sequence. If we use three characters to distinguish each character, 10 characters will require 30 bits, which is OK on a 32-bit machine.

In order to extract the last 30 bits, you need to use **mask**, with a value of 0x7ffffff (the binary representation contains 27 1s). First, use this mask to extract the last 27 bits of the **entire sequence**, and then shift it to the left by three bits to extract a 10-letter sequence (30 bits).

In order to save the frequency of substrings, a hash table is used here.

First, when the tenth character is taken out, it is stored in the hash table and mapped with the frequency of occurrence of the string. Then, one character is replaced every three places to the left, and the number of occurrences of the new string in the hash table is found. If it has appeared once before, the current string is stored in the array of the return value and the number of occurrences is increased by one. If it has never appeared, map it to 1.

### 

### Animation description

To be added

### Code implementation

```c++
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        if (s.size() <= 10) return res;
        int mask = 0x7ffffff, cur = 0;
        unordered_map<int, int> m;
        for (int i = 0; i < 9; ++i) {
            cur = (cur << 3) | (s[i] & 7);
        }
        for (int i = 9; i < s.size(); ++i) {
            cur = ((cur & mask) << 3) | (s[i] & 7);
            if (m.count(cur)) {
                if (m[cur] == 1) res.push_back(s.substr(i - 9, 10));
                ++m[cur]; 
            } else {
                m[cur] = 1;
            }
        }
        return res;
    }
};
```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/xzbvx.png)