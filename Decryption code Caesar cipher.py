#Ciphertext decryption code
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - shift % 26) + ord('a')))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


def caesar_frequency_analysis(ciphertext):
    #calculate the frequencies of letter in the ciphertext
    letter_frequency = {}
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            if char in letter_frequency:
                letter_frequency[char] += 1
            else:
                letter_frequency[char] = 1
    
    #Find the most common letter in English (usually 'e')
    most_common_letter = max(letter_frequency, key = letter_frequency.get)

    #Calculate the shift needed to decrypt
    shift = (ord(most_common_letter) - ord('e')) % 26

    #Decrypt the ciphertext using the calculated shift

    return decrypted_text

#Example usage:
ciphertext = "LU DZNUAMNDODJUDTUZDGYQDLU DGOJDCKDTKKJDOZ"
decrypted_text = caesar_frequency_analysis(ciphertext)
print(decrypted_text)
