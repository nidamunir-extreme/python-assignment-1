def vowel_counter(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

print(vowel_counter("Hello, world!"))  