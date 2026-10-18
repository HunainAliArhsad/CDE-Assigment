# Python Practice - Part 4: Dictionaries (Questions 31-40)
# Rules: no loops, no comprehensions, no lambda, no hardcoded answers


# ---------------- Q31. Dictionary Access ----------------
print("----- Q31 -----")
student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}

print("Name:", student["name"])
print("Marks:", student["marks"])
print("City:", student.get("city", "Karachi"))   # city nahi hai to Karachi


# ---------------- Q32. Update Dictionary ----------------
print("\n----- Q32 -----")
employee = {"name": "Sara", "salary": 100000, "department": "IT"}

employee["salary"] = int(employee["salary"] * 1.20)   # 20% raise
employee["bonus"] = 15000
employee["department"] = "Data Engineering"

print("Updated employee:", employee)


# ---------------- Q33. Dictionary Methods ----------------
print("\n----- Q33 -----")
product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}

print("Keys:", list(product.keys()))
print("Values:", list(product.values()))
print("Items:", list(product.items()))

stock = product.pop("stock")   # stock hata di, value variable mein rakh li

print("Removed stock value:", stock)
print("Product now:", product)


# ---------------- Q34. Merge Dictionaries ----------------
print("\n----- Q34 -----")
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 50, "d": 40}

merged = dict1.copy()
merged.update(dict2)   # same key ho to dict2 ki value aa jati hai

print("Merged:", merged)


# ---------------- Q35. Student Marks ----------------
print("\n----- Q35 -----")
marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}

highest = max(marks.values())
lowest = min(marks.values())
average = sum(marks.values()) / len(marks)
top_student = max(marks, key=marks.get)   # sab se zyada marks wali key

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Top student:", top_student)


# ---------------- Q36. Nested Employee Records ----------------
print("\n----- Q36 -----")
employees = {
    "E101": {"name": "Ali", "salary": 80000},
    "E102": {"name": "Sara", "salary": 120000},
    "E103": {"name": "Ahmed", "salary": 95000}
}

sara_salary = employees["E102"]["salary"]
employees["E101"]["salary"] = round(employees["E101"]["salary"] * 1.15)   # 15% raise

total_payroll = (employees["E101"]["salary"]
                 + employees["E102"]["salary"]
                 + employees["E103"]["salary"])

print("Sara salary:", sara_salary)
print("Ali new salary:", employees["E101"]["salary"])
print("Total payroll:", total_payroll)


# ---------------- Q37. Dictionary Inversion ----------------
print("\n----- Q37 -----")
data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}

inverse = dict(zip(data.values(), data.keys()))   # values ko keys bana diya

print("Inverse:", inverse)


# ---------------- Q38. Order Calculation ----------------
print("\n----- Q38 -----")
order = {
    "laptop": {"price": 120000, "quantity": 2},
    "mouse": {"price": 1500, "quantity": 5},
    "keyboard": {"price": 3500, "quantity": 3}
}

subtotals = {
    "laptop": order["laptop"]["price"] * order["laptop"]["quantity"],
    "mouse": order["mouse"]["price"] * order["mouse"]["quantity"],
    "keyboard": order["keyboard"]["price"] * order["keyboard"]["quantity"]
}

grand_total = sum(subtotals.values())
after_discount = grand_total * 0.90   # 10% discount

print("Subtotals:", subtotals)
print("Grand total:", grand_total)
print("After 10% discount:", after_discount)


# ---------------- Q39. Employee Performance ----------------
print("\n----- Q39 -----")
employees = {
    "Ali": {"python": 90, "sql": 85, "aws": 88},
    "Sara": {"python": 95, "sql": 92, "aws": 90},
    "Ahmed": {"python": 80, "sql": 87, "aws": 84}
}

averages = {
    "Ali": sum(employees["Ali"].values()) / len(employees["Ali"]),
    "Sara": sum(employees["Sara"].values()) / len(employees["Sara"]),
    "Ahmed": sum(employees["Ahmed"].values()) / len(employees["Ahmed"])
}

top_performer = max(averages, key=averages.get)

sql_scores = {
    "Ali": employees["Ali"]["sql"],
    "Sara": employees["Sara"]["sql"],
    "Ahmed": employees["Ahmed"]["sql"]
}
highest_sql = max(sql_scores.values())

print("Averages:", averages)
print("Top performer:", top_performer)
print("Highest SQL score:", highest_sql, "by", max(sql_scores, key=sql_scores.get))


# ---------------- Q40. Inventory Management ----------------
print("\n----- Q40 -----")
inventory = {
    "P101": {"name": "Laptop", "price": 120000, "stock": 5},
    "P102": {"name": "Mouse", "price": 1500, "stock": 20},
    "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
}

item_values = {
    "Laptop": inventory["P101"]["price"] * inventory["P101"]["stock"],
    "Mouse": inventory["P102"]["price"] * inventory["P102"]["stock"],
    "Keyboard": inventory["P103"]["price"] * inventory["P103"]["stock"]
}

total_value = sum(item_values.values())
most_valuable = max(item_values, key=item_values.get)

# 2 laptops aur 5 mouse bik gaye
inventory["P101"]["stock"] -= 2
inventory["P102"]["stock"] -= 5

print("Total inventory value:", total_value)
print("Most valuable item:", most_valuable)
print("Laptop stock now:", inventory["P101"]["stock"])
print("Mouse stock now:", inventory["P102"]["stock"])
