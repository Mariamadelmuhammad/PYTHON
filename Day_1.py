# 1 (done)

# str = input("enter a word containing vowels")


# def countv(str):

#     count = 0

#     vowel = set("aeiouAEIOU")

#     for alphabet in str:

#         if alphabet in vowel:
#             count = count + 1

#     print("Number of vowels is :", count)


# countv(str)


# 2
# subject = ["html", "css", "react", "apache", "linux"]
# print(subject)

# subject.sort()
# print(subject)

# subject.sort(reverse=True)
# print(subject)

# 3
# inst = "Information iti Technology iti Institute iti"
# print(inst.count('iti'))

# ************************
#4 (done)

# string = input("enter sentence")


# def removev(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     result = [letter for letter in string if letter.lower() not in vowels]
#     result = ''.join(result)
#     print(result)


# removev(string)


# 5 (done)
# word = input("enter a word containing i")
# print(word.count("i"))


# 6
# number = input("please enter a number ")
# if number.isdigit():
#     number = int(number)

# for i in range(1, 11):

#     print(number, 'x', i, '=', number*i)


# 7

# def pypart(n):

#     for i in range(0, n):

#         for j in range(0, i+1):

#             print("* ", end="")

#         print("\r")


# n = 5
# pypart(n)
