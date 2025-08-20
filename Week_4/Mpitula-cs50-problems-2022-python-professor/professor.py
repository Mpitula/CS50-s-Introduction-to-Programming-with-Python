import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3] :
                return level
            else:
                raise ValueError
        except ValueError:
            print("EEE")

def generate_integer(level):
    count = 1
    score = 0
    while count <= 10:
        x, y = generate_numbers(level)
        correct = x+y

        attempts = 0
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct:
                    score +=1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                attempts+=1

        if attempts == 3:
             print(f"{x} + {y} = {correct}")

        count+=1

    print(f"Score: {score}/10")


def generate_numbers(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:  # level == 3
        return random.randint(100, 999), random.randint(100, 999)

if __name__ == "__main__":
    main()
