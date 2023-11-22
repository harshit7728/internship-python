# 1. Check if a given string is a palindrome or not.

def is_palindrome(s):
    return s == s[::-1]
ans = is_palindrome("122")
if ans:
    print("yes")
else:
    print("no")

# 2. Concatenate two strings into a single string.
def concatenate_strings(str1, str2):
    return str1 + str2
ans = concatenate_strings("hello","world")
print(ans)




# 3. Calculate the sum of elements in a list of integers.
def sum_of_elements(lst):
    return sum(lst)
list1 =[1,2,3,4]
print(sum_of_elements(list1))


# 4. Reverse the order of elements in a list without using the reverse() method.
def reverse_list(lst):
    return lst[::-1]
list1=[1,2,3,4,5]
print(reverse_list(list1))


# 5. Sort a list of strings in ascending order.
def sort_strings(lst):
    return sorted(lst)
list1=[4,3,5,6,7]
print(sort_strings(list1))
# 6. Remove duplicates from a list while preserving the order of elements.
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if x not in seen and not seen.add(x)]

# 7. Perform basic arithmetic operations (addition, subtraction, multiplication, division) using user input.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
addition_result = a + b
subtraction_result = a - b
multiplication_result = a * b
division_result = a / b if b != 0 else "Cannot divide by zero"

# 8. Check if a given number is even or odd.
def is_even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# 9. Check whether a given year is a leap year or not.
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 10. Use logical operators (AND, OR, NOT) to check conditions and return True or False.
condition1 = True
condition2 = False
result_and = condition1 and condition2
result_or = condition1 or condition2
result_not = not condition1

# 11. Find the maximum and minimum values in a list of numbers.
def find_max_min(lst):
    return max(lst), min(lst)

# 12. Check if a string is a pangram (contains all letters of the alphabet).
import string

def is_pangram(sentence):
    return set(sentence.lower()) >= set(string.ascii_lowercase)

# 13. Split a string into words and count the frequency of each word.
def word_frequency(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# 14. Find the intersection of two lists (common elements).
def find_intersection(list1, list2):
    return list(set(list1) & set(list2))

# 15. Create a dictionary from two lists (keys and values).
keys = ["name", "age", "gender"]
values = ["John", 25, "Male"]
result_dict = dict(zip(keys, values))

# 16. Check if all elements in a list are unique.
def are_elements_unique(lst):
    return len(lst) == len(set(lst))

# 17. Merge two sorted lists into a single sorted list.
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

# 18. Rotate elements in a list by a specified number of positions.
def rotate_list(lst, positions):
    return lst[positions:] + lst[:positions]

# 19. Determine the factorial of a given number.
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

# 20. Find the second largest element in a list of numbers.
def second_largest(lst):
    unique_elements = list(set(lst))
    if len(unique_elements) < 2:
        return "List doesn't have a second largest element"
    unique_elements.sort()
    return unique_elements[-2]
