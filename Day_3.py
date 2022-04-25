import re
import json
from turtle import title

# validname = '[A-Za-z]'
# validphone = '01[0125][0-9]{8}$'
# validemail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# my_dict = {"Email": [], "password": []}


# def inputfromuser():
#     first_name = input("Enter Your First Name?")
#     while True:

#         if(re.match(validname, first_name)):
#             print("Valid name")

#         else:
#             print("inValid name")
#             first_name = input("Enter Your First Name again?")

#         break
#     last_name = input("Enter Your last Name?")

#     while True:

#         if(re.match(validname, last_name)):
#             print("Valid name")

#         else:
#             print("inValid name")
#             last_name = input("Enter Your last Name again?")

#         break
#     email = str(input("Enter Your Email : "))

#     while True:
#         if(re.match(validemail, email)):
#             print("Valid email")
#             my_dict["Email"].append(email)
#             print(my_dict)
#         else:
#             print("Invalid Email")
#             email = input("Enter Your email again?")
#         break
#     password = (input("Enter Your Password : "))
#     while True:
#         SpecialSym = ['$', '@', '#', '%']
#         # val = True

#         if len(password) < 6:
#             print('length should be at least 6')
#             password = input("Enter Your Password again: ")

#         # val = False

#         if len(password) > 20:
#             print('length should be not be greater than 8')
#             password = input("Enter Your Password again: ")

#         # val = False

#         if not any(char.isdigit() for char in password):
#             print('Password should have at least one numeral')
#             password = input("Enter Your Password again: ")

#         # val = False

#         if not any(char.isupper() for char in password):
#             print('Password should have at least one uppercase letter')
#             password = input("Enter Your Password again: ")

#         # val = False

#         if not any(char.islower() for char in password):
#             print('Password should have at least one lowercase letter')
#             password = input("Enter Your Password again: ")

#         # val = False

#         if not any(char in SpecialSym for char in password):
#             print('Password should have at least one of the symbols $@#')
#             password = input("Enter Your Password again: ")

#         else:
#             my_dict["password"].append(password)
#             print(my_dict)
#             break
#     confirm_Password = (input("Confirm Your Password : "))
#     while True:
#         if confirm_Password == password:
#             print("passwords match ")
#         else:
#             print(" passwords should be matched")
#             confirm_Password = (input("Confirm Your Password : "))
#             print("passwords match ")

#         break
#     mobile_phone = (input("Enter Your Phone Number : "))
#     while True:
#         if(re.match(validphone, mobile_phone)):
#             print("Valid egyption number")

#         else:
#             print("inValid ")
#             mobile_phone = input("Enter Your phone number again?")
#         break


# inputfromuser()


# project_data = {"title": [], "details": [],
#                 "target": [], "start date": [], "end date": []}


# def login():

#     emailll = input("Email: ")

#     pasworddd = input("Password: ")
#     f = open("Day_3.txt", "r")
#     for line in f.readlines():
#         emm, pwd = line.strip().split("|")
#         while (emailll not in emm) and (pasworddd not in pwd):
#             print("Wrong email or password, try again")
#             emailll = input("Email: ")
#             pasworddd = input("Password: ")
#         else:
#             print("Login successful!")
#             break
#     print(f"1-create your own project""2-view your project",
#           "3-update your project", "4-delete your project")

#     numbers = int(input("enter 1 or 2, 3 ,4..."))
#     a = 1
#     b = 2
#     c = 3
#     d = 4
#     validate_start_date = '^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))|^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d+$'
#     validate_end_date = '^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))|^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d+$'

#     if numbers == a:
#         title = input("enter your title")
#         project_data["title"].append(title)
#         print(project_data)
#         Details = input("enter your details")
#         project_data["details"].append(Details)
#         print(project_data)
#         target = int(input("enter your target"))
#         while True:

#             if target < 0 or target > 500000:
#                 print('target should be >0 and < 500,000 , i.e: 250000')
#                 target = input("Enter Your target again: ")

#             else:
#                 print("Valid")
#                 project_data["target"].append(target)
#                 print(project_data)
#             break
#         start_date = input("enter your start date")
#         while True:
#             if(re.match(validate_start_date, start_date)):
#                 print("Valid date")
#                 project_data["start date"].append(start_date)
#                 print(project_data)
#             else:
#                 print("inValid ")
#                 start_date = input("enter your start date")

#             break
#         end_date = input("enter your end date")
#         while True:
#             if(re.match(validate_end_date, end_date)):
#                 print("Valid date")
#                 project_data["end date"].append(end_date)
#                 print(project_data)
#             else:
#                 print("inValid ")
#                 end_date = input("enter your end date")

#             break
#         print("your project created successfully")
#     elif numbers == b:
#         f = open('day_3_project.json')
#         data = json.load(f)
#         for key, value in data.items():
#             print(f"{key} = {value}")
#         f.close()
#     elif numbers == c:
#         a_file = open("day_3_project.json", "r")
#         json_object = json.load(a_file)
#         a_file.close()
#         a_file = open("day_3_project.json", "w")
#         json.dump(json_object, a_file)
#         a_file.close()
#     elif numbers == d:
#         a_file = open("day_3_project.json", "w")
#         a_file.truncate()
#         a_file.close()
#     else:
#         ("enter 1,2,3,4 only")


# login()
