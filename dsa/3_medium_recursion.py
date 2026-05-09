"""
Recursive Implementation of atoi()

Problem Statement: Implement the function myAtoi(s) which converts the given string s to a 32-bit signed integer (similar to the C/C++ atoi function).

Steps to Implement: 1. First, ignore any leading whitespace characters ' ' until the first non-whitespace character is found.
2. Check the next character to determine the sign. If it's a '-', the number should be negative. If it's a '+', the number should be positive. If neither is found, assume the number is positive.
3. Read the digits and convert them into a number. Stop reading once a non-digit character is encountered or the end of the string is reached. Leading zeros should be ignored during conversion.
4. The result should be clamped within the 32-bit signed integer range: [-2147483648, 2147483647]. If the computed number is outside this range, return -2147483648 if the number is less than -2147483648, or return 2147483647 if the number is greater than 2147483647.
5. Finally, return the computed number after applying all the above steps.

Examples
Example 1:
Input:
 s = " -12345"  
Output:
 -12345  
Explanation:
  
Ignore leading whitespaces.  
The sign '-' is encountered, indicating the number is negative.  
Digits 12345 are read and converted to -12345.

Example 2:
Input:
 s = "4193 with words"  
Output:
 4193  
Explanation:
  
Read the digits 4193 and stop when encountering the first non-digit character (w).

"""

"""

1. removing the leading whitespace
2. append the sign if present

Base Condition:
--------------
non-digit character --> alphas, whitespace, symbols
end of the given string
    returning the output

Until:
-----
append the digits and move the index by 1 until the end of the string/non-digit character comes,  to construct the output

"""

class AtoI():

    def __init__(self, s) -> None:
        self.s = s.lstrip()
        self.output = ''
        self.index = 0

        if self.s[self.index]== '-':
            self.output += self.s[self.index]
            self.index += 1

    def atoi(self):
        if self.index >= len(self.s) or not self.s[self.index].isdigit():
            if not self.output or self.output in ["-", "+"]:
                return 0
        
            val = int(self.output)
            INT_MIN, INT_MAX = -2147483648, 2147483647
            if val < INT_MIN: 
                return INT_MIN
            if val > INT_MAX: 
                return INT_MAX
            return val
        
        self.output += self.s[self.index]
        self.index += 1
        return self.atoi()



"""
Implement Pow(x,n) | X raised to the power N

Problem Statement: Implement the power function pow(x, n) , which calculates the x raised to n i.e. xn.

Examples
Example 1:
Input:
 x = 2.0000, n = 10  
Output:
 1024.0000  
Explanation:
 The answer is calculated as 2^10, which equals 1024.

Example 2:
Input:
 x = 2.0000, n = -2  
Output:
 0.2500  
Explanation:
 The answer is calculated as 2^(-2), which is equal to 1/4 = 0.25.

"""

"""

Initial:
-------
1. check if n is -ve. if so, i have to inverse the answer ( 1/ ans)

Base Condition:
---------------
1. if the current iteration is equal to modulus value of n
    return the output

Until:
-----

mulitply the value of x with n
increament the current iteration count
call myself


"""

