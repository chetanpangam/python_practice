# factorial.py
# Find the factorial of the given number recursively

def fact(n):
    if n == 0:
        return 1

    result = n * fact(n-1)

    return result

n =10

print(fact(n))