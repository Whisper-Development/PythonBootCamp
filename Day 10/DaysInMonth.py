def is_leap(year):
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
   # Check if the year is a leap year.
  is_leap_year = is_leap(year)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
   # Adjust the number of days in February if it is a leap year.
  if is_leap_year and month == 2:
    month_days[1] = 29

  # Return the number of days in the month.
  return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

