def ubah_huruf(sentence):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted_alphabet = 'KLMNOPQRSTUVWXYZABCDEFGHIJ'
    result = ''

    for char in sentence:
        if char.isalpha():
            if char.isupper():
                index = alphabet.index(char)
                encrypted_char = shifted_alphabet[index]
                result += encrypted_char
            else:
                # Handle lowercase characters
                index = alphabet.index(char.upper())
                encrypted_char = shifted_alphabet[index].lower()
                result += encrypted_char
        else:
            # Handle non-alphabet characters
            result += char

    return result

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB