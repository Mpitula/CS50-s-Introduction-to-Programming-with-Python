#Ask the user for input
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()

#using conditionals
if answer == "42" or answer.lower() == "forty two" or (" ".join(answer.split("-"))).lower() == "forty two":
    print("Yes")
else:
    print("No")

