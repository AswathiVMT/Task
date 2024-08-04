# 1) find largest number
def largest_number(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    
    return largest

numbers = [3, 5, 7, 2, 8 ,1]
print(largest_number(numbers)) 

#or
list1 = [15,20,18, 4, 45, 99]
print("Largest element is:", max(list1))

# 2) check palindrome 

def Palindrome(string):
   
    cleaned_str = ''.join(char.lower() for char in string if char.isalnum())
    
    if cleaned_str == cleaned_str[::-1]:
        return "The string is a palindrome."
    else:
        return "The string is not a palindrome."

string = input("Enter string: ")

print(Palindrome(string))

#3) check prime
def is_prime(n):
    
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(7)) 
print(is_prime(4)) 

#4)
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count

string = "variance"
print(count_vowels(string)) 

#5)

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

number =512068
print(sum_of_digits(number))  