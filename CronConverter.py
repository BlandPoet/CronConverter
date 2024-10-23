"""
    Convert a datetime object to a cron expression for PSU. since it only uses cron... UGH
    ref for cron: https://github.com/HangfireIO/Cronos
    Framework of this can be used for the api calls to allow PSU to have correct format for scheduling.
    
    :param dt: datetime object
    :return: cron expression string
"""

from datetime import datetime
#cron format
def datetime_to_cron(dt):
    return f"{dt.minute} {dt.hour} {dt.day} {dt.month} *"

#input section
date_str = input("Enter a date and time (YYYY-MM-DD HH:MM:SS): ") 
try:
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    cron_expression = datetime_to_cron(dt)
    print(f"Cron expression for {date_str} is: {cron_expression}")
except ValueError:
    print("Invalid date format. Please enter the date in the format YYYY-MM-DD HH:MM:SS.")