def is_leap(year):
    
        if 1900 <= year <= 10**5:
            if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
                return True
            return False
        return False
year = int(input())
print(is_leap(year))
