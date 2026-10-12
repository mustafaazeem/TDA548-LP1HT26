'''
We write two algorithms for factorial problem 
    1 - iterative 
    2 - recursive 

The benchmark function calculates time for each algorithm's run
It takes thee arguments: 
1 - function: name of the function which it need to run
2 - input: input which it needs to pass to function 
3 - n: number of times it needs to run function(input)
'''
import time 

    
def fac_iterative(n):
    '''
    This function takes a number and produces its factorial
    '''

    factorial = 1
    for i in range(2,n+1):
        factorial *= i
    return factorial 

def fac_recursive(n):
    # Base case / Stopping condition 
    if n <= 1:
        return 1

    # Recursive case 
    else:
        return n * fac_recursive(n-1)


def benchmark(function, input, n):

    # note time before starting my function 
    start = time.perf_counter()
    for _ in range(n):
        function(input)
    
    # note time after ending my function 
    end = time.perf_counter()
    return end-start

print(f'benchmark fac_iterative {benchmark(fac_iterative, 600, 1000):.6f}')
print(f'benchmark fac_recursive {benchmark(fac_recursive, 6, 1000):.6f}')
