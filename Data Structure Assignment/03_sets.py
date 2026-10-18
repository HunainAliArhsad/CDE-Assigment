# Python Practice - Part 3: Sets (Questions 21-30)
# Rules: no loops, no comprehensions, no lambda, no hardcoded answers


# ---------------- Q21. Unique Values ----------------
print("----- Q21 -----")
numbers = [10, 20, 10, 30, 40, 20, 50]

unique_numbers = set(numbers)

print("Set:", unique_numbers)
print("Unique count:", len(unique_numbers))


# ---------------- Q22. Set Operations ----------------
print("\n----- Q22 -----")
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("Union:", a | b)
print("Intersection:", a & b)
print("a - b:", a - b)
print("Symmetric difference:", a ^ b)


# ---------------- Q23. Add and Remove ----------------
print("\n----- Q23 -----")
skills = {"Python", "SQL", "AWS"}

skills.add("Snowflake")
skills.add("Databricks")
skills.discard("AWS")   # discard error nahi deta agar item na ho (safe remove)

print("Skills:", skills)


# ---------------- Q24. Common Students ----------------
print("\n----- Q24 -----")
python_students = {"Ali", "Sara", "Ahmed", "Zain"}
sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}

both = python_students & sql_students
exactly_one = python_students ^ sql_students

print("Both courses:", both)
print("Exactly one course:", exactly_one)


# ---------------- Q25. Subset and Superset ----------------
print("\n----- Q25 -----")
required_skills = {"Python", "SQL"}
candidate_skills = {"Python", "SQL", "AWS", "Snowflake"}

print("Required is subset:", required_skills.issubset(candidate_skills))
print("Candidate is superset:", candidate_skills.issuperset(required_skills))


# ---------------- Q26. Missing Numbers ----------------
print("\n----- Q26 -----")
numbers = {1, 2, 4, 6, 8, 10}

all_numbers = set(range(1, 11))   # 1 se 10 tak
missing = all_numbers - numbers

print("Missing numbers:", sorted(missing))


# ---------------- Q27. Three-Set Analysis ----------------
print("\n----- Q27 -----")
python = {"Ali", "Sara", "Ahmed", "Zain"}
sql = {"Sara", "Ahmed", "Hamza"}
aws = {"Ahmed", "Zain", "Hamza"}

all_three = python & sql & aws
python_sql_not_aws = (python & sql) - aws
at_least_two = (python & sql) | (python & aws) | (sql & aws)

print("All three:", all_three)
print("Python and SQL but not AWS:", python_sql_not_aws)
print("At least two:", at_least_two)


# ---------------- Q28. Transaction Analysis ----------------
print("\n----- Q28 -----")
day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}
day3 = {104, 106, 107, 108}

all_days = day1 & day2 & day3
at_least_two = (day1 & day2) | (day1 & day3) | (day2 & day3)
exactly_one = (day1 | day2 | day3) - at_least_two

print("All days:", all_days)
print("Exactly one day:", exactly_one)
print("At least two days:", at_least_two)


# ---------------- Q29. Access Control ----------------
print("\n----- Q29 -----")
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write", "delete"}

missing = required_permissions - user_permissions
extra = user_permissions - required_permissions
authorized = required_permissions.issubset(user_permissions)

print("Missing permissions:", missing)
print("Extra permissions:", extra)
print("Fully authorized:", authorized)


# ---------------- Q30. Customer Segmentation ----------------
print("\n----- Q30 -----")
website = {"C1", "C2", "C3", "C4", "C5"}
mobile = {"C3", "C4", "C6", "C7"}
store = {"C2", "C4", "C7", "C8"}

all_three = website & mobile & store
at_least_two = (website & mobile) | (website & store) | (mobile & store)
exactly_two = at_least_two - all_three
exactly_one = (website | mobile | store) - at_least_two

print("Exactly one platform:", exactly_one)
print("Exactly two platforms:", exactly_two)
print("All three platforms:", all_three)
