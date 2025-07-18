def main():
    time = input("What time is it? ").strip()

    converted_time = convert(time)

    if converted_time >= 7 and converted_time <= 8:
        print("breakfast time")
    elif converted_time >= 12 and converted_time <= 13:
        print("lunch time")
    elif converted_time >= 18 and converted_time <= 19:
        print("dinner time")

def convert(time):
    time = time.split(":")
    new_time = float(time[0]) + (float(time[1])/60)
    return new_time

if __name__ == "__main__":
    main()
