#1
# age = int(input("enter your age"))
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")
#2
# num = int(input("enter a number"))
# if num > 0:
#     print("Pozitiv")
# elif num<0:
#     print("Negitiv")
# else:
#     print("Zero")
#3
# is_even = int(input("enter numbr"))
# if is_even %2 == 0:
#     print("is even")
# else:
#     print("is odd")
#4
# num1 = int(input("enter first number"))
# num2 = int(input("enter secend number"))
# if num1 > num2:
#     print(f"{num1} is big")
# elif num1 < num2:
#     print(f"{num2} is big")
# else:
#     print("its equal")
#5
# PASSWORD = "Python123"
# password = input("enter the password")
# if password == PASSWORD:
#     print("Access Granted")
# else:
#     print("Access Denied") 
#6
# num = int(input("enter number"))
# if num >1 and num < 11:
#     print("the number betwwen 1 and 10")
# elif num>10 and num < 51:
#     print("the number betwwen 11 and 50")
# elif num > 51 and num <101:
#     print("the number betwwen 50 - 100")
# else:
#     print("is not in the scope")
#7
# grade = int(input("enter the studant grade"))
# if grade > 89 and grade < 101:
#     print("Excellent")
# elif grade <90 and grade > 79:
#     print("Very Good")
# elif grade < 80 and grade > 69:
#     print("Good")
# elif grade < 70 and grade > 59:
#     print("Passed")
# elif grade < 60 and grade > 0:
#     print("field")
# else:
#     print("its out of scope")
#8
# correct_username = "admin"
# correct_password = "123456"
# username = input("enter user name")
# password = input("enter password")
# if username == correct_username and password == correct_password:
#     print("Login Successful")
# elif username == correct_username and password != correct_password:
#     print("Wrong Password")
# elif username != correct_username:
#     print("Unknown User")
#9
# age = int(input("enter your age"))
# price = int(input("enter the price"))
# if age > 59:
#     print(f"the price is {round(price-(price*20/100),2)}")
# elif age < 19:
#     print(f"the price is {round(price-(price*10/100),2)}")
# else:
#     print(f"not have discount")
#10
# num = int(input("enter a number"))
# if num %3 == 0 and num %5 == 0:
#     print("the number divisible at 3 and at 5")
# elif num %3 == 0 and num %5 != 0:
#     print("the number divisible at 3")
# elif num %5 == 0 and num%3 != 0:
#     print("the number divisible at 5")
# else:
#     print("is not divisible")
#11
# age = int(input("enter your age"))

# if age >17:
#     print("you can enter the club")
# elif age > 15 and age < 18:
#     old_men = input("enter True/False: ")
#     if old_men:
#         print("you can enter")
#     else:
#         print("you cant enter")
# else:
#     print("you cant enter")
#12
# grades_averge = int(input("enter your averge grads"))
# monthly_income = int(input("enter your monthly income"))
# if grades_averge >89:
#     print("you entitled to discount")
# elif grades_averge >84 and grades_averge<90:
#     if monthly_income < 5000:
#         print("you entitled to discount")
#     else:
#         print("you not entitled")
# else:
#     print("you not entitled")
#13
# USERNAME = "pini"
# PASSWORD = "wer87"
# active_acount = True
# username = input("enter user name")
# password = input("enter password")
# acoont = input("enter if acoount is acctive")
# if username == USERNAME and password == PASSWORD and active_acount:
#     print("your acces alow")
# else:
#     print("your acces not alow")
#14
# number = int(input("enter number: "))
#  if 19<number<81:
#      print(True)
# if not(number<19 or number>81):
#     print (True)
# else:
#     print(False)
#15
# balance = 5000
# withdrow = int(input("enter the amount do you want withdrow"))
# if withdrow > 0:
#     if balance > withdrow:
#         balance -= withdrow
#         print(f"the new balance {balance}")
#     else:
#         print("not enough money")
# else:
#     print("the withdroe must be pozitiv")
#16
# age = int(input("enter your age: "))
# card_club = input("enter if you have club card: ")
# if age < 13:
#     if card_club:
#         print("you need pay 22.5")
#     else:
#         print("you need pay 25")
# elif 12<age<18:
#     if card_club:
#         print("you need pay 31.5")        
#     else:
#         print("you need pay 35")
# elif age>17:
#     if card_club:
#         print("you need pay 45 ")
#     else:
#         print("you need pay 50")
#17
# age = int(input("enter your age: "))
# monthly_income = int(input("enter your monthly income"))
# work_yers = int(input("enter your work yers"))
# if age > 21 and monthly_income > 6900 and work_yers > 1:
#     print(True)
# else:
#     print(False)
#18
# type_core = input("enter the type of car: ")
# parking_hours = float(input("enter how much hyers you parking: "))
# if type_core == "motorcycle":
#     if parking_hours < 1:
#         print("you need pay 9 LIS")
#     elif parking_hours > 5:
#         print(f"you need pay {(parking_hours*10)-(parking_hours*10)*15/100}")
#     else:
#         print(f"you need pay {parking_hours*10}")
# elif type_core == "private vehicle":
#     if parking_hours < 1:
#         print("you need pay 18 LIS") 
#     elif parking_hours > 5:
#         print(f"you need pay {(parking_hours*20)-(parking_hours*20)*15/100}")
#     else:
#         print(f"you need pay {parking_hours*20}")
# elif type_core == "commercial vehicle":
#     if parking_hours < 1:
#         print("you need pay 27 LIS")
#     elif parking_hours > 5:
#         print(f"you need pay {(parking_hours*30)-(parking_hours*30)*15/100}")
#     else:
#         print(f"you need pay {parking_hours*30}")
#19
# num1 = int(input("enter first number: "))
# num2 = int(input("enter the secend number"))
# oprator = input("enter oprator + / - / * / /")
# if oprator == "/":
#     if num2 == 0:
#         print("you cant division by zero")
#     print(f"the result is {num1/num2}")
# elif oprator == "*":
#     print(f"result: {num1*num2}")
# elif oprator == "+":
#     print(f"result: {num1+num2}")
# elif oprator == "-":
#     print(f"result: {num1-num2}")
# else:
#     print("enter a avileable oprator")
#20
# year = int(input("enter the year do you whant chek: "))
# if year %400 == 0:
#     print ("leap year")
# elif year %100 == 0:
#     print("not leap year")
# elif year %4 == 0:
#     print("leap year")
# else:
#     print("not leap year")
#21
# basic_wage = 50
# regilur = 182
# total = basic_wage*regilur
# extra = 0
# hour_work = int(input("enter the hours work: "))
# if hour_work < 183:
#     print(f"your monthely wage {total}")
# elif hour_work > 182:
#     extra += hour_work-regilur
#     if extra < 3:
#         print(f"your monthly wage {total+(62.5*extra)}")
#     elif extra > 3:
#         print(f"your monthely hour {total+((extra-2)*75)+(2*62.5)}")

#22
# amount_purchase = int(input("enter the amount purchase: "))
# member_club = input("do you member club: ")
# dayes = int(input("enter the days the pass from purchase: "))
# is_open = input("is not open: ")
# resipt_purchase = input("do you have resipt: ")
# if amount_purchase > 0 and  is_open == True and resipt_purchase == True :
#     if member_club:
#         if dayes < 31:
#             print("you have refound")
#         else:
#             print("you not have refound")
#     else:
#         if dayes < 15:
#             print("you have refound")
#         else:
#             print("you dont have refound")
# else:
#     print("you dont have refound")
    






