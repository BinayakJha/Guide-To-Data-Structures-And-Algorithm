import re

# Regex to remove non-alphanumeric
def remove_non_alphanumeric(string):
    string = re.sub(r'\W+', '', string)
    return string

def is_palindrome(string):
    formatted_string = remove_non_alphanumeric(string).lower()
    length = len(formatted_string)

    return all(
        formatted_string[i] == formatted_string[length - 1 - i]
        for i in range(length // 2)
    )

if __name__ == '__main__':
    string = input('Enter a string: ')
    print(is_palindrome(string))