# Python Practice - Part 5: Mixed Data Structures (Questions 41-50)
# Rules: no loops, no comprehensions, no lambda, no hardcoded answers


# ---------------- Q41. Student Performance System ----------------
print("----- Q41 -----")
students = [
    {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
    {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
    {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
]

s1 = students[0]
s2 = students[1]
s3 = students[2]

averages = {
    s1["name"]: sum(s1["marks"]) / len(s1["marks"]),
    s2["name"]: sum(s2["marks"]) / len(s2["marks"]),
    s3["name"]: sum(s3["marks"]) / len(s3["marks"])
}

top_student = max(averages, key=averages.get)
names = (s1["name"], s2["name"], s3["name"])
unique_marks = set(s1["marks"] + s2["marks"] + s3["marks"])

print("Averages:", averages)
print("Top student:", top_student)
print("Names:", names)
print("Unique marks:", unique_marks)


# ---------------- Q42. Employee Skills ----------------
print("\n----- Q42 -----")
employees = {
    "Ali": {"Python", "SQL", "AWS"},
    "Sara": {"Python", "Databricks", "SQL"},
    "Ahmed": {"AWS", "Snowflake", "SQL"}
}

common = employees["Ali"] & employees["Sara"] & employees["Ahmed"]
ali_only = employees["Ali"] - employees["Sara"] - employees["Ahmed"]
all_skills = employees["Ali"] | employees["Sara"] | employees["Ahmed"]

required = {"Python", "SQL"}
qualified = []
if required.issubset(employees["Ali"]):
    qualified.append("Ali")
if required.issubset(employees["Sara"]):
    qualified.append("Sara")
if required.issubset(employees["Ahmed"]):
    qualified.append("Ahmed")

print("Common skills:", common)
print("Ali only skills:", ali_only)
print("All team skills:", all_skills)
print("Python + SQL employees:", qualified)


# ---------------- Q43. Sales Data ----------------
print("\n----- Q43 -----")
sales = [
    ("Laptop", 120000, 2),
    ("Mouse", 1500, 5),
    ("Keyboard", 3500, 3)
]

revenue = {
    sales[0][0]: sales[0][1] * sales[0][2],
    sales[1][0]: sales[1][1] * sales[1][2],
    sales[2][0]: sales[2][1] * sales[2][2]
}

total_revenue = sum(revenue.values())
top_product = max(revenue, key=revenue.get)
prices = {sales[0][1], sales[1][1], sales[2][1]}

print("Revenue per product:", revenue)
print("Total revenue:", total_revenue)
print("Top revenue product:", top_product)
print("Set of prices:", prices)


# ---------------- Q44. Customer Orders ----------------
print("\n----- Q44 -----")
customers = {
    "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
    "C102": {"name": "Sara", "orders": [3000, 4500]},
    "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
}

c1 = customers["C101"]
c2 = customers["C102"]
c3 = customers["C103"]

spending = {
    c1["name"]: sum(c1["orders"]),
    c2["name"]: sum(c2["orders"]),
    c3["name"]: sum(c3["orders"])
}

top_customer = max(spending, key=spending.get)
totals_in_id_order = (sum(c1["orders"]), sum(c2["orders"]), sum(c3["orders"]))

print("Spending:", spending)
print("Top customer:", top_customer)
print("Totals (C101, C102, C103):", totals_in_id_order)


# ---------------- Q45. Course Enrollment ----------------
print("\n----- Q45 -----")
courses = {
    "Python": {"Ali", "Sara", "Ahmed"},
    "SQL": {"Sara", "Ahmed", "Zain"},
    "AWS": {"Ali", "Ahmed", "Zain"}
}

py = courses["Python"]
sql = courses["SQL"]
aws = courses["AWS"]

all_three = py & sql & aws
at_least_two = (py & sql) | (py & aws) | (sql & aws)
exactly_two = at_least_two - all_three
everyone = py | sql | aws
exactly_one = everyone - at_least_two

print("Exactly two courses:", exactly_two)
print("All three courses:", all_three)
print("Exactly one course:", exactly_one)
print("Unique students:", len(everyone))


# ---------------- Q46. E-Commerce Transactions ----------------
print("\n----- Q46 -----")
transactions = [
    {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
    {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
    {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
]

t1 = transactions[0]
t2 = transactions[1]
t3 = transactions[2]

t1_total = t1["items"][0][1] * t1["items"][0][2] + t1["items"][1][1] * t1["items"][1][2]
t2_total = t2["items"][0][1] * t2["items"][0][2] + t2["items"][1][1] * t2["items"][1][2]
t3_total = t3["items"][0][1] * t3["items"][0][2]

totals = {t1["id"]: t1_total, t2["id"]: t2_total, t3["id"]: t3_total}
total_revenue = sum(totals.values())

ali_spending = 0
if t1["customer"] == "Ali":
    ali_spending += t1_total
if t2["customer"] == "Ali":
    ali_spending += t2_total
if t3["customer"] == "Ali":
    ali_spending += t3_total

largest_transaction = max(totals, key=totals.get)

products = {
    t1["items"][0][0], t1["items"][1][0],
    t2["items"][0][0], t2["items"][1][0],
    t3["items"][0][0]
}

print("Total revenue:", total_revenue)
print("Ali spending:", ali_spending)
print("Largest transaction ID:", largest_transaction, "Amount:", totals[largest_transaction])
print("Unique products:", products)


# ---------------- Q47. Pipeline Monitoring ----------------
print("\n----- Q47 -----")
pipelines = {
    "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
    "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
    "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
}

p1 = pipelines["pipeline_1"]
p2 = pipelines["pipeline_2"]
p3 = pipelines["pipeline_3"]

pipeline_totals = {
    "pipeline_1": sum(p1["records"]),
    "pipeline_2": sum(p2["records"]),
    "pipeline_3": sum(p3["records"])
}

total_processed = sum(pipeline_totals.values())

failed = []
if p1["status"] == "failed":
    failed.append("pipeline_1")
if p2["status"] == "failed":
    failed.append("pipeline_2")
if p3["status"] == "failed":
    failed.append("pipeline_3")

largest_pipeline = max(pipeline_totals, key=pipeline_totals.get)

average_per_run = {
    "pipeline_1": sum(p1["records"]) / len(p1["records"]),
    "pipeline_2": sum(p2["records"]) / len(p2["records"]),
    "pipeline_3": sum(p3["records"]) / len(p3["records"])
}

print("Total processed records:", total_processed)
print("Failed pipelines:", failed)
print("Largest pipeline:", largest_pipeline)
print("Average per run:", average_per_run)


# ---------------- Q48. Banking Transactions ----------------
print("\n----- Q48 -----")
accounts = {
    "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
    "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
    "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
}

a1 = accounts["A101"]
a2 = accounts["A102"]
a3 = accounts["A103"]

# starting balance zero hai, is liye final balance = sab transactions ka sum
balances = {
    a1["holder"]: sum(a1["transactions"]),
    a2["holder"]: sum(a2["transactions"]),
    a3["holder"]: sum(a3["transactions"])
}

highest_balance = max(balances, key=balances.get)

# withdrawals = negative numbers. Sab ko jor kar 0 daala aur sort kiya,
# ab 0 se pehle wale sab numbers negative (withdrawals) hain
all_transactions = a1["transactions"] + a2["transactions"] + a3["transactions"]
sorted_list = sorted(all_transactions + [0])
zero_position = sorted_list.index(0)
total_withdrawals = -sum(sorted_list[:zero_position])

largest_deposit = max(all_transactions)

print("Final balances:", balances)
print("Highest balance:", highest_balance, balances[highest_balance])
print("Total withdrawals:", total_withdrawals)
print("Largest single deposit:", largest_deposit)


# ---------------- Q49. Product Recommendations ----------------
print("\n----- Q49 -----")
users = {
    "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
    "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
    "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
}

ali_p = users["Ali"]["purchased"]
sara_p = users["Sara"]["purchased"]
ahmed_p = users["Ahmed"]["purchased"]

ali_w = users["Ali"]["wishlist"]
sara_w = users["Sara"]["wishlist"]
ahmed_w = users["Ahmed"]["wishlist"]

bought_by_two = (ali_p & sara_p) | (ali_p & ahmed_p) | (sara_p & ahmed_p)
ali_wish_not_bought = ali_w - ali_p
shared_wishlist = (ali_w & sara_w) | (ali_w & ahmed_w) | (sara_w & ahmed_w)
all_products = ali_p | sara_p | ahmed_p | ali_w | sara_w | ahmed_w

print("Bought by at least two users:", bought_by_two)
print("Ali wishlist minus purchases:", ali_wish_not_bought)
print("Shared wishlist products:", shared_wishlist)
print("All products:", all_products)


# ---------------- Q50. Final Company Analysis ----------------
print("\n----- Q50 -----")
company = {
    "departments": {
        "Engineering": {
            "employees": [
                ("Ali", 120000, {"Python", "AWS", "SQL"}),
                ("Sara", 150000, {"Python", "Databricks", "SQL"})
            ],
            "budget": 500000
        },
        "Analytics": {
            "employees": [
                ("Ahmed", 100000, {"SQL", "Power BI"}),
                ("Zain", 130000, {"Python", "SQL", "Tableau"})
            ],
            "budget": 400000
        }
    }
}

eng = company["departments"]["Engineering"]
ana = company["departments"]["Analytics"]

e1 = eng["employees"][0]
e2 = eng["employees"][1]
a1 = ana["employees"][0]
a2 = ana["employees"][1]

# 1. Payroll per department
payroll = {
    "Engineering": e1[1] + e2[1],
    "Analytics": a1[1] + a2[1]
}
print("1. Payroll per department:", payroll)

# 2. Company payroll
company_payroll = sum(payroll.values())
print("2. Company payroll:", company_payroll)

# 8. Name-to-salary dictionary (pehle bana liya kyunke 3 mein kaam aayega)
salaries = {e1[0]: e1[1], e2[0]: e2[1], a1[0]: a1[1], a2[0]: a2[1]}

# 3. Highest-paid employee
highest_paid = max(salaries, key=salaries.get)
print("3. Highest-paid employee:", highest_paid, salaries[highest_paid])

# 4. Skills shared by all
shared_skills = e1[2] & e2[2] & a1[2] & a2[2]
print("4. Skills shared by all:", shared_skills)

# 5. Engineering-only skills
eng_skills = e1[2] | e2[2]
ana_skills = a1[2] | a2[2]
print("5. Engineering-only skills:", eng_skills - ana_skills)

# 6. Remaining budget per department
remaining = {
    "Engineering": eng["budget"] - payroll["Engineering"],
    "Analytics": ana["budget"] - payroll["Analytics"]
}
print("6. Remaining budget:", remaining)

# 7. Department with higher average salary
avg_salary = {
    "Engineering": payroll["Engineering"] / len(eng["employees"]),
    "Analytics": payroll["Analytics"] / len(ana["employees"])
}
print("7. Higher average salary:", max(avg_salary, key=avg_salary.get), avg_salary)

# 8. Name-to-salary dictionary
print("8. Name to salary:", salaries)

# 9. All unique skills
print("9. All unique skills:", eng_skills | ana_skills)

# 10. Is combined budget sufficient?
combined_budget = eng["budget"] + ana["budget"]
print("10. Budget sufficient:", combined_budget >= company_payroll,
      "(Budget:", combined_budget, "Payroll:", company_payroll, ")")
