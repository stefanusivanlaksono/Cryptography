import string

letters = string.ascii_lowercase
LETTERS = string.ascii_uppercase

def caesar_cipher(mode, string, k):  
    if mode == 'encoding':
        return encoding(string, k)
    if mode == 'decoding':
        return decoding(string, k)         

def caesar_k(mode, input, output):
    checker  = []
    if mode == 'encoding':
        for i in range(26):
            checker.append(encoding(input, i))
    if mode == 'decoding':
        for i in range(26):
            checker.append(decoding(input, i))
    if checker.index(output):
        return checker.index(output)
    else:
        return False

def encoding(string, k):
    result = ''
    for char in string:
        if char in letters:
            index = (letters.find(char) + k) % 26
            result += letters[index]
        elif char in LETTERS:
            index = (LETTERS.find(char) + k) % 26
            result += LETTERS[index]
        else:
            result += char
    return result

def decoding(string, k):
    result = ''
    for char in string:
        if char in letters:
            index = letters.find(char) - k
            if index < 0:
                index = (index + 26) % 26
            else:
                index = index % 26
            result += letters[index]
        elif char in LETTERS:
            index = LETTERS.find(char) - k
            if index < 0:
                index = (index + 26) % 26
            else:
                index = index % 26
            result += LETTERS[index]
        else:
            result += char
    return result
    

print(f"\n1a. {caesar_cipher('encoding','AMBIDEXTROUS: Able to pick with equal skill a right-hand pocket or a left.',4)}")
print(f"1b. {caesar_cipher('encoding','GUILLOTINE: A machine which makes a Frenchman shrug his shoulders with good reason.',17)}")
print(f"1c. {caesar_cipher('encoding','IMPIETY: Your irreverence toward my deity.',21)}")
print(f"2a. {caesar_cipher('decoding','ZXAI: P RDHIJBT HDBTIXBTH LDGC QN HRDIRWBTCXC PBTGXRP PCS PBTGXRPCH XC HRDIAPCS',15)}")
print(f"2b. {caesar_cipher('decoding','MQTSWXSV: E VMZEP EWTMVERX XS TYFPMGLSRSVW',4)}")
print(f"3.  {caesar_cipher('encoding', 'This is a silly example',0)}")
print(f"4a. {caesar_k('encoding','ROSEBUD','LIMYVOX')}") 
print(f"4b. {caesar_k('encoding','YAMAMOTO','PRDRDFKF')}")   
print(f"4c. {caesar_k('encoding','ASTRONOMY','HZAYVUVTF')}") 
print(f"5.  {caesar_cipher('encoding',caesar_cipher('decoding','UMMSVMAA: Cvkwuuwv xibqmvkm qv xtivvqvo i zmdmvom bpib qa ewzbp epqtm.',8),9)}\n")