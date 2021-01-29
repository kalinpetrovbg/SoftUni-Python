from datetime import date
import calendar

holiday = date(2021, 3, 3)
today = date.today()
print(f"Today is :{today}")

result = holiday - today
print("Remaining days to the national holiday: %d" % result.days)

print()
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2021, 1, 0, 0)
print(st)