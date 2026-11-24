#תרגיל 1
# def say_hello():
#     print("Hello world")

#תרגיל 2
# def show_welcome():
#     print("Welcome to system")

#תרגיל 3
# def show_menu():
#     print("===== Main Menu =====")
#     print("1. Start")
#     print("2. Settings")
#     print("3. Exit")

#תרגיל 4
# def show_number():
#     for i in range(10):
#         print(i)

#תרגיל 5
# def show_even_numbers():
#     for i in range(1,100):
#         if i %2 == 0:
#             print(i)

#תרגיל 6
# def show_stars():
#     print("*"*10)

#תרגיל 7
# def greet(name):
#     print(f"Hello {name}")

#תרגיל 8
# def show_age(age):
#     print(f"you are {age} old")

#תרגיל 9
# def calculate_sum(num1,num2):
#     print(num1+num2)

#תרגיל 10
# def calculate_average(num1,num2,num3):
#     total = num2+num1+num3
#     print(round(total/3,2))

#תרגיל 11
# def check_even(number):
#     if number %2 == 0:
#         print("is even")
#     else:
#         print("is odd")

#תרגיל 12
# def check_password(password):
#     curent_password = "123456"
#     if password == curent_password:
#         print("Access Granted")
#     else:
#         print(" Access Denied")

#תרגיל 13
# def calculate_discount(price,precent):
#     discount = (price*precent)/100
#     print(price-discount)

#תרגיל 14
# def show_range(num1,num2):
#     for i in range(num1,num2+1):
#         print(i)

#תרגיל 15
# def print_rectangle(hight,wight):
#     for i in range(hight):
#         print("*"*wight)

#תרגיל 16
# def multiply(num1,num2):
#     return num2*num1

#תרגיל 17
# def get_full_name(firstname,lastname):
#     return firstname + lastname

#תרגיל 18
# def get_max(num1,num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

#תרגיל 19
# def is_positive(num):
#     if num > -1:
#         return True
#     else:
#         return False

#תרגיל 20
# def calculate_tax(price,precent_vat):
#     vat = (price*precent_vat)/100
#     return price+vat

#תרגיל 21
# def get_grade_status(grade):
#     if 89 < grade<101:
#         return "Excellent"
#     elif  74 < grade < 90:
#         return "Good"
#     elif 59 < grade < 75:
#         return "Averge"
#     else:
#         return "Field"

#תרגיל 22
# def count_digits(number):
#     stri = str(number)
#     return len(stri)

#תרגיל 23
# def calculate_power(num1,power):
#     number = 1
#     for i in range(power):
#         number *= num1
#     return number

#תרגיל 24
# def print_list(listi):
#     for i in listi:
#         print(i)

#תרגיל 25
# def get_list_sum(listi):
#     total = 0
#     for l in listi:
#         total += l
#     print(total)

#תרגיל 26
# def get_list_average(listi):
#     if len(listi) == 0:
#         print("zerodivitionerror")
#     else:
#         print(sum(listi)/len(listi))

#תרגיל 27
# def find_number(listi,num):
#     counter = 0
#     for i in listi:
#         if i == num:
#             counter += 1
#     if counter > 0:
#         print(True)
#     else:
#         print(False)


#תרגיל 28
# def find_max(listi):
#     max_num = 0
#     for l in listi:
#         if l > max_num:
#             max_num = l
#     print(max_num)

#תרגיל 29
# def get_even_number(listi):
#     even_numbers = [num for num in listi if num%2 == 0]
#     print(even_numbers)

#תרגיל 30
# def get_long_names(listi):
#     names = [name for name in listi if len(name) > 3]
#     print(names)

#תרגיל 31
# def reverse_list(listi):
#     print(listi[::-1])

#תרגיל 32
# def count_occurrences(listi):
#     new_listi = []
#     for i in listi:
#         new_listi.append(listi.count(i))
#     print(new_listi)

#תרגיל 33
# def remove_duplicates(listi):
#     new_listi = []
#     for i in listi:
#         if i not in new_listi:
#             new_listi.append(i)
#     print(new_listi)

# תרגיל 34
# def calculate_final_price(price,precent):
#     discount = (price*precent)/100
#     total = price-discount
#     if total > 499:
#         discount = (total*5)/100
#         total -= discount
#     print(f"the price is {total}")

#תרגיל 35
# def check_list(listi):
#     counter_even = 0
#     counter_odd = 0
#     counter_sum = 0
#     for num in listi:
#         counter_sum += num
#         if num %2 == 0:
#             counter_even += 1
#           e ףlse::
#             counter_odd += 1
#     print(f"even numbers: {counter_even}. odd numbers: {counter_odd}. sum: {counter_sum}")

#תרגיל 36
# def analyze_grades(listi):
#     min_num = min(listi)
#     max_listi = max(listi)
#     averge = sum(listi)/len(listi)
#     print(f"min: {min_num}. max: {max_listi}.averge {averge}")

