def main():

    titlecased = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
            }

    cost = 0


    try:
         while True:
            item = input("Item: ").strip().title()
            if item in titlecased:
                cost += titlecased[item]
                print(f"Total: ${cost:.2f}")
    except EOFError:
            print()

main()
