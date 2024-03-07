3
5
8
abcabc

import re


def find_pattern_occurrences(text):
    # Define the pattern using regular expression
    pattern = r'C\w+jeb'  # C followed by any number of letters and ending with jeb

    # Use re.findall to find all occurrences of the pattern in the text
    matches = re.findall(pattern, text)

    # Return the number of matches found
    return len(matches)




# Example usage:
text = "Cexamplejeb, Cpatternjeb, Ctestjeb"
print(find_pattern_occurrences(text))  # Output: 3

# Mutable list example
my_list = [1, 2, 3]
print("Original list:", my_list)

# Modify the list
my_list[0] = 10
print("Modified list:", my_list)  # Output: [10, 2, 3]

# Immutable string example
my_string = "hello"
print("Original string:", my_string)

# Attempting to modify the string (this will raise an error)
# my_string[0] = 'H'  # This will raise a TypeError

# Creating a new string with the modification
my_string = "Hello" + my_string[1:]
print("Modified string:", my_string)  # Output: "Hello"

import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Remove numbers greater than 50 and replace others with "XX"
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        random_numbers[i] = "XX"
    else:
        random_numbers[i] = "XX"

# Print the modified list
print(random_numbers)


def is_valid_url(url):
    # Check if the URL starts with "http://" or "https://"
    if url.startswith("http://") or url.startswith("https://"):
        return True
    else:
        return False

# Example usage:
url1 = "http://www.example.com"
url2 = "https://www.example.com"
url3 = "www.example.com"

print(is_valid_url(url1))  # Output: True
print(is_valid_url(url2))  # Output: True
print(is_valid_url(url3




def days_passed_since_birthday(birthday):
    # Extract birth year from the birthday string
    birth_year = int(birthday[-4:])

    # Get the current year (assuming it's 2024)
    current_year = 2024

    # Calculate the number of whole years between birth year and current year
    whole_years = current_year - birth_year - 1  # Subtracting 1 because we exclude birth year and current year

    # Calculate the total number of days passed since birth
    days_passed = whole_years * 365  # Assuming each year has 365 days

    # Add extra days for leap years
    leap_years = sum(
        1 for year in range(birth_year + 1, current_year) if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    days_passed += leap_years

    return days_passed


# Example usage:
birthday = "01-12-2003"
print(days_passed_since_birthday(birthday))  # Output will vary depending on the current year
