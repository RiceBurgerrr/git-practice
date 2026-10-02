def mul(a, b):
    return a * b


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print(mul(7, 9))
    print(add(4, 2))
    print(sub(6, 4))
    print(div(4, 2))
