"""
Puzzle 12:

The Fibonacci sequence is 0,1,1,2,3,5,8,13...
The definition of the Fibonacci sequence is:
    f_n = f_n-2 + f_n-1 for n >= 0
    where f_0 = 0 and f_1 = 1

Find the n value of a generic Fibonacci sequence with this recursion.
"""


def fib(f_0, f_1, n):
    if n == 0:
        return f_0
    if n == 1:
        return f_1
    return fib(f_0, f_1, n - 2) + fib(f_0, f_1, n - 1)


if __name__ == "__main__":

    print(fib(0, 1, 7))
    print(fib(3, 4, 2))
