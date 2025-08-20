names = []

while True:
    
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

if len(names) == 1:
    output = names[0]
elif len(names) == 2:
    output = f"{names[0]} and {names[1]}"
else:
    output = ", ".join(names[:-1]) + f", and {names[-1]}"

print(f"Adieu, adieu, to {output}")
