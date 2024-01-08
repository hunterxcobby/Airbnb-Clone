#!/usr/bin/python3

from datetime import datetime, date, time

current_time = datetime.now()

# print(current_time)


# format time

formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_time)

