customers = input().split(", ")
taxis = input().split(", ")
driving_time = 0

while True:
    customer = int(customers[0])
    customers.pop(0)
    taxi = int(taxis[-1])
    taxis.pop(-1)

    if taxi >= customer:
        driving_time += customer
    else:
        customers.insert(0, customer)

    if not customers:
        print("All customers were driven to their destinations")
        print(f"Total time: {driving_time} minutes")
        break

    if not taxis:
        print("Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join(map(str, customers))}")
        break