class Poww():
        
    def calc_pow(self, base, power):
        if power == 0:
            return 1
        half = self.calc_pow(base, power // 2 )

        if power % 2 == 0:
            answer = half * half
        else:
            answer = half * half * base
        return answer
    
    def get_results(self, base, power):
        if power < 0:
            return 1/self.calc_pow(base, (-1 * power))
        return self.calc_pow(base, power)
        

    


"""
Count Good numbers
Problem Statement: A digit string is considered good if the digits at even indices (0-based) are even digits (0, 2, 4, 6, 8) and the digits at odd indices are prime digits (2, 3, 5, 7).

Given an integer n, return the total number of good digit strings of length n. As the result may be large, return it modulo 109 + 7.

A digit string is a string consisting only of the digits '0' through '9'. It may contain leading zeros.

Examples
Example 1:
Input:
 n = 1
Output:
 5
Explanation:
 Only one index (0) → must be even.
Valid strings: "0", "2", "4", "6", "8"

Example 2:
Input:
 n = 2
Output:
 20
Explanation:
 Index 0: 5 options (even digits)
Index 1: 4 options (prime digits)
Total: 5 * 4 = 20

"""

"""
even place = 0,2,4,6,8
odd place = 2,3,5,7

n = 2

0th = 0,2,4,6,8
1st = 2,3,5,7

P & C = 5 * 4
==> 20 (02, 03, 05, 07...)

n = 3

0th = 0,2,4,6,8
1st = 2,3,5,7
2nd = 0,2,4,6,8

==> 5 * 4 * 5 = 100


counter = 0 --> num
output = 1

Base condition:
--------------
counter == num --> return output

until:
-----

if odd: output * 4
if even: output * 5

"""

class CountGN():
    def __init__(self, num):
        self.num = num
        self.counter, self.output = 0, 1
    
    def countgoodnum(self):
        if self.counter == self.num:
            return self.output
        
        if self.counter % 2 == 0:
            self.output *= 5
        else:
            self.output *= 4
        self.counter += 1
        return self.countgoodnum()


"""
Sort a Stack
Problem Statement: You are given a stack of integers. Your task is to sort the stack in descending order using recursion, such that the top of the stack contains the greatest element. You are not allowed to use any loop-based sorting methods (e.g., quicksort, mergesort). You may only use recursive operations and the standard stack operations (push, pop, peek/top, and isEmpty).

Examples
Example 1:
Input:
 stack = [4, 1, 3, 2]
Output:
 [4, 3, 2, 1]
Explanation:
 After sorting, the largest element (4) is at the top, and the smallest (1) is at the bottom.

Example 2:
Input:
 stack = [1]
Output:
 [1]
Explanation:
 A single-element stack is already sorted.

"""

class SortStack():
    def __init__(self, input_stack):
        self.input_stack = input_stack
        self.output_stack = []
        self.current_iter = 0
        self.temp = []
    
    def sortstack(self):
        if not self.input_stack:
            return self.output_stack

        if self.current_iter == 0:
            self.output_stack.append(self.input_stack.pop())
            self.current_iter += 1
            return self.sortstack()
        
        i_ele = self.input_stack.pop()

        while len(self.output_stack) != 0 and i_ele > self.output_stack[-1]:
            self.temp.append(self.output_stack.pop())
            
        self.output_stack.append(i_ele)
        self.output_stack.extend(reversed(self.temp))
        self.temp = []
        self.current_iter += 1
        return self.sortstack()


"""
Reverse a stack using recursion

Problem Statement: You are given a stack of integers. Your task is to reverse the stack using recursion. You may only use standard stack operations (push, pop, top/peek, isEmpty). You are not allowed to use any loop constructs or additional data structures like arrays or queues.

Your solution must modify the input stack in-place to reverse the order of its elements.

Examples
Example 1:
Input:
 stack = [4, 1, 3, 2]  
Output:
 [2, 3, 1, 4]

Example 2:
Input:
 stack = [10, 20, -5, 7, 15]  
Output:
 [15, 7, -5, 20, 10]

"""
"""
BaseCondition:
-------------
if start pointer >= end pointer -> return the stack as output

Until:
-----
swap the start and end pointer values
inc the start, dec the end by 1
call itself 

"""

class RevStack():
    def __init__(self, stack):
        self.stack = stack
        self.start = 0
        self.end = len(stack) - 1
    
    def reverse(self):
        if self.start >= self.end:
            return self.stack
        self.stack[self.start], self.stack[self.end] = self.stack[self.end], self.stack[self.start]
        self.start += 1
        self.end -= 1
        return self.reverse()
    
class RevStack2():
    def __init__(self, stack) -> None:
        self.stack = stack

    def insert_at_bottom(self, val):
        if not self.stack:
            self.stack.append(val)
            return
        top_val = self.stack.pop()
        self.insert_at_bottom(val)
        self.stack.append(top_val)
        

    def reverse(self):
        if not self.stack:
            return
        val = self.stack.pop()
        self.reverse()
        self.insert_at_bottom(val)


    





if __name__ == "__main__":              
    obj = RevStack2([1,2,3])
    obj.reverse()
    print(obj.stack)
