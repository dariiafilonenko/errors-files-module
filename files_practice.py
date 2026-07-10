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
# failed = []
# with open("files/transactions.csv", "r", encoding="utf=8") as file:
#      reader = csv.DictReader(file)
#      for row in reader:
#          if row["status"] == "failed":
#              failed.append(row)
# with open("output files/failed_transactions.csv", "w", encoding="utf-8", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["id", "amount", "category", "status"])
#     writer.writeheader()
#     writer.writerows(failed)



# with open("files/users.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#     for user in data:
#         if user["balance"] >= 1000:
#             user["status"] = "VIP"
#         else:
#             user["status"] = "Regular"
# with open("output files/new_users.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=4)
#     print(data)

with open("files/users.json", "r", encoding="utf-8") as file:
     data = json.load(file)
     for user in data:
         user["balance"] += 50
with open("output files/new_updated_users.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)






