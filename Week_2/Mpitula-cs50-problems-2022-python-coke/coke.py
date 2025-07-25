valid_coins = [25, 10, 5]
amount_due = 50
total_inserted = 0

while total_inserted < amount_due:
    print(f"Amount Due: {amount_due - total_inserted}")
    try:
        coin = int(input("Insert Coin: "))
        if coin in valid_coins:
            total_inserted += coin
        else:
            print("Coin not accepted.")
    except ValueError:
        print("Please insert a valid integer coin.")

change = total_inserted - amount_due
print(f"Change Owed: {change}")
