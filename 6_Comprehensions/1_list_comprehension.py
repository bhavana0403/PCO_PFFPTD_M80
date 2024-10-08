# List comprehension
"""
Syntax:
        Var = [val_to_be_appended for_loop]
        Var = [val_to_be_appended  for_loop  if <cond>]
        Var = [true_value if <cond> else false_value  for_loop]
"""

st = 'hello world'
print(list(st))     # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

res = []
for ch in st:
    res.append(ch)
print(res)      # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

res = [ch for ch in st]
print(res)      # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']


# create a list of square of a numbers from 1 to 10
res = []
for i in range(1, 11):
    res.append(i**2)
print(res)      # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

_res = [i**2 for i in range(1, 11)]
print(_res)     # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

###########################################################################################

sentence = 'good morning everyone'
# o/p = [('good', 4), ('morning', 7), ('everyone', 8)]
res = []
for word in sentence.split():
    res.append((word, len(word)))
print(res)      # [('good', 4), ('morning', 7), ('everyone', 8)]

_res = [(word, len(word)) for word in sentence.split()]
print(_res)     # [('good', 4), ('morning', 7), ('everyone', 8)]

###########################################################################################

# WAP to extract all the even numbers from given list

li = [8, 2, 45, 23, 21, 88, 67, 98, 12, 56]
res = []
for num in li:
    if num % 2 == 0:
        res.append(num)
print(res)      # [8, 2, 88, 98, 12, 56]

_res = [num for num in li if num % 2 == 0]
print(_res)     # [8, 2, 88, 98, 12, 56]

##########################################################################################

# WAP to extract all the vowels in a given string

st = 'hello everyone'
res = []
for ch in st:
    if ch in 'aeiouAEIOU':
        res.append(ch)
print(res)      # ['e', 'o', 'e', 'e', 'o', 'e']

_res = [ch for ch in st if ch in 'aeiouAEIOU']
print(_res)     # ['e', 'o', 'e', 'e', 'o', 'e']
print(''.join(_res))    # eoeeoe

#########################################################################################

# WAP to extract all the words starting with 'a' in the given sentence

sentence = "a anagram rolex alex paul daniel"
_res = [word for word in sentence.split() if word.startswith('a')]
print(_res)     # ['a', 'anagram', 'alex']

###########################################################################################

# WAP to extract all the words starting with 'a' or 'A' in the given sentence
sentence = "a anagram rolex Alex paul daniel"
_res = [word for word in sentence.split() if word.startswith('a') or word.startswith('A')]
print(_res)     # ['a', 'anagram', 'Alex']

sentence = "a anagram rolex Alex paul daniel"
_res = [word for word in sentence.split() if word[0] in 'Aa']
print(_res)     # ['a', 'anagram', 'Alex']

#############################################################################################

# WAP to extract all the odd numbers in the range 1 to 50
odds = [num for num in range(1, 51) if num % 2 == 1]
print(odds)

_odds = [num for num in range(1, 51) if num % 2]
print(_odds)

#########################################################################################

# WAP to separate first and last names from full names

names = ['steve jobs', 'bill gates', 'michael jackson', 'abraham lincoln', 'mukesh ambani']
first_name = [name.split()[0] for name in names]
last_name = [name.split()[1] for name in names]
print(first_name)   # ['steve', 'bill', 'michael', 'abraham', 'mukesh']
print(last_name)    # ['jobs', 'gates', 'jackson', 'lincoln', 'ambani']

# WAP to extract all the words which has even length

st = 'python science data manual webtech'
res = [word for word in st.split() if len(word) % 2 == 0]
print(res)      # ['python', 'data', 'manual']

# WAP to create a list of numbers from 1 to 10 along with it's factorial

from math import factorial
print(factorial(5))     # 120

res = [(i, factorial(i)) for i in range(1, 11)]
print(res)

#########################################################################################

# WAP to create a list of numbers from 1 to 10 along with its cube if the number is odd, along with square if the number is even
# o/p = [(1, 1), (2, 4), (3, 27), (4, 16), ........(9, 729),(10, 100)]

res = [(i, i**3) if i % 2 !=0 else (i, i**2) for i in range(1, 11)]
print(res)      # [(1, 1), (2, 4), (3, 27), (4, 16), (5, 125), (6, 36), (7, 343), (8, 64), (9, 729), (10, 100)]

# reverse the string if the length is even else keep it as it is
li = ['python', 'science', 'data', 'manual', 'web']
res = [st[::-1] if len(st) % 2 == 0 else st for st in li]
print(res)      # ['nohtyp', 'science', 'atad', 'launam', 'web']

#########################################################################################

# WAP to filter all the languages starting with 'p' or 'P'
languages = ['python', 'php', 'java', 'Pearl', 'C']
res1 = [language for language in languages if language.startswith('p') or language.startswith('P')]
res2 = [language for language in languages if language[0] in 'pP']
res3 = [language for language in languages if language[0].lower() == 'p']
print(res1, res2, res3, sep='\n')
"""
['python', 'php', 'Pearl']
['python', 'php', 'Pearl']
['python', 'php', 'Pearl']
"""

# WAP to extract the string which has length less than 6

words = ['a', 'alex', 'anthony', 'apple', 'alexander', 'abraham', 'michael']
res = [word for word in words if len(word) < 6]
print(res)  # ['a', 'alex', 'apple']

########################################################################################




