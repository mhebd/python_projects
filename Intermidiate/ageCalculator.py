# Age calculator

from datetime import date

today = date.today()

bDate = input('Enter your birth day date [dd mm yyyy]: ').split(' ')

cDate = today.strftime('%d %m %Y').split(' ')

bDay = int(bDate[0])
bMon = int(bDate[1])
bYear = int(bDate[2])
cDay = int(cDate[0])
cMon = int(cDate[1])
cYear = int(cDate[2])

if cDay < bDay:
    cDay += 30
    bMon += 1

if cMon < bMon:
    cMon += 12
    bYear += 1

day = cDay - bDay
mon = cMon - bMon
year = cYear - bYear

print("Year age is: {0} Year {1} Month {2} Day".format(year, mon, day))

more = int(input('Press 1 for more or 0 to exit...'))

if more == 1:
    tHour = (day * 24) + (mon * 30.5 * 24) + (year * 365 * 24)
    tDay = tHour / 24
    tWeek = tDay / 7
    tMon = tDay / 30.5
    print('Your age in hour: {0} \nYour age in day: {1} \nYour age in week: {2} \nYour age in month: {3}'.format(
        tHour, tDay, tWeek, tMon))
