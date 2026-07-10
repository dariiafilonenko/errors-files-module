departments_sales = {
    "Tech": 150000,
    "Marketing": 0,
    "Sales": 450000,
    "HR": 0,
    "Finance": 120000,
    "Legal": 0,
    "Operations": 85000,
    "Customer Support": 25000
}
departments_employees = {
    "Tech": 15,
    "Marketing": 0,
    "Sales": 30,
    "HR": 0,
    "Finance": 8,
    "Legal": 0,
    "Operations": 12,
    "Customer Support": 5
}
avg_revenue = {}
for r in departments_sales:
    try:
        avg= round(departments_sales[r] / departments_employees[r])
        avg_revenue[r] = avg
    except ZeroDivisionError:
        print(f"Department {r} doesn't have employees")
        avg_revenue[r] = 0
print(avg_revenue)