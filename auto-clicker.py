##!IMPORTANT!! YOU NEED TO PIP INSTALL PYAUTOGUI IN ORDER FOR THIS APP TO WORK!!!


import pyautogui
import time


def res_inp():
  print("Enter Speed")
  usr_speed = input("> ")
  print("Enter Duration(Seconds are default. Type M for minutes S for seconds)")
  print("Example: M 1 S 30")
  usr_duration = input("> ")

def get_time():
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




def clicker():
  duration = get_time()
  counter = 0
  for i in range(duration):
     
     while counter <= duration:
      counter += 1
      pyautogui.click()
      #print(f"click: {counter}")
    





clicker()