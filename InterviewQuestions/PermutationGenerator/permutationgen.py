def generate_permutation(string):
    # Solution
    if len(string) <= 1:
        return [string]
    # recursive case
    permutations_array = []
    for i in range(len(string)):
        front_char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        remaining_permutations = generate_permutation(remaining_chars)
        for permutation in remaining_permutations:
            permutations_array.append(front_char + permutation)
    return permutations_array

print(generate_permutation("ben"))