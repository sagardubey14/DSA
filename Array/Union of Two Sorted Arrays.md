---
## Problem Statement

Given two sorted arrays, `a` and `b`, of size `n` and `m`, respectively, return the union of the arrays.

The union of two sorted arrays can be defined as an array consisting of the common and the distinct elements of the two arrays. The final array should be sorted in ascending order.

**Note:** `a` and `b` may contain duplicate elements, but the union array must contain unique elements.

### Example

**Input:** 
- `n` = 5
- `m` = 3
- `a` = [1, 2, 3, 4, 6]
- `b` = [2, 3, 5]

**Output:** [1, 2, 3, 4, 5, 6]

---

---

### Method 1: Using Dictionary for Frequency Count

**Description:**
- This method utilizes a dictionary to count the frequency of elements in both arrays `a` and `b`.
- Elements from both arrays are iterated through separately, and their frequencies are updated in the `freq` dictionary.
- Unique elements are extracted from the dictionary and appended to the `union` list.
- Finally, the `union` list is sorted in ascending order.

---

### Method 2: Using Two Pointer Approach

**Description:**
- This method employs a two-pointer approach to merge two sorted arrays `arr1` and `arr2` into a single sorted array.
- Two pointers `i` and `j` are used to traverse the arrays `arr1` and `arr2` respectively.
- At each step, the smaller element among `arr1[i]` and `arr2[j]` is added to the `result` list.
- After one array is exhausted, the remaining elements from the other array are added to the `result` list.
- Finally, the `result` list containing the union array is printed.

---
