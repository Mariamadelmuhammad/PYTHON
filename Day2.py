# import re
# 1
# def arr(start, length):

#     array = list(range(start, start+length))
#     print(array)


# arr(1, 15)


# ************************************************

# 2
# num = int(input("Enter number:"))


# def numberr(num):

#     if num % 5 == 0 and num % 3 == 0:
#         print('fizzbuzz')

#     elif num % 5 == 0:
#         print("buzz")
#     elif num % 3 == 0:
#         print('fizz')


# numberr(num)
# ******************************************************************
# 3
# fullname = str(input("enter your fullname"))
# x = fullname


# def reversefun(x):
#     return x[::-1]


# txt = reversefun(x)

# print(txt)

# ******************************************************************

# 4
# name = input("Enter your name: ")
# validname = '[A-Za-z]'


# def inputfromuser():
#     name = input("Enter Your First Name?")
#     while True:

#         if(re.match(validname, name)):
#             print("Valid name")

#         else:
#             print("inValid name")
#             name = input("Enter Your First Name again?")
#         break


# inputfromuser()
# ******************************************************************

# 5
# word = input("enter your word")
# maxLen = 0
# current = word[0]
# longest = word[0]


# for i in range(len(word) - 1):
#     if word[i + 1] >= word[i]:
#         current += word[i + 1]

#         if len(current) > maxLen:
#             maxLen = len(current)
#             longest = current
#     else:
#         current = word[i + 1]

#     i += 1

# print("Longest substring in alphabetical order is: " + longest)
# ******************************************************************

# 6


# list = []


# def Average(list):
#     return sum(list)


# average = Average(list)


# i = 1
# while i < 10:

#     a = input("Please enter your number")
#     if a.isdigit():
#         list.append(a)
#     i += 1
#     # print(list)

#     if a == "done":
#         print(list)
#         print(len(list))
#         mylist = list
#         avg = sum(mylist)/len(mylist)
#         print("The average is ", round(avg, 2))


#     elif a.isalpha():
#         print("error, please enter numbers only")


# ******************************************************************
# 7


# import random


# name = input("Enter your name? ")


# print("HELLO ! ", name)

# words = ['react', 'html', 'php', 'programming',
#          'python', 'database', 'css', 'nginx',
#          'linux', 'bash', 'es6', 'apache']


# word = random.choice(words)


# print("Guess the characters")

# guesses = ''


# turns = 7


# while turns > 0:

#     failed = 0

#     for charachter in word:

#         if charachter in guesses:
#             print(charachter)

#         else:
#             print("_")

#             failed += 1

#     if failed == 0:

#         print("You Win")

#         print("The word is: ", word)
#         break

#     guess = input("guess a character:")

#     guesses += guess

#     if guess not in word:

#         turns -= 1

#         print("Wrong")

#         print("You have", + turns, 'more guesses')

#         if turns == 0:
#             print("You Lost")

# ******************************************************************
