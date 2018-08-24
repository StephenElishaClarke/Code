def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
            print(memo)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
       return 0
    elif n == 1:
       return 1
    else:
       return fib(n-1)+fib(n-2)

n = input("Enter the desired nth term of the fibonacci sequence: ")
#n = int(n)
print(fib(n))


@memoize
def s(n):
    if n == 0:
       return 0
    elif n == 1:
       return 1
    elif n == 2:
       return 2
    else:
       return s(n-1)+s(n-3)

print(s(n))

###################################################################


import pickle
fn = open("data.pkl", "w")
pickle.dump(fib(n), fn)
fn.close()

with open('data.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)

