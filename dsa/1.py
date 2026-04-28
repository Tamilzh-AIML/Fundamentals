"""
****
****
****
****

"""
def pattern1(N):
    for row in range(N):
        print('*'* N)

"""
*
**
***
****
"""
def pattern2(N):
    for row in range(N):
        for col in range(N):
            if col <= row:
                print('*', end="")
        print()

"""
1
12
123
1234
"""
def pattern3(N):
    for row in range(N):
        for col in range(row+1):
            print(col+1, end="")
        print()

"""
1
22
333
4444
"""
def pattern4(N):
    for row in range(N):
        for _ in range(row+1):
            print(row+1, end="")
        print()

"""
****
***
**
*
"""
def pattern5(N):
    for row in range(N):
        for _ in range(N-row):
            print('*',end="")
        print()

"""
1234
123
12
1
"""
def pattern6(N):
    for row in range(N):
        for col in range(N-row):
            print(col+1, end="")
        print()

""" 
  *
 *** 
*****

N = 3

"""
def pattern7(N):
    counter = 1
    for row in range(N):
        for space1 in range(N-row-1):
            print(" ",end="")
        for stars in range(row+counter):
            print('*', end="")
        for space2 in range(N-row-1):
            print(" ", end="")
        counter += 1
        print()

"""
*****
 *** 
  *
N = 3

"""
def pattern8(N):
    counter = N + (N-1)
    for row in range(N):
        for space1 in range(row):
            print(" ",end="")
        for starts in range(counter):
            print('*', end="")
        for space2 in range(row):
            print(" ", end="")
        counter -= 2
        print()

"""
  *
 *** 
*****
*****
 *** 
  *

N = 3
"""
def pattern9(N):
    pattern7(N)
    pattern8(N)

"""
*
**
***
****
*****
****
***
**
*

N=5
"""
def pattern10(N):
    #upperset
    for row in range(1, N):
        print('*' * row)
    #lowerset
    for row in range(N, 0, -1):
        print('*' * row)

"""
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1

N = 5
"""
def pattern11(N):
    value = 1
    for row in range(N):
        for numbers in range(row +1):
            print(value, end="")
            value = 0 if value == 1 else 1
        print()



if __name__  == "__main__":
    pattern11(5)