def group_permutations_of_palindromes(strings):
    permutations_of_palindromes = {}

    # Iterate through all O(n) strings in our array
    for string in strings:
        if is_permutation_of_palindrome(string):
            # Sort our string's order O(c log c)
            # Permutations will sort to the same string
            sorted_string = ''.join(sorted(string))

            # Initialize the key to an array if we
            # haven't seen any of the string's permutations yet
            if sorted_string not in permutations_of_palindromes:
                permutations_of_palindromes[sorted_string] = []

            permutations_of_palindromes[sorted_string].append(string)

    # This will return all the values of the hash table as an array
    # Since the values are also arrays, this is the form of the result we want\
    return print(list(permutations_of_palindromes.values()))


# use the modulo operator to determine if a number is odd
def is_odd(num):
    return num % 2 != 0


def is_permutation_of_palindrome(string):
    # Use a hash table to count the occurence of each character in a string
    # These are sequential O(c) operations
    character_count_table = {}

    for char in string:
        if char not in character_count_table:
            character_count_table[char] = 0

        character_count_table[char] += 1

    odd_character_count = sum(
        1
        for character_count in character_count_table.values()
        if is_odd(character_count)
    )
    # If only one character has an odd count, this function returns true
    return odd_character_count <= 1


if __name__ == '__main__':
    strings =  ['racecar', 'acerrac', 'aaccerr', 'naa', 'aan', 'todo', 'doto', 'code', 'bob']
    group_permutations_of_palindromes(strings)
