camelCase = input("camelCase: ").strip()
snake_case = []
for i in camelCase:
    if i.isupper():
        snake_case.append("_")
        snake_case.append(i.lower())
    else:
        snake_case.append(i)
print("".join(snake_case))


