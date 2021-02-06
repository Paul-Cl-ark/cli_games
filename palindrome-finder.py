text = input('Enter your text... ')
stripped = text.replace(' ', '').lower()

ignore_middle_character = len(stripped) % 2
middle = len(stripped) // 2

start = stripped[:middle]
end = stripped[middle + ignore_middle_character:][::-1]

palindrome = start == end

print('It is a palindrome') if palindrome else print('It\'s not a palindrome')
