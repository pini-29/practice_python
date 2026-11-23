#1
# num1 = 25
# num2 = 7
# print(num1+num2,num1-num2,num1/num2,num1*num2,num1//num2,num1%num2)
#2
# balance = 1000
# balance += 250
# print(balance)
# balance -= 100
# print(balance)
# balance *= 2
# print(balance)
# balance /= 4
# print(balance)
#3
# price = int(input("Enter the price"))
# precent = int(input("enter the precnt discount"))
# price_precent = price*precent/100
# print(f" the discount is {price_precent}")
# print(f"you need py {price+price_precent}")
#4
# amount = int(input("enter the amount price"))
# precnt_interst = int(input("enter the precnt interst"))
# new_amount = amount*precnt_interst/100
# print(f"this year you have {amount+new_amount} next year is will be{((amount+new_amount)*precnt_interst/100)+amount+new_amount}")
#5
# grade1 = float(input("enter 1 grade"))
# grade2 = float(input("enter 2 grade"))
# grade3 = float(input("enter 3 grade"))
# print(round((grade1+grade2+grade3)/3,2))
#6
# first_name = "David"
# last_name = "Cohen"
# city = "Tel Aviv"
# print(f"Hello, my name is {first_name} {last_name} and I live in {city}.")
# print("Hello, my name is" + first_name +  last_name + "and I live in" + city)
#7
# full_name = input("enter your full name")
# print(f"{full_name} {len(full_name)} {full_name.upper()} {full_name.lower()}")
#8
# santnce = input("enter full santance")
# print(santnce.upper(),santnce.lower(),santnce.capitalize(),santnce.title())
#9
# name = input("enter name")
# new_name = name.strip()
# print(name)
# print(new_name)
#10
# sentence = "I love Java programming"
# new_sentence = sentence.replace("Java","Python")
# print(new_sentence)
# print(sentence.count("love "))
# print(sentence.startswith("I"))
# print(sentence.endswith("programming"))
#11
# word = "Programming"
# print(word[0])
# print(word[-1])
# print(word[2])
# print(word[0:5:1])
# print(word[::-1])
#12
# a = int("100")
# b = float("25")
# c = str(10)
# d = int(5.5)
# print(type(a),type(b),type(c),type(d))
#13
# age = input("Enter your age: ")
# print(int(age)+10)
#14
# VAT = 0.18
# price = float(input("enter the price"))
# print((price*VAT)+price)
#15
# first_name = input("enter your name")
# last_name = input("enter your last name")
# age = int(input("enter your age"))
# monthly_salary = int(input("enter your month salary"))
# print(len(first_name+last_name))
#16
# usd_rate = 3.25
# commission = 0.2
# uoro_rate = 3.75
# shekel = float(input("enter the price"))
# print(f"the usd rate {shekel*usd_rate} + commission {shekel*commission} ")
#17
# first_name = input("enter your first name")
# last_name = input("enter the last name")
# year_birth = input("enter your birth year")
# print(f"your name email {first_name.lower()}.{last_name.lower()}.{year_birth}@gmail.com")
#18
# full_santance = input("enter full santance")
# print(full_santance,len(full_santance),full_santance.upper(),full_santance.lower(),full_santance[::-1],full_santance.count("a"),full_santance.replace(' ',"-"))
#19
custumer_name = input("enter your name: ")
products_name = input("enter the product name: ")
product_price = int(input("enter product price: "))
quntaty_products = int(input("enter the quntaty: "))
precnt_discount = int(input("enter the precnt discount: "))
vat = float(input("enter the vat"))
total = product_price*quntaty_products
discount = total*precnt_discount/100
totali = discount*vat/100
print("================================")
print("       PURCHASE INVOICE         ")
print("================================")
print(f"Customer: {custumer_name}")
print(f"Product: {products_name}")

print(f"Unit Price: {product_price}")
print(f"Quantity: {quntaty_products}")

print(f"Subtotal: {total}")
print(f"Discount: {total*precnt_discount/100}")
print(f"After Discount: {total-discount}")

print(f"VAT: {vat}%")
print(f"VAT Amount: {(total-discount)*vat/100}")
print(f"TOTAL: {(total-discount)+totali}")

print(" THANK YOU FOR SHOPPING")



