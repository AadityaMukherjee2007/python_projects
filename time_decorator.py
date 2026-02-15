import time

def runtime(func):
    def enhanced_fn(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        time_elapsed = time.time() - start
        print(f"Function {func.__name__} took {time_elapsed:.5f} seconds to run.\n")
        return result 
    return enhanced_fn

def runtime_precise(func):
    def enhanced_fn(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - start
        print(f"Function {func.__name__} took {time_elapsed:.5f} seconds to run.\n")
        return result 
    return enhanced_fn

@runtime
# @runtime_precise
def fac():
    n = 10
    fac = 1
    for i in range(2, n + 1):
        fac *= i
    
    print(f"{n}! = {fac}")


@runtime
def find_prime():
    c = 0
    for i in range(10000):
        if is_prime(i):
            c += 1
    print(f"{c} primes found.")


# @runtime
@runtime_precise
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            return False
        
    return True

@runtime
def brew_tea(tea_type, steep_time):
    print(f"Brewing {tea_type} tea...")
    time.sleep(steep_time)
    print("Tea is ready!")


@runtime 
def make_matcha():
    print("Making matcha...")
    time.sleep(1)
    print("Matcha is ready!")

fac()
print(is_prime(100013))
brew_tea(tea_type="green", steep_time=1)
brew_tea("black", 2)
make_matcha()  
# find_prime()
