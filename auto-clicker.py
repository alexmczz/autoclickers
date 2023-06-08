##!IMPORTANT!! YOU NEED TO PIP INSTALL PYAUTOGUI IN ORDER FOR THIS APP TO WORK!!!

import os
import pyautogui
import time 
from datetime import datetime

def res_inp():
  print("Enter Speed")
  usr_speed = input("> ")
  print("Enter Duration(Seconds are default. Type M for minutes S for seconds)")
  print("Example: M 1 S 30")
  usr_duration = input("> ")

def get_duration():
  res = input("test [string][int] > ")
  if "M" in res:
    times = [res.split()]
    times2 = []
    for char in times[0]:
      times2.append(char)
    #print(f"test 1: {test}")
    #print(f"test 2: {test2}")
    #print(f"test 3: {test2[1]}")
    return int(times2[1])
      #print(test3)


def rate():
  res = input("Enter rate(clicks per second)> ")
  rate_i = int(res)
  return rate_i
  


def clicker():
  duration = get_duration()
  counter = 0
  
  my_rate = rate()
  
  while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    dif_time = current_time + my_rate
    
    if str(current_time) != str(dif_time):
      print(current_time)
      #os.system("clear")
      continue
    else:
      break
    







  
  


#clicker()

