"""DATETIME CHALLENGE
The Portland-based company you work for just opened two new branches. One is
in New York City, the other in London. They need a very simple program to find
out if the branches are open or closed. The hours of both branches are 9:00 a.m.
-5:00 p.m. in their own time zone.

1. Using IDLE, create a new file.

2. Import the datetime module and any others to aid in time zone calculations.

3. Create a script that will find out the current times in the Portland HQ and
NYC and London branches. Then, compare that time with each branch's hours to
see if they are open or closed.

4. Print out to the screen the three branches and whether they are open or
closed."""

import datetime as dt
from pytz import timezone
import pytz
from datetime import datetime, time

utc = pytz.utc
utc.zone
'UTC'
#Current time in portland
Now= dt.datetime.now()
#Set timezones
PDXTZ = pytz.timezone('US/Pacific')
NYTZ = pytz.timezone('Us/Eastern')
LNTZ = pytz.timezone('Europe/London')
#Set current time displayed formatting.
Time=Now.strftime("%m/%d %H:%M")

#Setting timezone on each varibale.
PDXTimeRAW = Now.astimezone(PDXTZ)
NYTimeRAW = Now.astimezone(NYTZ)
LNTimeRAW = Now.astimezone(LNTZ)

#Formatting each varibale
PDXTime = PDXTimeRAW.strftime("%H:%M")
NYTime = NYTimeRAW.strftime("%H:%M")
LNTime = LNTimeRAW.strftime("%H:%M")
PDXtoday9am = PDXTimeRAW.replace(hour=9, minute=0, second=0, microsecond=0)
PDXtoday5pm = PDXTimeRAW.replace(hour=17, minute=0, second=0, microsecond=0)
NYtoday9am = NYTimeRAW.replace(hour=9, minute=0, second=0, microsecond=0)
NYtoday5pm = NYTimeRAW.replace(hour=17, minute=0, second=0, microsecond=0)
LNtoday9am = LNTimeRAW.replace(hour=9, minute=0, second=0, microsecond=0)
LNtoday5pm = LNTimeRAW.replace(hour=17, minute=0, second=0, microsecond=0)
def in_between(now, start, end):
    if start<= end:
        return start <= now < end
    else:
        return start <= now or now < end
    
def PDXStatus():
    print("It is currently {} in Portland".format(PDXTime))
    if in_between(PDXTimeRAW, PDXtoday9am, PDXtoday5pm):
        print("Portland is Open")
    else:
        print("Portland is closed.")
def NYStatus():
    print("It is currently {} in New York".format(NYTime))
    if in_between(NYTimeRAW, NYtoday9am, NYtoday5pm):
        print("New York is Open")
    else:
        print("New York is closed.")

def LNStatus():
    print("It is currently {} in London".format(LNTime))
    if in_between(LNTimeRAW, LNtoday9am, LNtoday5pm):
        print("London is Open")
    else:
        print("London is closed.")


if __name__ == "__main__":
    PDXStatus()
    NYStatus()
    LNStatus()
