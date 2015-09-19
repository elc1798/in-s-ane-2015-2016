import string
from base64 import b64decode

dec_ciphers = ['rot13', 'b64d', 'caesard']

def rot13(s):
    _rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return string.translate(s, _rot13)

def b64e(s):
    return b64encode(s)

def b64d(s):
    return b64decode(s)

def caesar(plaintext, shift=3):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def caesard(ciphertext, shift=3):
    return caesar(ciphertext, -shift)


#number in front indicates how it was encrypted
#look at number, decrypt, look at new number, decrypt, repeat
def decode(cip):
    while cip[0] in "123":
        cip = globals()[dec_ciphers[int(cip[0]) - 1]](cip[1:])
    return cip

if __name__ == '__main__':
    print decode(open("data").read())
