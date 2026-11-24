#תרגיל 1
# numbers = (10,20,30,40,50)
# print(numbers)
# print(numbers[0],numbers[-1])
# print(numbers[0:3])
# print(len(numbers))

#תרגיל 2
# names = ("pini","michal","dana","david","dani")
# for name in names:
#     print(name)
# if "pini" in names:
#     print(True)
# print(f"Have {len(names)} studants")

#תרגיל 3
# numbers = (10,65,98,78,4,2,5,8,9)
# print(numbers[0:3])
# print(numbers[-3:])
# print(numbers[::-1])

#תרגיל 4
# products = ("laptop",1000,10,"hi-tec")
# print(products[0])
# print(products[2])

#תרגיל 5
# numbers = [14,98,78,97,45,78,90,99,100]
# even_num = 0
# counter = 0
# max_num = numbers[0]
# for num in numbers:
#     counter += num
#     if num > max_num:
#         max_num = num
#     if num %2 == 0:
#         even_num += 1

#תרגיל 6
# products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
# products1 = products[0:3]
# products2 = products[-2:]
# products3 = products1+products2
# print(products3)

#תרגיל 7
# dicti = {"name":"Noa","age":23,"grade":100,"city":"Jeruslem"}
# for k in dicti:
#     print(dicti[k])

#תרגיל 8
# cars = {"brand":"Toyota","model":"Corola","year":2021,"price":80000}
# cars["price"]=75000
# cars["year"]=2020
# cars["colar"]="white"
# print(cars)

#תרגיל 9
# salaries = {    "David": 12000,    "Moshe": 15000,    "Dana": 13500}
# for k in salaries:
#     print(salaries[k])
# salaries["Dana"]=12500
# salaries["pini"]=30000
# print(salaries)

#תרגיל 10
# menu = {"pizza":63,"pasta":58,"cola":9,"ice-cream":16}
# product = input("Enter product: ")
# for k in menu:
#     if k == product:
#         print(menu[product])
#         break
#     else:
#         print("its not on the menu")
#         break

#תרגיל 11
# studant_grade = {"pini":90,"avi":78,"meni":97,"eli":87,"yoel":76}
# for k,v in studant_grade.items():
#     print(f"Studant: {k} | Grade: {v}")

#תרגיל 12
# grades = {"David": 90,"Moshe": 75,"Dana": 100,"Noa": 55,"Avi": 82}
# max_grade = grades["David"]
# field = 0
# total = 0
# for k in grades:
#     total += grades[k]
#     if grades[k] > 79:
#         print(grades[k])
#     if grades[k] > max_grade:
#        max_grade = grades[k]
#     if grades[k] < 60:
#         field += 1
# print(f"big studant grade {max_grade} field: {field} averge: {total/len(grades)}")

#תרגיל 13
# menu = {"pizza":63,"pasta":58,"cola":9,"ice-cream":16,"sheik":23}
# product = input("Enter the product name: ")
# price = int(input("Enter the new price"))
# menu[product] = price
# print(menu)

#תרגיל 14
# students = [{"name": "David", "age": 20, "grade": 90},{"name": "Moshe", "age": 22, "grade": 75},{"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
# total = 0
# max_studant = 0
# greet_studant = None
# for d in students:
#     total += d["grade"]
#     if d["grade"] > max_studant:
#         max_studant = d["grade"]
#         greet_studant = d["name"]
#     if d["grade"] > 79:
#         print(f"this studant big of 80 {d["name"]}")
# print(f"the greet studant {greet_studant}. is grade {max_studant}")
# print(f"averge {total/len(students)}")

#תרגיל 15
# students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
# print(students)
# students.append({"name":"Dnieal","age":24,"grade":93})
# change_grade = int(input("Enter a new grade: "))
# name = input("Enter studant name: ")
# for s in students:
#     if s["name"] == name:
#         s["grade"] = change_grade
# deleta_studant = input("Enter name do you whant deleit: ")
# for studant in students:
#     if studant["name"] == deleta_studant:
#         students.remove(studant)
# print(students) 

#תרגיל 16
# classroom = {    "Class A": ["David", "Moshe", "Dana"],    "Class B": ["Noa", "Avi", "Michael"],    "Class C": ["Daniel", "Shir", "Yossi"]}
# for k in classroom:
#     print(k)
# print(classroom["Class A"])
# classroom["Class B"].append("Pinhas")
# classroom["Class C"].remove("Yossi")
# for c in classroom:
#     print(len(classroom[c]))

#תרגיל 17
# products = {    "Laptop": {        "price": 4500,        "stock": 10    },    "Mouse": {        "price": 80,        "stock": 50    },    "Keyboard": {        "price": 150,        "stock": 20    }}
# for k in products:
#     print(products[k]["price"])
#     print(products[k]["stock"])
# products["Laptop"]["stock"] = 30
# products["Screen"] = {"price":3500,"stock":20}
# for p in products:
#     if products[p]["price"] > 99:
#         print(p,products[p])

