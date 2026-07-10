raw_transactions = [
    "1500", "200", "N/A", "450", "Cancel", "3000", "120.50", "ERROR", "800", "NULL",
    "50.25", "999", "-", "2500", "10", "Empty", "350", "15.99", "Failed", "4200"
]
total=0
for i in raw_transactions:
    try:
        float_i = float(i)
        total = total + float_i
    except ValueError:
        print(f"Encountered invalid transactions: {i}")
print(total)