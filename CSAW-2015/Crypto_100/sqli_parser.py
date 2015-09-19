import string

key_file = open("substitution" , 'r')
original = key_file.readline().strip()
converted = key_file.readline().strip()
key_file.close()

assert(len(original) == len(converted))
assert(len(original) == 26)

def indexInOriginal(char):
    for i in range(0, len(original)):
        if char == original[i]:
            return i
    return -1

def convert(string):
    string_builder = ""
    for c in string.upper():
        index = indexInOriginal(c)
        string_builder += c if index == -1 else converted[index]
    return string_builder

user_in = str(raw_input("input >> "))
while user_in != "exit":
    print("output >> " + convert(user_in))
    user_in = str(raw_input("input >> "))
