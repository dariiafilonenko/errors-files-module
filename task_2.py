clients_names = [
    "Alice Smith", "Bob", "Charlie Brown", "Diana", "Eve Adams",
    "Frank", "Grace Kelly", "Hank", "Ivy Poison", "Jack",
    "Karen Page", "Leo", "Mona Lisa", "Ned", "Olivia Pope",
    "Paul", "Quinn Fabray", "Rachel", "Steve Rogers", "Tony"
]
last_names=[]

for client in clients_names:
    try:
        last_name = client.split()[1]
        last_names.append(last_name)
    except IndexError:
        last_names.append(f"unknown")
print(last_names)


