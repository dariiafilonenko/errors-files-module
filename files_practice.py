import csv
import json

# Ваш код для завдань нижче:
# suma = 0
# succ = []
# with open("files/transactions.csv", "r", encoding="utf=8") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         try:
#             suma += float(row["amount"])
#             succ.append(row)
#         except ValueError:
#             continue
# print(succ)
# with open("output files/st.csv", "w") as file:
#     writer = csv.DictWriter(file, fieldnames=["id", "amount", "category", "status"])
#     writer.writeheader() # Обов'язково записуємо заголовки колонок
#     writer.writerows(succ)

with open("files/transactions.csv", "r", encoding="utf=8") as file:
     reader = csv.DictReader(file)
     for row in reader:
         try:
             succ =float(row["amount"])
         except ValueError:
             




