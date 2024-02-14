def is_leap(year):
    leap = False
    # come with 4 years
    if year % 4 == 0:
        #but not in every 100 years
        if year % 100 == 0:
            # but also come every 400 years even it were in 100
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))