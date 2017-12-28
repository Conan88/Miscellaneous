import time
from datetime import date

today = date.today()
today == date.fromtimestamp(time.time())

christmas = date(today.year, 12, 24)

if christmas < today:
	christmas = christmas.replace(year=today.year + 1)

daysToChristmas = abs(christmas - today)
print(daysToChristmas.days, "days till christmas")
