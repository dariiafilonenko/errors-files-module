complex_data = [
    {"client": "Alice Smith", "amount": "1200"},
    {"client": "Bob", "amount": "400"},
    {"client": "Charlie Brown", "amount": "N/A"},
    {"client": "Diana Prince", "amount": "5500"},
    {"client": "Eve", "amount": "Error"},
    {"client": "Frank Castle", "amount": "800"},
    {"client": "Grace", "amount": "150.50"},
    {"client": "Hank Pym", "amount": "-"},
    {"client": "Ivy", "amount": "3000"},
    {"client": "Jack Reacher", "amount": "NULL"}
]
lastname_transaction = []
for r in complex_data:
    try:
        last_name = r["client"].split()[1]
        r["last_name"]= last_name
    except IndexError:
        print(f"Client {r['client']} has no last name")
        r["client"] = "Unknown"
    try:
        r["amount"]= float(r["amount"])
    except ValueError:
        print(f"Client {r['client']} has no amount {r['amount']}")
        r["amount"]= 0
print(complex_data)
