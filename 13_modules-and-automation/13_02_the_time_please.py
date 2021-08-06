# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

import datetime

current = datetime.datetime.now()
print(current.strftime("%H:%M %d/%m/%y"))

# 24 hour clock, day/month/year.  Everything else is trash, fight me.