#תרגיל 18
# employees = [("David", "Development", 15000),("Moshe", "Marketing", 12000),("Dana", "Development", 18000),("Noa", "HR", 11000)]
# total = 0
# max_salary = 0
# name_max = None
# for t in employees:
#     if t[1] == "Development":
#         print(t[0])
# for employee in employees:
#     total += employee[2]
#     if employee[2] > max_salary:
#         max_salary = employee[2]
#         name_max = employee[0]
# print(name_max)
# print(total/len(employees))

#תרגיל 19
# inventory = {    "Laptop": 10,    "Mouse": 50,    "Keyboard": 20}
# product = input("Enter product name: ")
# quntaty = int(input("Enter quntaty: "))
# if product not in inventory.keys():
#     print ("This product not in the dictienary")
# elif inventory[product] < quntaty:
#     print("Not enoghy quntaty")
# else:
#     inventory[product] -= quntaty
#     print(inventory[product])

#תרגיל 20
# votes = { "David": 0,"Moshe": 0, "Dana": 0}
# runing = True
# while runing:
#     print("1. For David")
#     print("2. for Moshe")
#     print("3. for Dana")
#     print("4. Exit")
#     vote = input("Enter your vote: ")
#     if vote == "1":
#         votes["David"] += 1
#     if vote == "2":
#         votes["Moshe"] +=1
#     if vote == "3":
#         votes["Dana"] += 1
#     if vote == "4":
#         runing = False
# winer = 0
# name_winer = None
# for v in votes:
#     if votes[v] > winer:
#         name_winer = v
#         winer += votes[v]
# print(f"The result of votes {votes}")
# print(name_winer)

#תרגיל 21
# contact_persons = {"avi":"05656486","pini":"050548756","shlomo":"05879566"}
# runing = True
# while runing:
#     print("1. add person")
#     print("2. serch person")
#     print("3. deleta person")
#     print("4. update person")
#     print("5. show all persons")
#     print("6. Exit")
#     choice = input("Choice:")
#     if choice == "1":
#         person = input("Person name: ")
#         number = input("Number fhone: ")
#         contact_persons[person]=number
#     if choice == "2":
#         name = input("Enter person name: ")
#         for p in contact_persons:
#             if p == name:
#                 print(p,contact_persons[p])
#     if choice == "3":
#         del_person = input("Enter name: ")
#         for per in contact_persons:
#             if contact_persons[per] == del_person:
#                 contact_persons.pop(del_person)
#     if choice == "4":
#         name_person = input("Enter name: ")
#         update = input("New number")
#         for pe in contact_persons:
#             if contact_persons[pe] == name_person:
#                 contact_persons[pe] = update
#     if choice == "5":
#         for k,v in contact_persons.items():
#             print(k, v)
#     if choice == "6":
#         runing = False 

#מערכת ניהול חנות
# products = [    {"name": "Laptop", "price": 4500, "stock": 10},    {"name": "Mouse", "price": 80, "stock": 50},    {"name": "Keyboard", "price": 150, "stock": 20},    {"name": "Screen", "price": 900, "stock": 15}]
# runing = True
# while runing:
#     print("===== Store Management =====")
#     print("1. Show all products")
#     print("2. Add product")
#     print("3. Search product")
#     print("4. Update product price")
#     print("5. Update product stock")
#     print("6. Sell product")
#     print("7. Show products by price")
#     print("8. Show products with low stock")
#     print("9. Show total inventory value")
#     print("0. Exit")
#     choice = input("Choice: ")
#     if choice == "1":
#         for product in products:
#             print(product["name"],product["price"],product["stock"])
#     if choice == "2":
#         dicti = {"name":None,"price":0,"stock":0}
#         dicti["name"] = input("Enter name: ")
#         dicti["price"] = input("Enter price: ")
#         dicti["stock"] = input("Enter quntaty: ")
#         products.append(dicti)
#     if choice == "3":
#         search = input("Enter product name: ")
#         for p in products:
#             if p["name"] == search:
#                 print(p["name"],p["price"],p["stock"])
#     if choice == "4":
#         name_product = input("Enter name: ")
#         new_price = int(input("Enter new price: "))
#         for d in products:
#             if d["name"] == name_product:
#                 d["price"] = new_price
#     if choice == "5":
#         p_name = input("Enter product name: ")
#         new_stock = int(input("Enter new stock"))
#         for dicti in products:
#             if dicti["name"] == p_name:
#                 dicti["stock"] = new_stock
#     if choice == "6":
#         product_n = input("Enter product name: ")
#         sell_quntaty = int(input("Enter sell quntaty: "))
#         for preduct in products:
#             if product["name"] == product_n:
#                 if product["stock"] < sell_quntaty:
#                     print("Not enghoy quntaty to sell")
#                 product["stock"] -= sell_quntaty
#     if choice == "7":
#         product_price = input("Enter the price do you whant see: ")
#         for producti in products:
#             if producti["price"] >= product_price:
#                 print(producti["name"],producti["price"],producti["stock"])
#     if choice == "8":
#         for d in products:
#             if d["stock"] < 10:
#                 print(d["name"],d["stock"])
#     if choice == "9":
#         total = 0
#         for p in products:
#             total += p["price"]*p["price"]
#         print(total)
#     if choice == "10":
#         runing = False

    

