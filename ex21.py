#defines the function add to add the two variables and then 'return' allows the result of a + b to be used in a variable that runs the function
def add(a , b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} + {b}")
    return a - b

def multiply(a , b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions:")

age = add(20, 3)
height = subtract(80, 4)
weight = multiply(88, 2)
iq = divide(250, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"That becomes {what}, can you do it by hand?")