#תרגיל 37
# def validate_user(username,password):
#     if username and len(password) >= 6:
#         print(True)
#     else:
#         print(False)

#תרגיל 38
# students = [    {"name": "David", "grade": 90},    {"name": "Moshe", "grade": 75},    {"name": "Dana", "grade": 100}]
# def search_students(listi,studant):
#     for s in listi:
#         if s["name"] == studant:
#             return s
#     return None

#תרגיל 39
# cart = [    {"name": "Laptop", "price": 4500, "quantity": 1},    {"name": "Mouse", "price": 80, "quantity": 2},    {"name": "Keyboard", "price": 150, "quantity": 1}]
# def calculate_cart_total(carti):
#     total = 0
#     for c in carti:
#         total += c["price"]*c["quantity"]
#     return total

#תרגיל 40
# def get_fibonacci(number):
#     listi = []
#     a, b = 0, 1 
#     for i in range(number):
#         listi.append(a)
#         a, b = b, a+b
#     print(listi)
# get_fibonacci(7)

#תרגיל 41
# name = "David"
# def show_name():	
#     name = "Moshe"
#     print(name)
# show_name()
# print(name)

#תרגיל 42
# counter = 10
# def increase():
#     counter = 20
#     print(counter)
# increase()
# print(counter)

#תרגיל 43
# def add_ten(number):
#     return number+10
# num = 10
# print(add_ten(num))
# print(num)

#תרגיל 44
# numbers = [12,13,14,15]
# def add_number(listi):
#     listi.append(30)
#     print(numbers)
# add_number(numbers)
# print(numbers)

#תרגיל 45
# listi = [12,23,4,56]
# def add_to_list(lis):
#     new_list=lis[::-1]
#     new_list.append(30)
#     print(new_list)
#     print(lis)
# add_to_list(listi)

#מערכת ניהול תלמידים 
# students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
# def show_menu():
#     print("===== Student Management =====")
#     print("1. Show all students")
#     print("2. Add student")
#     print("3. Search student")
#     print("4. Update student grade")
#     print("5. Remove student")
#     print("6. Show passing students")
#     print("7. Show class statistics")
#     print("8. Show students above average")
#     print("0. Exit")
# def show_students(students):
#     for studant in students:
#         print(studant)
# def add_student(students):
#     new_studant = {"name":None,"age":0,"grade":0}
#     new_studant["name"] = input("Enter studant name: ")
#     new_studant["age"] = input("Enter age: ")
#     new_studant["grade"] = input("Enter grade: ")
#     students.append(new_studant)
# def search_student(students, name):
#     for studant in students:
#         if studant["name"] == name:
#             return studant
#     return None
# def update_grade(students, name, grade):
#     studant = search_student(students,name)
#     if studant:
#         studant["grade"] = grade
#     else:
#         print("the studant not exists")

# def remove_student(students, name):
#     studant = search_student(students,name)
#     if studant:
#         students.remove(studant)
#     else:
#         print("the studant not exusts")
# def get_passing_students(students):
#     pass_studants = []
#     for studant in students:
#         if studant["grade"] > 59:
#             pass_studants.append(studant["name"])
#     return pass_studants
# def get_average(students):
#     total = 0
#     for studant in students:
#         total += studant["grade"]
#     return total/len(students)
# def above_average(students):
#     average = get_average(students)
#     studants_above = []
#     for studant in students:
#         if studant["grade"] > average:
#             studants_above.append(studant["name"])
#     return studants_above
# def get_highest_grade(students):
#     max_grade = 0
#     for studant in students:
#         if studant["grade"] > max_grade:
#             max_grade = studant["grade"]
#             name = studant["name"]
#     return max_grade
# def get_min_grade(studants):
#     min_grade = students[0]["grade"]
#     for studant in students:
#         if studant["grade"] < min_grade:
#             min_grade = studant["grade"]
#     return min_grade
# def show_statistics(students):
#     min_grade = get_min_grade(students)
#     max_grade = get_highest_grade(students)
#     aveerge = get_average(students)
#     print(f"the max grade: {max_grade}.'\n'min grade: {min_grade}.'\n'averge: {aveerge}")

# runing = True
# while runing:
#     show_menu()
#     choice = input("Choice: ")
#     if choice == "1":
#         show_students()
#     if choice == "2":
#         add_student(students)
#     if choice == "3":
#         name = input("Enter name: ")
#         searche = search_student(students,name)
#         print(searche)
#     if choice == "4":
#         n = input("Enter name: ")
#         grade = int(input("Enter grade: "))
#         update_grade(students,n,grade)
#     if choice == "5":
#         name_remove = input("Enter name: ")
#         remove_student(students,name_remove)
#     if choice == "6":
#         passing = get_passing_students(students)
#         print(passing)
#     if choice == "7":
#         show_statistics(students)
#     if choice == "8":
#         above = above_average(students)
#         print(above)
#     if choice == "9":
#         runing = False

    





























