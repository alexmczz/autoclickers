##!IMPORTANT!! YOU NEED TO PIP INSTALL PYAUTOGUI IN ORDER FOR THIS APP TO WORK!!!

import pyautogui
from datetime import datetime



class Clicker:
  
  def __init__(self, name=None):
    self.name = name
  #menu
  def help_menu():
    print("Enter Speed start with number then per S for seconds M for minutes H for hours")
    print("Example: > 90PM   90 clicks Per Minute")
    print("Enter Duration(Seconds are default. Type M for minutes S for seconds)")
    print("Example: > M 1 S 30")
    

  #def get_duration():
  #  res = input("test [string][int] > ")
  #  if "M" in res:
  #    times = [res.split()]
  #    times2 = []
  #    for char in times[0]:
  #      times2.append(char)
  #    #print(f"test 1: {test}")
  #    #print(f"test 2: {test2}")
  #    #print(f"test 3: {test2[1]}")
  #    return int(times2[1])
        #print(test3)


  def rate():
    res = input("Enter rate(clicks per second)> ")
    rate_i = int(res)
    return rate_i
    


  def clicker():
    duration = input("enter duration: ")
    duration = int(duration)
    counter = 0
    
    my_rate = Clicker.rate()
    while True:
      now = datetime.now()
      current_time = now.strftime("%H:%M:%S")
      
      current_time1 = current_time.split(":")
      test1=[char for char in current_time1]
      minutes = test1[1]
      minutesPF = int(minutes) + duration
      print(minutes)
      print(minutesPF)

      #if str(current_time) != str(dif_time):
        #print(current_time)
        #os.system("clear")
        #pyautogui.click()
        #continue
      #else:
       # break

Clicker.clicker()

