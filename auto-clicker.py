##!IMPORTANT!! YOU NEED TO PIP INSTALL PYAUTOGUI IN ORDER FOR THIS APP TO WORK!!!


import pyautogui
import time

print("Enter Speed")
usr_speed = input("> ")
print("Enter Duration(Seconds are default. Type M for minutes S for seconds)")
print("Example: M 1 S 30")
usr_duration = input("> ")

def total_time(times):
  if "m" in times:
    times = times.split(" ")
    calculated_time = times[1] 
    return calculated_time * 60
  else:
    return int(times)
  
  
time.sleep(5)
for i in range(int(usr_speed)):
  pyautogui.click()
  time.sleep(total_time(usr_duration))
