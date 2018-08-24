# A decorator function which checks the conditions of an input before passing to a function to avoid errors

def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper
    

@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(5, factorial(5))
#print(factorial(-1))

#########################################################

# A decorator function that tracks the number of times a function is called

def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1

print(succ.calls)
for i in range(10):
    succ(i)
    
print(succ.calls)
