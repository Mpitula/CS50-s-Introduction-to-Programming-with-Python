def main():
    try:
        fruits = []
        while True:
            item = input()
            fruits.append(item.upper())
    except EOFError:
        print()
        count = {}
        for i in fruits:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i, counts in count.items():
            print(f"{counts} {i}")
main()
