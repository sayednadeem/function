import datetime
print("Current date and time:",datetime.datetime.now())
print("Current year:",datetime.date.today().strftime("%Y"))
print("month of year:",datetime.date.today().strftime("%B"))
print("week number of the year:",datetime.date.today().strftime("%W"))
print("weekday of the week:",datetime.date.today().strftime("%w"))
print("day of year:",datetime.date.today().strftime("%j"))
print("day of the month:",datetime.date.today().strftime("%d"))
print("day of week:",datetime.date.today().strftime("%A"))

