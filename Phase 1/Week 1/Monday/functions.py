def greet():
    print("Hello, World!")
greet()  #To call the function

#return statement
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  


def add(a, b=5):
    return a + b

print(add(10))

#Find the Square of a Number
def square(num):
    return num * num

print(square(4))

