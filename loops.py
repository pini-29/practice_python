#1
# count = 0
# while count < 10:
#     count += 1
#     print(count)
#2
# count = 10
# while count > 0:
#     print(count)
#     count -= 1
# print("START! ")
#3
# counter = 0
# while counter < 50:
#     if counter %2 == 0:
#         print(counter)
#         counter += 1
#     else:
#         counter+=1
#         continue
#4
# num = int(input("enter number: "))
# index = 1
# while index < 6:
#     print(num*index)
#     index+=1

#5
# counter = 100
# total = 0
# while counter > 0:
#     total += counter
#     counter -= 1
# print(total)

#תרגיל6 
# PASSWORD = "python123"
# flag = True
# while flag:
#   password = input("enter password: ")
#   if password == PASSWORD:
#     print("Wlcome! ")
#     flag = False

# תרגיל7
# secret_number = 27
# flag = True
# while flag:
#     guass = int(input("guass the secret number"))
#     if guass == secret_number:
#         print("You guass!")
#         flag = False

#תרגיל8
# flag = True
# total = 0
# while flag:
#     num = int(input("enter a number"))
#     if num == 0:
#         flag = False
#         print(total)
#     total += num

#תרגיל 9
# total = 0
# flag = True
# counter = 0
# while flag:
#     num = int(input("enter a number: ")) 
#     if num == 999:
#         flag = False
#         print("Exit")
#     total += num
#     counter += 1
# print(total,counter,total/counter)

#תרגיל 10
# total = 0
# counter = 0
# flag = True
# while flag:
#     num = int(input("enter a number: "))
#     if num < 0:
#         flag = False
#         print("Exit")
#     total += num
#     counter += 1
# print(total,counter)

#תרגיל 11
# counter = 10
# num = 1
# number = int(input("Enter number: "))
# while counter >0:
#     counter -= 1
#     print(number*num)
#     num += 1

#תרגיל 12
# num = int(input("Enter number: "))
# counter = 0
# while num > 0:
#     num = num // 10
#     counter += 1
# print(counter)

#תרגיל13
# num1 = int(input("Enter number: "))
# print(f"Input: {num1} ")
# flag = True
# reverse = 0
# while num1 > 0:
#     temp =  num1%10
#     num1 = num1//10
#     reverse = reverse*10
#     reverse += temp
# print(f"Output: {reverse}")

#תרגיל 14
# number = int(input("Enter number: "))
# index = 2
# flag = True
# while index < number:
#     if number %index == 0:
#         print("This number is not prime")
#         break
#     index += 1

#תרגיל 15
# balance = 5000
# flag = True
# while flag:
#     print("1. Cheak balance.")
#     print("2. Deposit money.")
#     print("3. Withdrow money")
#     print("4. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         print(balance)
#         continue
#     if choice == "2":
#         deposit = int(input("Enter deposit: "))
#         if deposit < 0:
#             print("must be pozitiv")
#             continue
#         balance += deposit
#         print(f"new balance {balance}")
#     if choice == "3":
#         withdrow = int(input("Enter withdrow"))
#         if withdrow < 0:
#             print("its must be pozitiv")
#             continue
#         balance -= withdrow
#         print(f"new balance {balance}")
#     if choice == "4":
#         flag = False

#תרגיל 16
# counter = 0
# while True:
#     print(counter)
#     counter += 1
#     if counter == 15:
#         break

#תרגיל 17
# counter = 1
# while counter < 31:
#     if counter %3 == 0:
#         counter += 1
#         continue
#     print(counter)
#     counter+= 1

#תרגיל 18
# while True:
#     num = int(input("enter number: "))
#     if num == 100:
#         break

#תרגיל 19
# for i in range(10):
#     print(i)

#תרגיל 20
# for i in range(0,100,5):
#     print(i)

#תרגיל 21
# total = 0
# for i in range(101):
#     total += i
# print(total)

#תרגיל 22
# number = int(input("enter number: "))
# for i in range(1,11):
#     print(number*i)

#תרגיל 23
# num1 = int(input("enter number"))
# num2 = int(input("enter number"))
# result = 0
# for i in range(num1,num2+1):
#     result += i
# print(f"Start: {num1}")
# print(f"End: {num2}")
# print(f"Result: {result}")

#תרגיל 24
# for i in range(1,100):
#     if i %3 == 0 and i%5 == 0:
#         print(i)

#תרגיל 25
# rows = int(input("enter num of rows"))
# coulem = int(input("enter num of coulem"))
# for i in range(rows):
#     print("*"*coulem)

#תרגיל 26
# for i in range(6):
#     print ("*"*i)

#תרגיל 27
# for i in range(1,11):
#     for j in range(1,11):
#         print (str(i*j).ljust(2),end=" ")
#     print()

#תרגיל 28
# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i},{j}")

#פרוייקט: טריוויה
# runing = True
# while runing:
#     print("===== MATH GAME =====")
#     print("1. Start Game")
#     print("2. View Instructions")
#     print("3. Exit")
#     choice = input("Choose:")
#     if choice == "1":
#         counter = 0
#         quastions = [("4*20=",80),("26/2=",13),("100+98=",198),("100/4=",25)]
#         for q in quastions:
#             num = int(input(q[0]))
#             if num == q[1]:
#                 counter += 1
#     if choice == "2":
#         print(f"You have {counter} points")
#     if choice == "3":
#         runing = False        



    
      
    
