# Python Practice - Part 2: Tuples (Questions 11-20)
# Rules: no loops, no comprehensions, no lambda, no hardcoded answers

from operator import itemgetter


# ---------------- Q11. Tuple Indexing ----------------
print("----- Q11 -----")
colors = ("red", "green", "blue", "yellow", "purple")

print("Second:", colors[1])
print("Last:", colors[-1])
print("Middle three:", colors[1:4])


# ---------------- Q12. Tuple Unpacking ----------------
print("\n----- Q12 -----")
employee = ("Ali", 28, "Data Engineer", 150000)

name, age, job, salary = employee

print("Name:", name)
print("Salary:", salary)


# ---------------- Q13. Tuple Concatenation ----------------
print("\n----- Q13 -----")
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

combined = tuple1 + tuple2
reversed_tuple = combined[::-1]

print("Combined:", combined)
print("Reversed:", reversed_tuple)


# ---------------- Q14. Count and Locate ----------------
print("\n----- Q14 -----")
numbers = (10, 20, 30, 20, 40, 20, 50)

print("20 kitni dafa aaya:", numbers.count(20))
print("20 ka pehla index:", numbers.index(20))


# ---------------- Q15. Extended Tuple Unpacking ----------------
print("\n----- Q15 -----")
data = (100, 200, 300, 400, 500, 600)

first, second, *middle, last = data   # * baqi sab ko list mein daal deta hai

print("First:", first)
print("Second:", second)
print("Last:", last)
print("Remaining (list):", middle)


# ---------------- Q16. Modify an Immutable Tuple ----------------
print("\n----- Q16 -----")
numbers = (10, 20, 30, 40, 50)

i = numbers.index(30)
new_numbers = numbers[:i] + (300,) + numbers[i + 1:]

print("Old tuple:", numbers)
print("New tuple:", new_numbers)


# ---------------- Q17. Nested Tuple Access ----------------
print("\n----- Q17 -----")
students = (
    ("Ali", (85, 90, 88)),
    ("Sara", (92, 87, 95)),
    ("Ahmed", (78, 84, 80))
)

sara_second = students[1][1][1]
ali_marks = students[0][1]
ali_average = sum(ali_marks) / len(ali_marks)
ahmed_highest = max(students[2][1])

print("Sara second score:", sara_second)
print("Ali average:", round(ali_average, 2))
print("Ahmed highest score:", ahmed_highest)


# ---------------- Q18. Tuple Sorting ----------------
print("\n----- Q18 -----")
employees = (
    ("Ali", 80000),
    ("Sara", 120000),
    ("Ahmed", 95000)
)

# itemgetter(1) ka matlab: har tuple ki index 1 (salary) se sort karo
sorted_employees = tuple(sorted(employees, key=itemgetter(1), reverse=True))

print("Sorted by salary (high to low):", sorted_employees)


# ---------------- Q19. Tuple Matrix ----------------
print("\n----- Q19 -----")
matrix = ((2, 4, 6), (8, 10, 12), (14, 16, 18))

diagonal = (matrix[0][0], matrix[1][1], matrix[2][2])
product = diagonal[0] * diagonal[1] * diagonal[2]
row_sums = (sum(matrix[0]), sum(matrix[1]), sum(matrix[2]))

print("Diagonal:", diagonal)
print("Product of diagonal:", product)
print("Row sums:", row_sums)


# ---------------- Q20. Inventory Tuple Challenge ----------------
print("\n----- Q20 -----")
records = (
    ("Laptop", 120000, 5),
    ("Mouse", 1500, 20),
    ("Keyboard", 3500, 10)
)

laptop_value = records[0][1] * records[0][2]
mouse_value = records[1][1] * records[1][2]
keyboard_value = records[2][1] * records[2][2]
total_value = laptop_value + mouse_value + keyboard_value

most_expensive = max(records, key=itemgetter(1))   # price index 1 par hai

names = (records[0][0], records[1][0], records[2][0])
reversed_names = names[::-1]

print("Total inventory value:", total_value)
print("Most expensive product:", most_expensive[0])
print("Reversed names:", reversed_names)
