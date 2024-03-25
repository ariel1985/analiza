# Example for Variables in Python

# name_of_variable = value

# boolean (True or False)
bit = True
print('bit:', bit)

# int
num = 10
print('num:', num)

# float (fractional number)
decimal = 3.14159
print('decimal:', decimal)

# empty value
empty = ''

# char
char = 'a'
print('char:', char)

# string (group of chars)
word = 'Hello, World!'
print('word:', word)

# array
arrInts = [12, 78822, 35, 47, 412125555]
arrFloats = [1.1, 2.2, 3.3, 4.4, 5.5]
arrChars = ['a', 'b', 'c', 'd', 'e']
arrStrings = ['one', 'two', 'three', 'four', 'five']
arrMixed = [-19, 2.2, 'c', 'four', 5.5]

# empty array
arrEmpty = []

# define array
arrWeekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  # 0-based index

# print array
print('arrWeekdays:', arrWeekdays)

# select value in array by index
print('arrWeekdays[0]:', arrWeekdays[0])
print('Thursday:', arrWeekdays[3])
print(arrWeekdays[-1]) # only in Python
# print(arrWeekdays[20]) # Error

# edit value in array by index
arrWeekdays[3] = "Thor's Day"
print('arrWeekdays:', arrWeekdays)

def search_char_in_string(char, string):
    if char in string:
        print('char is in string')
    else:
        print('char is not in string')
        
search_char_in_string('a', 'Hello, World!')

search_char_in_string('z', 'Hello, World!')

search_char_in_string('z', 'World War z')


print( len('Hello, World!') )
