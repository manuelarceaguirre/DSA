# Most common patterns for leetcode

## Arrays

### Two pointers
it uses two indices to traverse in an array
    - opposite ends
    - in the same direction 

'Pairs to sum a target'
'Reversing an array or string'
'Removing duplicate from sorted array'
'Merging 2 sorted arrays'


> Example
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
Example 1:

*Input:* numbers = [2,7,11,15], target = 9.

*Output:* [1,2]


Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1  # Start pointers at both ends
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed result
        elif current_sum < target:
            left += 1  # Need a larger sum, move left pointer
        else:
            right -= 1  # Need a smaller sum, move right pointer
    return []  # No solution found
```