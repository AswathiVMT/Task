#1. Arithmatic calculator
def calculator(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"


print(calculator('add', 20, 5))
print(calculator('subtract', 10, 5))
print(calculator('multiply', 10, 5))
print(calculator('divide', 20, 5))

#2.Area calculator
import math

def area_calculator(shape, *args):
    if shape == 'circle':
        radius = args[0]
        return math.pi * (radius ** 2)
    elif shape == 'square':
        side = args[0]
        return side ** 2
    elif shape == 'rectangle':
        length, width = args[0], args[1]
        return length * width
    elif shape == 'triangle':
        base, height = args[0], args[1]
        return 0.5 * base * height
    else:
        return "Invalid shape"


print(area_calculator('circle', 5))
print(area_calculator('square', 4))
print(area_calculator('rectangle', 4, 5))
print(area_calculator('triangle', 4, 5))

#3.Temperature converter
def temperature_converter(temp, unit):
    if unit == 'C':
        return (temp * 9/5) + 32  # Convert Celsius to Fahrenheit
    elif unit == 'F':
        return (temp - 32) * 5/9  # Convert Fahrenheit to Celsius
    else:
        return "Invalid unit"

print(temperature_converter(100, 'C'))
print(temperature_converter(212, 'F'))

#List Manipulation

L = [20,11,5,7,8,5,39,25,10]

largest = max(L)
smallest = min(L)
average = sum(L) / len(L)

print(largest)
print(smallest)
print(average)

# Dictionary 
person = {
    "name": "sree",
    "age": 30,
    "city": "Calicut"
}

# Accessing the values
name = person["name"]
age = person["age"]
city = person["city"]

print(name)
print(age)
print(city)

# string
text = "Hello, how are you?"

vowels = "aeiouAEIOU"

# Count the number of vowels
vowel_count = sum(1 for char in text if char in vowels)

print(vowel_count)




