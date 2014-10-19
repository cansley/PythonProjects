__author__ = 'cxa70'
# page displays title of "whom?"
# page shows calendar with Jan-26th circled
# page shows calendar with 1**6 in the year
# page source has these hints:
#  he aint the youngest, he's the second
#  todo: buy flowers for tomorrow
#
# target date is jan-27th, but what year?
# Feb on calendar shows 29 days, so its a leap year.
# Jan 1 is a Thursday...

import datetime

year = 2010
rndDate = datetime.date(year, 3, 1)  # lets start with march first...
rndDate += datetime.timedelta(days=-1)
while rndDate.day != 29:
    year += -1
    rndDate = datetime.date(year, 3, 1) + datetime.timedelta(days=-1)

startYear = rndDate.year

for x in range(startYear, 1, -4):
    theDate = datetime.date(x, 1, 1)
    theYear = list(str(theDate.year))
    if theDate.weekday() == 3 and theYear[0] == '1' and theYear[-1] == '6':
        newDate = datetime.date(theDate.year, 1, 27)
        print(newDate)

# from the dates produced, find the birtday (hint: its mozart!)