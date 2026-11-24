#תרגיל1
# numbers = [20,30,40,50,60]
# print(numbers,numbers[0],numbers[-1],numbers[2])

#תרגיל 2
# studants = ["pini","avi","kobi","hrel","dani"]
# print(studants[0],studants[-1])
# studants[1]="ariel"
# print(studants)

#תרגיל 3
# grads = [89,67,89,90,100]
# grads.append(99)
# grads.insert(0,78)
# print(grads)

#תרגיל 4
# numbers = [23,45,67,89,12,23,34,45,56]
# numbers.pop(0)
# print(numbers)
# numbers.pop(2)
# print(numbers)

#תרגיל 5
# product = ["laptop","computer","bluthoh"]
# print("laptop" in product)
# print("fd" in product)

#תרגיל 6
# numbers = [1,2,3,4,5,67,8,9,10]
# for number in numbers:
#     print (number)

#תרגיל 7
# numbers = [1,2,3,4,5,67,8,9,10]
# for number in numbers:
#     if number %2 == 0:
#         print(number)

#תרגיל 8
# grads = [100,29,38,47,59,67,89,9,10]
# total = 0
# for grade in grads:
#     total += grade
# print(total)

#תרגיל 9
# numbers = [13,56,78,99,123,654,345]
# big_number = numbers[0]
# for number in numbers:
#     if number > big_number:
#         big_number = number
# print(big_number)

#תרגיל 10
# names = ["avi","nama","bibi","noa","eyal"]
# name_choice = input("enter name: ")
# for name in names:
#     if name == name_choice:
#         print("Found")
#         break
#     else:
#         print("Not found")
#         break

#תרגיל 11
# numbers = [45,67,89,9,0,5,6,124,67,67]
# num = int(input("enter number you looking for: "))
# index = []
# for i,number in enumerate(numbers):
#     if number == num:
#          index.append(i)
# print(index)

#תרגיל 12
# numbers = [15,748,54,78,2,5,98]
# big_50 = 0
# for num in numbers:
#     if num > 50:
#         big_50 += 1
# print(big_50)

#תרגיל 13
# numbers = [23,45,67,78,98,90,15,58,97]
# even_numbers = []
# for num in numbers:
#     if num %2 == 0:
#         even_numbers.append(num)
# print(even_numbers)

#תרגיל 14
# names = ["dani","eli","michal","dana"]
# len_names = len(names)
# index = 0
# while index < len_names:
#     print(index,names[index])
#     index += 1

#תרגיל 15
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[3:6])
# print(numbers[::-1])

#תרגיל16
# names = ["pini","kpbi","avi","eli","dana","dani","hrel"]
# for i, name in enumerate(names):
#     if i%2 == 0:
#         print(name,end=' ')
# for i, name in enumerate(names):
#     if i%2 != 0:
#         print(name,end=" ")
# print(names[::-3])

#תרגיל 17
# numbers = [1,2,3,4,5,6,7,8,9,1,0,11,12,13,14,15,16,17,18,19,20]
# start_list= numbers[0:9]
# end_list= numbers[-10:]
# print(numbers[5:14])
# print(start_list)
# print(end_list)
    
#תרגיל 18
# listi = [1,2,3,4,5,6]
# new_listi = listi[0:3]     
# print(new_listi) 

#תרגיל 19
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num_1 =[num *2 for num in numbers] 
# num2 = [num**2 for num in numbers]
# num3 = [num if num %2 == 0 else "odd" for num in numbers]
# num4 = [num for num in numbers if num > 5]
# num5 = [num*2 if num %2 == 0 else num for num in numbers]

#תרגיל 20
# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# pass_grade = [grade for grade in grades if grade > 59]
# field_grade = [grade for grade in grades if grade < 60]
# add_5 = [grade + 5 for grade in grades]

#תרגיל 21
# names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi","Dniel"]
# big_4 = [name for name in names if len(name) > 4]
# big_letters = [name.upper() for name in names]
# start_D = [name for name in names if name.startswith("D")]

