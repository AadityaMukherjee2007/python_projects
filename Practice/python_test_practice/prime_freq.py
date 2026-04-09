def prime_factors(n):
    primeFacs = dict()

    i = 2
    while i * 1 <= n:
        while n % i == 0:
            primeFacs[i] = primeFacs.get(i, 0) + 1
            n //= i
        i += 1

    if n > 1:
        primeFacs[n] = primeFacs.get(n, 0) + 1

    return primeFacs

def main():
    n = int(input("n: "))
    print(f"Prime Factors: {prime_factors(n)}")

if __name__ == "__main__":
    main()
