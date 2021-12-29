#!/bin/python3
from sense_hat import SenseHat
import time
import datetime

s = SenseHat()
s.low_light = True

"""
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)
pink = (255, 105, 180)
"""


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def displayW(target):
    res = target - datetime.datetime.now()
    seconds = int(res.total_seconds())
    while seconds > 1:
        print(seconds)
        res = target - datetime.datetime.now()
        seconds = int(res.total_seconds())
        years = seconds//31536000
        yearsSecs = years*31536000
        months = (seconds - yearsSecs)//2592000
        monthSecs = months * 2592000
        days = (seconds - yearsSecs - monthSecs) // 86400
        daysSecs = 86400*days
        hours = (seconds - yearsSecs - monthSecs - daysSecs) // 3600
        hoursSecs = hours*3600
        minutes = (seconds - yearsSecs - monthSecs -
                   daysSecs - hoursSecs) // 60
        minutesSecs = minutes*60
        secondsF = seconds - yearsSecs - monthSecs - daysSecs - hoursSecs - minutesSecs
        # display(years, months, days, hours, minutes, seconds, 0, 5)
        if years == 0 and months == 0 and days == 0 and hours == 0 and minutes == 0 and secondsF < 60:
            s.show_message(str(secondsF))
        else:
            display(years, months, days, hours, minutes, secondsF, 1)
        time.sleep(1)
    time.sleep(3)
    s.load_image("fire.png")
    time.sleep(5)
    s.show_message("E ora, i botti napoletani")
    time.sleep(6)


def display(years, months, days, hours, minutes, seconds, mode=0, timeInterval=10):
    # mode 1: display unit only when no bigger unit exists
    # mode 0: alternate
    global s
    yellow = (255, 255, 0)
    pink = (255, 105, 180)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    white = (255, 255, 255)
    nothing = (0, 0, 0)
    arrayList = []
    tArr = []
    for i in range(years):
        tArr.append(yellow)
    if not mode or (mode and years == 0):
        for i in range(months):
            tArr.append(pink)

    if not mode or (mode and months == 0 and years == 0):
        for i in range(days):
            tArr.append(green)

    if not mode or (mode and days == 0 and months == 0 and years == 0):
        for i in range(hours):
            tArr.append(blue)

    if not mode or (mode and hours == 0 and days == 0 and months == 0 and years == 0):
        for i in range(minutes):
            tArr.append(red)

    if not mode or (mode and minutes == 0 and hours == 0 and days == 0 and months == 0 and years == 0):
        for i in range(seconds):
            tArr.append(white)
    arrayList = list(chunks(tArr, 64))
    for i in range(64-len(arrayList[len(arrayList)-1])):
        arrayList[len(arrayList)-1].append(nothing)
    for pixar in arrayList:
        s.set_pixels(pixar)
        if len(arrayList) > 0:
            time.sleep(timeInterval)


target = datetime.datetime.strptime('2022-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
displayW(target)
