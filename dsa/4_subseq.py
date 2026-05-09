"""
Count all subsequences with sum K

Problem Statement: Given an array nums and an integer k.Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.

Examples
Example 1:
Input :
 nums = [4, 9, 2, 5, 1] , k = 10
Output :
 2
Explanation :
 The possible subsets with sum k are [9, 1] , [4, 5, 1].

Example 2:
Input :
 nums = [4, 2, 10, 5, 1, 3] , k = 5
Output :
 3
Explanation :
 The possible subsets with sum k are [4, 1] , [2, 3] , [5].

"""

"""
Base condition:
--------------
where the current iter == len(arr)
    if sum of the subsequence == k
        print(subseq)

Until:
-----
add the current index ele to the subseq arr
recur

Until2:
-------
pop the last ele of the subseq arr
recur again


"""

class Subseq():
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
    
    def subseq(self, index, current_sum, current_subseq):
        if index == len(self.arr):
            if current_sum == self.k:
                print(current_subseq)
            return
        current_subseq.append(self.arr[index])
        self.subseq(index + 1, current_sum + self.arr[index], current_subseq)

        current_subseq.pop()
        self.subseq(index + 1, current_sum, current_subseq)


"""
Combination Sum - 1
Problem Statement: 

Given an array of distinct integers and a target, you have to return the list of all unique combinations where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from the given array an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Examples
 Example 1:
Input: array = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
             7 is a candidate, and 7 = 7.
             These are the only two combinations.


Example 2:
Input: array = [2], target = 1
Output: []
Explaination: No combination is possible.
        
"""

"""
distinct integers
target

target = 7
num = 2 (index = 0, freq = 1)
diff = 5
    no 5 in arr
num = 2 (index = 0, freq = 2)
diff = 3
    3 is present in arr and (2 + 2 + 3) sums upto 7 --> print
num =2 (index = 0, freq = 3)
diff = 1
    no 1 in arr
num = 2 (index =0, freq = 4)
diff = -1
break

num = 3 (index = 1, freq = 1)
diff = 4
    no 4 in arr
num = 3 (indexx = 1, freq = 2)
diff = 1
    no 1 in arr

num = 6 (index = 2, freq = 1)
...
"""
class CombSum1():
    def __init__(self, arr) -> None:
        self.arr = arr 
        self.output = []
    
    def find_combinations(self, index, target, temp):
        if index == len(self.arr):
            if target == 0:
                self.output.append(list(temp))
            return
        
        if self.arr[index] <= target:
            temp.append(self.arr[index])
            self.find_combinations(index, target - self.arr[index], temp)
            temp.pop()

        self.find_combinations(index + 1, target, temp)
        return self.output



"""
Combination Sum II - Find all unique combinations

Problem Statement: Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination..

Examples
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]]
Explanation: These are the unique combinations whose sum is equal to target.
 
Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
Explanation: These are the unique combinations whose sum is equal to target.
            
"""


"""
Base condition:
--------------
if index == len(arr) and target == 0
    ouput.append(temp)


Forward tracking:
----------------

arr[index] <= target
temp.append(arr[index])
call(index + 1, target -= arr[index], temp)


Backward tracking:
-----------------
temp.pop()
call(index + 1, target, temp)
"""
class CombSum2():
    def __init__(self, arr) -> None:
        self.arr = sorted(arr)
        self.output = []

    def find_combinations(self, index, target, temp):
        if index == len(self.arr):
            if target == 0:
                self.output.append(list(temp))
            return
        
        if self.arr[index] <= target:
            temp.append(self.arr[index])
            self.find_combinations(index+1, target - self.arr[index], temp)
            temp.pop()
            
        next_index = index + 1
        while next_index < len(self.arr) and self.arr[next_index] == self.arr[index]:
            next_index += 1

        self.find_combinations(next_index, target, temp)
        return self.output

            
"""
Combination Sum III
Problem Statement: Determine all possible set of k numbers that can be added together to equal n while meeting the following requirements:
1. There is only use of numerals 1 through 9.
2. A single use is made of each number.
Return list of every feasible combination that is allowed. The combinations can be returned in any order, but the list cannot have the same combination twice.

Examples
Example 1:
Input:
 k = 3, n = 7
Output:
 [[1, 2, 4]]
Explanation:

1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input:
 k = 3, n = 9
Output:
 [[1, 2, 6],[1, 3, 5],[2, 3, 4]]
Explanation:

1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

"""

"""
input_arr = 1-9, one time use, 
k = 3 ( no of digits)
n = 7 (target)
temp = []

index = 0

base condition:
if target == 0:
    output.append(list(temp))

forward tracking:

if arr[index] <= target and len(temp) <= k
    temp.append(arr[index])
    target -= arr[index]
    call(index+1, target, temp)

backward trackong:

temp.pop()
call(index, target, temp)
"""

class CombSum3():
    def __init__(self, k):
        self.arr = list(range(1, 10))
        # print('array : ', self.arr)
        self.no_of_digits = k
        self.output = []

    def find_combinations(self, index, target, temp):

        if target == 0 and len(temp) == self.no_of_digits:
            self.output.append(list(temp))
            return
        if target < 0 or index >= len(self.arr):
            return
        if self.arr[index] <= target and len(temp) <= self.no_of_digits:
            temp.append(self.arr[index])
            self.find_combinations(index + 1, target - self.arr[index], temp)
            temp.pop()
        
        self.find_combinations(index + 1, target, temp)
        return self.output


"""
Subset Sum : Sum of all Subsets
Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.

Examples

Input: N = 3, arr[] = {5,2,1}
Output: 0,1,2,3,5,6,7,8
Explanation: We have to find all the subset's sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],so the sums we get will be  0,1,2,3,5,6,7,8

Input: N=3,arr[]= {3,1,2}
Output: 0,1,2,3,3,4,5,6
Explanation: We have to find all the subset's sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [3], [3,1], [3,2]. [3,2,1],so the sums we get will be  0,1,2,3,3,4,5,6

"""
"""

sort(arr)

base condition:
if index == 0:
    print([])
if index == len(arr):
    list(current_sum)

forward tracking:
temp.append(arr[index])
call(index + 1, current_sum + arr[index], temp)
temp.pop()

backward tracking:
call(index + 1, cuurent_sum,temp)

"""
class Subsets():
    def __init__(self, arr):
        self.arr = arr
        self.output = []
    
    def find_sums(self, index, current_sum):
        if index == len(self.arr):
            self.output.append(current_sum)
            return
        
        self.find_sums(index+1, current_sum + self.arr[index])

        self.find_sums(index+1, current_sum)
        return sorted(self.output)
    

        

if __name__ == "__main__":
    obj = Subsets([3,1,2])
    print(obj.find_sums(0, 0))



