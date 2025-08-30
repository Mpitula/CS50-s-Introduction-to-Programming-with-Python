def main():
    frac = input("Fraction: ").strip()
    percentage = convert(frac)
    guage = gauge(percentage)
    print(guage)

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            num = int(x)
            den = int(y)
            if num < 0 or den <= 0 or den < num :
                continue
            div = (num/den)*100
        except (ValueError, ZeroDivisionError):
            pass
        return div

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()
