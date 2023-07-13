import time
# Recursive implementation of Fibonacci sequence
def fibonacci_recursive(n):
   return n if n <= 1 else fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Dynamic programming implementation of Fibonacci sequence with recursion
def fibonacci_dynamic(n, m={}):
    if n in m:
      return m[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci_dynamic(n - 1, m) + fibonacci_dynamic(n - 2, m)
    m[n] = result
    return result

# Time comparison
n = int(input("Enter the value of n: "))

start_time = time.time()
fib_recursive = fibonacci_recursive(n)
end_time = time.time()
recursive_time = end_time - start_time

start_time = time.time()
fib_dynamic = fibonacci_dynamic(n)
end_time = time.time()
dynamic_time = end_time - start_time

print("Fibonacci number (recursive):", fib_recursive)
print("Time taken (recursive):", recursive_time)
print("\nFibonacci number (dynamic):", fib_dynamic)
print("Time taken (dynamic):", dynamic_time)
