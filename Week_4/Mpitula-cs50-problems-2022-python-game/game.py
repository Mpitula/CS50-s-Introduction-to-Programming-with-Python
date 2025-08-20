import random

def main():
    guess = getinput()
    print(guess)

def getinput():
    while True:
        try:
            result = ""
            level = int(input("Level: "))
            if level <= 0:  # Prevent non-positive integers
                continue
            num_rand = random.randint(1,level)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess <= 0:  # Prevent non-positive integers
                        continue
                    if num_rand == guess:
                        result = "Just right!"
                        break
                    elif guess < num_rand:
                        print("Too small!")
                    elif guess > num_rand:
                        print("Too large!")
                except ValueError:
                    pass
            return result
        except ValueError:
            pass
main()
