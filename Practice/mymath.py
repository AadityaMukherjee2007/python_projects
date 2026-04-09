def add(*args):
    return sum(*args)

def mul(*args):
    result = 1
    for i in list(*args):
        result *= i
    return result

def main():
    # print(__name__)
    print(add([1, 2, 3]))
    print(mul([1, 3, 5]))


if __name__ == "__main__":
    main()
