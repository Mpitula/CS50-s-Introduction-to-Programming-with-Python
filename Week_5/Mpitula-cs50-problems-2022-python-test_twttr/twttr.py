def main():
    word = input("Input: ")
    shorten(word)


def shorten(word):
    vowels = ["A","E","I","O","U","a","e","i","o","u"]
    result = ""
    for i in word:
        if i not in vowels:
            result+=i
    return result

if __name__ == "__main__":
    main()
