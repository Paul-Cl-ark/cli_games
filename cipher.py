# Caesar cipher - decrypting a message.
plaintext = input('Enter your cryptogram: ')
cipher = int(input('Enter your cipher between 1 and 25: '))

if cipher < 1 or cipher > 25:
    text = 'You didn\'t enter a ciper between 1 and 25...'
else: 
    text = ''

    for char in plaintext:
        if not char.isalpha():
            text += char
        else: 
            code = ord(char) + cipher
            if char.islower() and code > ord('z') or \
                char.isupper() and code > ord('Z'):
                
                code -= 26
            
            text += chr(code)

print(text)

