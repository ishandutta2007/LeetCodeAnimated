# LeetCode Question No. 690: The Importance of Employees

> This article was first published on the public account "Learning Algorithms in Five Minutes" and is one of the series of articles [Illustrated LeetCode](<https://github.com/MisterBooo/LeetCodeAnimation>).
>
> Personal website: [https://www.cxyxiaowu.com](https://www.cxyxiaowu.com)

The question comes from LeetCode Question No. 690: The Importance of Employees.

### Title description

Given a data structure that stores employee information, it contains the employee's unique ID, importance and direct subordinate IDs.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. Their corresponding importance is 15, 10, 5. Then the data structure of employee 1 is [1, 15, [2]], the data structure of employee 2 is [2, 10, [3]], and the data structure of employee 3 is [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, because ** is not a direct subordinate, it is not reflected in the data structure of employee 1.

Now enter all employee information of a company, as well as a single employee ID, and return the sum of the importance of this employee and all his subordinates.

**Example 1:**

```
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
explain:
Employee 1's own importance is 5. He has two direct subordinates 2 and 3, and the importance of 2 and 3 is both 3. Therefore the total importance of employee 1 is 5 + 3 + 3 = 11.
```

**Notice:**

1. An employee can have at most one **direct** leader, but can have multiple **direct** subordinates
2. The number of employees does not exceed 2,000.

### 

### Question analysis

Use a hash table to store employee information. After finding the employee with the specified id, use a breadth-first traversal algorithm to traverse the employee with the id and its subordinate employees.

### Animation description

To be added

### Code implementation

```
public int getImportance(List<Employee> employees, int id) {
        Employee emp = null;
        //Importance
		int sum = 0;   
        //Storage employee information
		HashMap<Integer,Employee> map=new HashMap<Integer,Employee>();  /
	    for(Employee e:employees) {
	    	map.put(e.id, e);
	    }
	    //Use breadth first to traverse employees
	    ArrayDeque<Employee> queue=new ArrayDeque<Employee>();
	    queue.addLast(map.get(id));
	    while(!queue.isEmpty()) {
	    	emp=queue.removeFirst();
	    	sum+=emp.importance;
	    	for(int i:emp.subordinates) {
	    		queue.addLast(map.get(i));
	    	}
	    }
		return sum;

    }
```



![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/wvk3e.png)