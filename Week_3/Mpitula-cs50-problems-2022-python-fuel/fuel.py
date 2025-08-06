def main():
    print(get_fraction("Fraction: "))

def get_fraction(prompt):
    while True:
        try:
            frac = input(prompt).strip()
            if  int(frac[0]) >= 0 or int(frac[2]) > 0 and int(frac[0]) > int(frac[2]):
                x = frac.split("/")
                div = (int(x[0])/int(x[1]))*100
                if div <= 1:
                    return "E"
                elif div > 98:
                    return "F"
                else:
                    return f"{round(div)}%"
        except (ValueError, ZeroDivisionError):
            pass
main()