#תרגיל 22
# numbers = [12, 7, 25, 30, 9, 44, 18, 3]
# new_list = [num for num in numbers if (num%3 == 0) and (num > 10)]

#תרגיל 23
# listi = []
# for i in range(10):
#     num = int(input("Enter number: "))
#     listi.append(num)
# print(listi)
# max_num = listi[0]
# for num in listi:
#     if num > max_num:
#         max_num = num
# print(max_num)
# min_num = listi[0]
# for num in listi:
#     if num < min_num:
#         min_num = num
# print(min_num)
# print(sum(listi)/len(listi))

#תרגיל 24
# names = ["pini","kobi","michal","dana"]
# name = input("Enter name: ")
# if name in names:
#     names.remove(name)
# else:
#     print("This name not in the list")
# print(names)

#תרגיל 25
# numbers_list = [15,78,14,18,78,98,45,12,129,1458,1249,2458]
# even_num = [num for num in numbers_list if num %2 == 0]
# odd_num = [num for num in numbers_list if num %2 != 0]
# big_20 = [num for num in numbers_list if num > 20]

#תרגיל 26
# num_list = [15,78,14,18,78,98,45,12,14,129,1458,1249,14,2458]
# num = int(input("Enter number: "))
# counter =0
# index = []
# for i,n in enumerate(num_list):
#     if n == num:
#         index.append(i)
# if index:
#     print(index)
#     print(len(index))
# else:
#     print("the number not in the list")

#תרגיל 27
# list1 = [12,768,345,765]
# list2 = [243,57,987,567]
# list3 = list1+list2
# print(list3[0:3])
# print(list3[-3:])
# print(list3[::-1])

#תרגיל 28
# listi = [34,67,89,99,79,67,89,90]
# num = int(input("Enter number: "))
# flag = True
# for n in listi:
#     if n == num:
#         print("This number exisit")
#         flag = False
#         break
# if flag:
#     listi.append(num)
# print(listi)

#פרוייקט ניהול ציונים
# grades = [90,85, 72, 90, 55, 100, 63, 48, 77,90]
# runing = True
# while runing:
#    print("===== Grades Management =====")
#    print("1. Show all grades")
#    print("2. Add a grade")
#    print("3. Search for a grade")
#    print("4. Remove a grade")
#    print("5. Show passing grades")
#    print("6. Show failing grades")
#    print("7. Show highest and lowest grade")
#    print("8. Show average grade")
#    print("9. Show first 3 grades")
#    print("10. Show grades in reverse")
#    print("0. Exit")
#    choice = input("Choice: ")
#    if choice == "1":
#       for grade in grades:
#          print(grade)
#    if choice == "2":
#       grade = int(input("Enter grade: "))
#       grades.append(grade)
#    if choice == "3":
#       search = int(input("Enter search grade: "))
#       indexes = []
#       for i,g in enumerate(grades):
#          if g == search:
#             indexes.append(i)
#       print(f"INDEXES: {indexes}")
#    if choice == "4":
#       remove_num = int(input("Enter remove number: "))
#       if remove_num not in grades:
#          print("You cant remove number not exists")
#       grades.remove(remove_num)
#    if choice == "5":
#       passing = [grade for grade in grades if grade > 59]
#       print(passing)
#    if choice == "6":
#       field = [grade for grade in grades if grade < 60] 
#       print(field)
#    if choice == "7":
#       max_num = grades[0]
#       min_num = grades[0]
#       for n in grades:
#          if n > max_num:
#             max_num = n
#       for g in grades:
#          if g < min_num:
#             min_num = g
#       print(f"Max grade: {max_num}'\n',Min grads: {min_num}")
#    if choice == "8":
#       if len(grades) == 0:
#          print("You cant division by zero")
#          continue
#       print(f"Averge grades: {sum(grades)/len(grades)}")
#    if choice == "9":
#       print(grades[0:3])
#    if choice == "10":
#       print(grades[::-1])
#    if choice == "11":
#       runing = False
    







