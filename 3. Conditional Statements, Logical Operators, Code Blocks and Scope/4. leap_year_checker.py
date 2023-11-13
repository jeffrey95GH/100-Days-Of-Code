"""
A program which checks whether a given year is a 
leap year.  
Leap years are calculated as follows: 
on every year that is evenly divisible by 4
    except every year that is evenly divisible by 100 
        unless the year is also evenly divisible by 400
"""

year = int(input("Which year are we checking? "))

if year % 4 == 0:
    if year % 100 == 0: 
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else: 
            print(f"{year} is not a leap year")
    else: 
        print(f"{year} is a leap year")
else: 
    print(f"{year} is not a leap year")