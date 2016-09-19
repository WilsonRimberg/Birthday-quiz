"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
name= input("Hello, what is your name? ")
birthmonth=input("Hi "+name+", what was the name of the month you were born in? ")
birthyear= input("And what year were you born in, "+name+"? ")
birthyear= input("And the day? ")
if birthmonth in ["January", "Febuary", "December"]:
    season="winter"
else:
    if birthmonth in ["March", "April", "May"]:
        season="spring"
    else:
        if birthmonth in ["June", "July", "August"]:
            season="summer"
        else: season="fall"
if int(birthyear)<1980:
    era="stone age"
else:
    if int(birthyear) in [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989]:
        era="eighties"
    else:
        if int(birthyear) in [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]:
            era="nineties"
        else:
            if int(birthyear)>= 2000:
                era="two thousands"
if birthday==31 and birthmonth=="October":
    halloween=yes
if birthmonth=="September":
    birthmonth=9
if birthmonth==
            
