# extracting time and date from the below website
# https://www.timeanddate.com/

"""Python Program to Quickly fetch date and time from https://www.timeanddate.com/ and copy it to clipboard"""
from bs4 import BeautifulSoup
import requests
import re
import time
from _datetime import datetime
import pyperclip as pc

def filter_date(date_string):
    Match_string = re.match(f"^(\S*), (\d*) (\D*) (\d*)", date_string)
    week_day = Match_string.group(1)
    date2 = Match_string.group(2)
    month = Match_string.group(3)
    year = Match_string.group(4)
    return week_day, date2, month, year


def filter_time(time_string):
    y_time = re.match('(\d*):(\d*):(\d*)', time_string)
    hr = y_time.group(1)
    minute = y_time.group(2)
    sec = y_time.group(3)
    return hr, minute, sec


if __name__ == '__main__':
    country = 'india'  # input('Enter your country:')
    city = 'kolkata'  # input('Enter your city:')
    # url = 'https://www.timeanddate.com/worldclock/india/kolkata'
    url = f'https://www.timeanddate.com/worldclock/{country}/{city}'
    headers = {"Accept-Language": "en-US,en;q=0.5"}
    r = requests.get(url, headers=headers)
    print(f'Status Code: {r.status_code}')  # permission status code, 200 - allowed, other wise = not allowed
    data = r.content
    soup = BeautifulSoup(data, "html5lib")
    # print(soup.prettify())
    time = soup.find_all('span', {"class": "h1"})[0].text  # gets the current local time from the given website
    print(f'Current local time: {time}')
    date = soup.find_all("span", {"id": "ctdat"})[0].text  # gets the current local date from the given website
    print(f'Current local date: {date}')
    week_day, day, mnth, year = filter_date(date)
    hr, minute, sec = filter_time(time)
    #    print(f'{day},{mnth},{year},{hr},{minute},{sec}')
    week_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']

    for i in months:
        if mnth.lower().startswith(i):
            mnth = months.index(i) + 1
            break
    #    print(f'month={mnth}')
    week_day_no = week_days.index(week_day.lower()) + 1
    time_tuple = (int(year), int(mnth), week_day_no, int(day), int(hr), int(minute), int(sec), 0)
    # just copy the date and time to the clip board
    pc.copy(time + '.0')
    print("Time copied!")
