## LeetCode Question No. 118: Yang Hui Triangle

> This article was first published on the public account "Illustrated Interview Algorithm" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal blog: www.zhangxiaoshuai.fun

**This question is selected from Leetcode question 118, easy level, current pass rate is 66.4%**
### Title description:
```
Given a nonnegative integer numRows, generate the first numRows rows of Yang Hui's triangle.
Example:

Input: 5
Output:
[
    	 [1],
   	 	[1,1],
  	   [1,2,1],
  	  [1,3,3,1],
 	 [1,4,6,4,1]
]
```

### Question analysis:
The Yang Hui triangle that I learned in junior high school unexpectedly appeared here again. The meaning of the question is easy to understand. The first number and the last number in each row are both 1, and the middle number is obtained by adding the two adjacent numbers above. The question gives us the number of non-negative rows of a Yang Hui triangle, and then we generate the corresponding Yang Hui triangle (set).
Since a List<List<Integer>> is returned, we use a large collection to store the numbers in each row, and we use a small collection to store the numbers in each row, and finally add each small collection to the large collection.

### gif animation demonstration:

There are already very good GIF illustrations in the official website, which are directly displayed here:

![](../Animation/resource.gif)

### Code:

```java
public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> triangle = new ArrayList<List<Integer>>();
    //When the given numRows is 0, just return the empty collection directly
    if (numRows == 0) {
        return triangle;
    }

    //Because the first row of Yang Hui's triangle is always 1, create a new list first and add 1 to the list.
    triangle.add(new ArrayList<>());
    triangle.get(0).add(1);

    //Starting from the second line, create a new list representing the current line, and get the list of the previous line of the current line.
    for (int rowNum = 1; rowNum < numRows; rowNum++) {
        List<Integer> row = new ArrayList<>();
        List<Integer> prevRow = triangle.get(rowNum-1);

        //The first element in a row
        row.add(1);

        //For each row, the two adjacent elements of the previous row are added together to obtain the number between the two 1's.
        for (int j = 1; j < rowNum; j++) {
            row.add(prevRow.get(j-1) + prevRow.get(j));
        }

        //The last element in a row
        row.add(1);

        //Finally add "the entire row to the large collection"
        triangle.add(row);
    }
	return triangle;
}
```


