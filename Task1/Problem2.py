# for the years that come with 366 days 

def leap_year_check(year):
    # come with 4 years
    if year % 4 == 0:
        #but not in every 100 years
        if year % 100 == 0:
            # but also come every 400 years even it were in 100
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# every month come with different days
def is_last(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leap_year_check(year):
            return 29
        else:
            return 28

def print_tomorrows_date(day, month, year):
    last_day = is_last(month, year)

    if day < last_day:
        day += 1
    else:
        day = 1
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1

    print("Output: Day:", day, "Month:", month, "Year:", year)

def main():
    day = int(input("Enter Day: "))
    month = int(input("Enter Month: "))
    year = int(input("Enter Year: "))

    print_tomorrows_date(day, month, year)

if __name__ == "__main__":
    main()
