import time
import os

def countdown(time_sec):
    os.system('clear') 

    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
        os.system('clear') 

    print("stop")

countdown(40)