# ------------------------------------------------------
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# ------------------------------------------------------

def e(a, b):
    return int(eval(str(a) + b))

def zero(n=""): return e(0, n)
def one(n=""): return e(1, n)
def two(n=""): return e(2, n)
def three(n=""): return e(3, n)
def four(n=""): return e(4, n)
def five(n=""): return e(5, n)
def six(n=""): return e(6, n)
def seven(n=""): return e(7, n)
def eight(n=""): return e(8, n)
def nine(n=""): return e(9, n)

def plus(n=""): return f"+{n}"
def minus(n=""): return f"-{n}"
def times(n=""): return f"*{n}" 
def divided_by(n=""): return f"/{n}" 

if __name__ == '__main__':
    print(seven(times(five()))) # 35
    print(seven(times(5)))
    print(four(plus(nine()))) # 13 
    print(eight(minus(three()))) # 5
    print(six(divided_by(two()))) # 3