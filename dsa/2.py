"""
Print Name N times using Recursion

Problem Description: Given an integer N, write a program to print your name N times.

Examples
Input: N = 3
Output: Ashish Ashish Ashish 
Explanation: Name is printed 3 times.
Input: N = 1
Output: Ashish 
Explanation: Name is printed once.

"""
def recur1(N, name):
    print(name)
    if N == 1:
        return
    recur(N-1, name)


"""
Print 1 to N using Recursion

Problem Description: Given an integer N, write a program to print numbers from 1 to N.

Input: N = 4
Output: 1, 2, 3, 4
Explanation: All the numbers from 1 to 4 are printed.
Input: N = 1
Output: 1 
Explanation: This is the base case.

"""
def recur2(num, N):
    print(num)
    if num == N:
        return
    num = num + 1
    recur2(num, N)


"""
Print N to 1 using Recursion

Problem Description: Given an integer N, write a program to print numbers from N to 1.

Examples
Input: N = 4
Output: 4, 3, 2, 1
Explanation: All the numbers from 4 to 1 are printed.
Input: N = 1
Output: 1 
Explanation: This is the base case.
"""

def recur3(N):
    print(N)
    if N == 1:
        return N
    recur3(N-1)

def recur4(nums, N) -> list:
    nums.append(N)
    if N == 1:
        return nums
    return recur4(nums, N-1)
    

"""
Sum of first N Natural Numbers

Problem Statement: Given a number N, find out the sum of the first N natural numbers .

Examples
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15

"""
def  recur5(N) -> int:
    if N == 1:
        return 1
    return N + recur5(N-1)


"""
Factorial of a Number : Iterative and Recursive

Problem Statement: Given a number X,  print its factorial.

To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.

Note: X  is always a positive number. 

Examples
Example 1:
Input:
 X = 5
Output:
 120
Explanation:
 5! = 5*4*3*2*1

Example 2:
Input:
 X = 3
Output:
 6
Explanation:
 3!=3*2*1
"""

def recur6(N)-> int:
    if N == 1:
        return 1
    return N * recur6(N-1)


"""
Reverse a given Array
Problem Statement: You are given an array. The task is to reverse the array and print it.

Examples
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.
"""

def recur7(arr, start, end) -> list:
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

    return recur7(arr, start, end)


"""
Check if the given String is Palindrome or not

Problem Statement: Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.

Examples
Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.
            
"""
def recur8(s, start, end):
    if s[start] != s[end]:
        return False
    if start >= end:
        return True
    start += 1
    end -= 1
    return recur8(s, start, end)


"""
Print Fibonacci Series up to Nth term
Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

Examples
Example 1:
Input: N = 5
Output: 0 1 1 2 3 5
Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

Example 2:
Input: 6
Output: 0 1 1 2 3 5 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)        

"""
def recur9(N):
    if N <= 1:
        return N
    return recur9(N-1) + recur9(N-2)


if __name__ == "__main__":
    for i in range(3):
        print(recur9(i), end=" ")