def anagrams(str1, str2):
    # Remove spaces and convert to lowercase for uniformity
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted characters match
    return sorted(str1) == sorted(str2)

# Get user input
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Check if they are anagrams
if anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")