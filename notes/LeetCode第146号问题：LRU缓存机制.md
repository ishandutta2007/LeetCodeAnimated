# LeetCode Issue No. 146: LRU caching mechanism

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The title comes from question No. 146 on LeetCode: LRU caching mechanism. The difficulty of the questions is Hard, and the current passing rate is 15.8%.

### Title description

Use the data structures you have mastered to design and implement an [LRU (least recently used) caching mechanism](https://baike.baidu.com/item/LRU). It should support the following operations: getting data `get` and writing data `put`.

Get data `get(key)` - If the key exists in the cache, get the value of the key (always positive), otherwise return -1.
Write data `put(key, value)` - If the key does not exist, its data value is written. When the cache capacity reaches its upper limit, it should delete the least recently used data values ​​before writing new data to make room for new data values.

**Advanced:**

Can you do both operations in **O(1)** time complexity?

**Example:**

```
LRUCache cache = new LRUCache( 2 /* cache capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1); // return 1
cache.put(3, 3); // This operation will invalidate key 2
cache.get(2); // Return -1 (not found)
cache.put(4, 4); // This operation will invalidate key 1
cache.get(1); // Return -1 (not found)
cache.get(3); // return 3
cache.get(4); // return 4
```

### Question analysis

This question asks us to implement an LRU cache. LRU is the abbreviation of Least Recently Used, which means the least recently used.

This cache mainly has two member functions, get and put.

The get function obtains the value by inputting the key. If successfully obtained, the pair (key, value) rises to the most commonly used position (top) in the cache. If the key does not exist, -1 is returned.

The put function inserts a new pair of (key, value). If the key exists in the original cache, you need to delete the original one first and insert the new one at the top of the cache. If it does not exist, it is inserted directly to the top.

If the buffer exceeds capacity after adding new values, you need to delete the least commonly used value, which is the bottom value.

For specific implementation, we need three private variables, cap, l and m, where cap is the capacity of the cache, l is a list that stores the contents of the cache, and m is a HashMap, which stores the mapping between the key value key and the iterator of each cache item, so that we can find the target item in O(1) time.

Then let's look at how get and put are implemented.

Among them, get is relatively simple. We search for the given key in m and directly return -1 if it does not exist; if it exists, move the item to the top.

For put, we also search for the given key in m. If it exists, delete the original item and insert the new item at the top. Then determine whether it overflows. If it overflows, delete the bottom item (the least commonly used item).

### Animation description

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/90896.gif)

### Code implementation

```c++
class LRUCache{
public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        auto it = m.find(key);
        if (it == m.end()) return -1;
        l.splice(l.begin(), l, it->second);
        return it->second->second;
    }
    
    void put(int key, int value) {
        auto it = m.find(key);
        if (it != m.end()) l.erase(it->second);
        l.push_front(make_pair(key, value));
        m[key] = l.begin();
        if (m.size() > cap) {
            int k = l.rbegin()->first;
            l.pop_back();
            m.erase(k);
        }
    }
    
private:
    int cap;
    list<pair<int, int>> l;
    unordered_map<int, list<pair<int, int>>::iterator> m;
};
```





![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/inind.png)