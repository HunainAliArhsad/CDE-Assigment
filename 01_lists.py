# Python Practice - Part 1: Lists (Questions 1-10)
# Rules: no loops, no comprehensions, no lambda, no hardcoded answers


# ---------------- Q1. Accessing List Elements ----------------
print("----- Q1 -----")
numbers = [10, 20, 30, 40, 50, 60, 70]

first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]

print("First:", first)
print("Middle:", middle)
print("Last:", last)
print("Original list:", numbers)


# ---------------- Q2. List Slicing ----------------
print("\n----- Q2 -----")
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

first_five = numbers[:5]
last_four = numbers[-4:]
every_second_reverse = numbers[::-2]

print("First five:", first_five)
print("Last four:", last_four)
print("Every second in reverse:", every_second_reverse)


# ---------------- Q3. List Modification ----------------
print("\n----- Q3 -----")
fruits = ["apple", "banana", "cherry", "mango"]

banana_index = fruits.index("banana")
fruits[banana_index] = "orange"     # banana ki jagah orange
fruits.insert(2, "grapes")          # index 2 par grapes
fruits.remove("cherry")             # cherry hata di

print("Updated fruits:", fruits)


# ---------------- Q4. Reverse Without reverse() ----------------
print("\n----- Q4 -----")
numbers = [12, 45, 23, 67, 89, 34]

reversed_numbers = numbers[::-1]

print("Original:", numbers)
print("Reversed:", reversed_numbers)


# ---------------- Q5. Second Largest Unique Number ----------------
print("\n----- Q5 -----")
numbers = [45, 12, 89, 34, 89, 67, 45, 23]

unique_numbers = sorted(set(numbers))   # set duplicates hata deta hai
second_largest = unique_numbers[-2]

print("Second largest unique:", second_largest)


# ---------------- Q6. Rotate a List ----------------
print("\n----- Q6 -----")
numbers = [10, 20, 30, 40, 50, 60]
k = 2

rotated = numbers[-k:] + numbers[:-k]

print("Rotated list:", rotated)


# ---------------- Q7. Remove Duplicates, Preserve Order ----------------
print("\n----- Q7 -----")
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

# dictionary keys repeat nahi hoti aur order bhi wahi rehta hai
no_duplicates = list(dict.fromkeys(numbers))

print("Without duplicates:", no_duplicates)


# ---------------- Q8. Flatten a Nested List ----------------
print("\n----- Q8 -----")
data = [[10, 20], [30, 40], [50, 60]]

flat_list = data[0] + data[1] + data[2]   # lists ko + se jor diya

print("Flat list:", flat_list)


# ---------------- Q9. Extract Data from a Matrix ----------------
print("\n----- Q9 -----")
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

main_diagonal = [matrix[0][0], matrix[1][1], matrix[2][2]]
secondary_diagonal = [matrix[0][2], matrix[1][1], matrix[2][0]]
middle_column = [matrix[0][1], matrix[1][1], matrix[2][1]]

print("Main diagonal:", main_diagonal, "Sum:", sum(main_diagonal))
print("Secondary diagonal:", secondary_diagonal, "Sum:", sum(secondary_diagonal))
print("Middle column:", middle_column, "Sum:", sum(middle_column))


# ---------------- Q10. List Transformation Challenge ----------------
print("\n----- Q10 -----")
data = [15, 5, 25, 10, 35, 20, 30]

unique_sorted = sorted(set(data))
three_largest = unique_sorted[-3:]         # ascending order mein
two_smallest = unique_sorted[:2][::-1]     # descending order mein

result = three_largest + two_smallest

print("Result:", result)
