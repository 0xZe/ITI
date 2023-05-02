def longest_substring(string):
    longest = ''
    current = ''
    for character in string:
        if current == '' or character >= current[-1]:
            current += character
        else:
            current = character
        longest = max(current, longest, key=len)
    print("Longest substring in alphabetical order is:" ,longest)

longest_substring(input("Enter the string: "))