def calculate_S1(m):
    result = 0
    for i in range(m+1):
        result += i + (i**2)
    return result

def calculate_S1_recursive(m):
    if m == 0: return 0
    else: return m + m**2 + calculate_S1_recursive(m-1)

def calculate_S2(m, n):
    """nested for loops so pretty much O(n^2)"""
    S2 = 0
    for i in range(1, m + 1):
        for j in range(i, n + 1):
            S2 += j + i
    return S2

def calculate_S3(m, n):
    """nested for loops so pretty much O(n^2)"""
    S3 = 0
    for i in range(1, m + 1):
        for j in range(i, n + 1):
            S3 += (j / i)
    return S3

#/
def f(x): return x**2 
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    result = (func(a) + func(b)) / 2.0

    for i in range(1, n):
        result += func(a + i * h)

    result *= h
    return result

a_value = 0
b_value = 2
n_value = 100

result = round(trapezoidal_rule(f, a_value, b_value, n_value), 4) #rounded to 4 decimals

print(f"The approximate integral using the Trapezoidal Rule is: {result}")
print("_____END_[TRAPEZOIDAL]_____")


# Implementing Simpson's 1/3 
def f(x): return x**2
def simpson13(x0,xn,n):
    h = (xn - x0) / n
    # Finding sum 
    integration = f(x0) + f(xn)
    for i in range(1,n):
        k = x0 + i*h
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    # Finding final integration value
    integration = integration * h/3
    
    return integration
    
# Input section
lower_limit = 0
upper_limit = 1
sub_interval = 4

# Call trapezoidal() method and get result
result = simpson13(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result) )