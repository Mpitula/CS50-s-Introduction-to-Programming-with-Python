def main():
    month = [ "January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"
            ]

    while True:
        try:
            date = input("Date: ").strip()  #September 8, 1636  or 8/9/1636 return 1636-08-09
            if "/" in date:
                date = date.split("/")
                mon = int(date[0])
                day = int(date[1])
                year = int(date[2])
                if mon <= 12 and day <= 31:
                    print(f"{year}-{mon:02}-{day:02}")
                    break
            elif "," in date:
                date = date.replace(",","").split(" ")
                mon = month.index(date[0]) + 1
                day = int(date[1])
                year = int(date[2])
                if mon <= 12 and day <= 31:
                    print(f"{year}-{mon:02}-{day:02}")
                    break
        except ValueError:
            pass
main()
