import string

letters = list(string.ascii_uppercase)
numbers = list(range(26))
letters_to_numbers = {letter: number for letter, number in zip(letters,numbers)}
numbers_to_letters = {number: letter for letter, number in zip(letters,numbers)}

def caesar_cipher(mode, string, k):
    if mode == 'encoding':
        return caesar_encoding(string, k)
    if mode == 'decoding':
        return caesar_decoding(string, k)

def caesar_encoding(string, k):
    encode = ''
    for char in string.upper():
        if char in letters_to_numbers:
            index = (letters_to_numbers[char] + k) % 26
            encode += numbers_to_letters[index]
        else:
            encode += char
    return encode

def caesar_decoding(string, k):
    decode = ''
    for char in string.upper():
        if char in letters_to_numbers:
            if letters_to_numbers[char] - k < 0:
                index = (letters_to_numbers[char] - k + 26) % 26
            else:
                index = (letters_to_numbers[char] - k) % 26
            decode += numbers_to_letters[index]
        else:
            decode += char
    return decode

def caesar_decoding_k(string):
    decode = ''
    for k in range(26):
        decode += f"k={k}, "
        for char in string.upper():
            if char in letters_to_numbers:
                if letters_to_numbers[char] - k < 0:
                    index = (letters_to_numbers[char] - k + 26) % 26
                else:
                    index = (letters_to_numbers[char] - k) % 26
                decode += numbers_to_letters[index]
            else:
                decode += char
        decode += '\n'
    return decode

print(f"Answer 1a: {caesar_cipher('encoding','AMBIDEXTROUS: Able to pick with equal skill a right-hand pocket or a left.',4)}\n")
print(f"Answer 1b: {caesar_cipher('encoding','GUILLOTINE: A machine which makes a Frenchman shrug his shoulders with good reason.',17)}\n")
print(f"Answer 1c: {caesar_cipher('encoding','IMPIETY: Your irreverence toward my deity.',21)}\n")
print(f"Answer 2a: {caesar_cipher('decoding','ZXAI: P RDHIJBT HDBTIXBTH LDGC QN HRDIRWBTCXC PBTGXRP PCS PBTGXRPCH XC HRDIAPCS',15)}\n")
print(f"Answer 2b: {caesar_cipher('decoding','MQTSWXSV: E VMZEP EWTMVERX XS TYFPMGLSRSVW',4)}\n")
print(f"Answer 3 : {caesar_cipher('encoding', 'This is a silly example',0)}\n")
print(f"Answer 4a: \n{caesar_decoding_k('LIMYVOX')}")     # Answer 20
print(f"Answer 4b: \n{caesar_decoding_k('PRDRDFKF')}")    # Answer 17
print(f"Answer 4c: \n{caesar_decoding_k('HZAYVUVTF')}")   # Answer  7
print(f"Answer 5 : {caesar_cipher('encoding',caesar_cipher('decoding','UMMSVMAA: Cvkwuuwv xibqmvkm qv xtivvqvo i zmdmvom bpib qa ewzbp epqtm.',8),9)}")