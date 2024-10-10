def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
        year = int(input("enter year: "))
        if leap_year(year):
            print(f"{year} is true")
        else:
            print(f"{year} is false")

if __name__ == "__main__":
        main()
