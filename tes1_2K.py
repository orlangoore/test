
import urllib
import cv2
from mss.linux import MSS as mss
import PIL
import time
import pyautogui
import imutils
import mss
import numpy
import pyautogui
import random
import os
import sys
import threading
import keyboard as kb
import random
import pynput
from pynput.mouse import Controller
from pynput import keyboard
from tkinter import *

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)

def quit():
   root.destroy()
   sys.exit()



primanka = "img\\primanka.png"
chervi = "img\\chervi.png"
poplavok = "img\\poplavok2.png"
udochka1 = "img\\lvl1.png"
udochka2 = "img\\lvl2.png"
udochka3 = "img\\mk3.png"
lopata = "img\\lopata.png"
kopat_chervei = "img\\kopat_chervei.png"
keyboardd = keyboard.Controller()
mouse = Controller()

dolgota = 0
test_item1 = 0




   

color_yellow = (0,255,255)


nazhivka = ""
udochka = ""
monitor_width, monitor_height = pyautogui.size()






def klick():
    monitor_width, monitor_height = pyautogui.size()
    mouse.position = (random.uniform(int(monitor_width/3+600),int(monitor_width/2+600)),random.uniform(int(monitor_height/3),int(monitor_height/2)))
    mouse.click(pynput.mouse.Button.left,1)
    time.sleep(random.uniform(0.06,0.075))



def zakinut():
    stop()
    
    monitor_width, monitor_height = pyautogui.size()
    mouse.position = (random.uniform(int(monitor_width/3),int(monitor_width/2+400)),random.uniform(int(monitor_height/3+400),int(monitor_height/2)))
    mouse.click(pynput.mouse.Button.left,random.randint(1,2))
    time.sleep(random.uniform(0.1,0.3))
    stop()
    keyboardd.press("i")
    time.sleep(random.uniform(0.1,0.15))
    keyboardd.release("i")
    stop()
    time.sleep(random.uniform(1.5,1.7))
    stop()
    try:
       pyautogui.click(udochka)
    except:
       pass
    time.sleep(random.uniform(0.2,0.6))
    stop()
    pyautogui.click(nazhivka)
    time.sleep(random.uniform(0.2,0.6))
    stop()
    mouse.click(pynput.mouse.Button.left,random.randint(1,2))
    time.sleep(random.uniform(0.2,0.8))
    mouse.click(pynput.mouse.Button.left,random.randint(1,2))
    time.sleep(random.uniform(0.2,0.6))
    stop()


def kopat():
    root.destroy()
    while True:
       stop()
       monitor_width, monitor_height = pyautogui.size()
       mouse.position = (random.uniform(int(monitor_width/3+600),int(monitor_width/2+600)),random.uniform(int(monitor_height/3),int(monitor_height/2)))
       mouse.click(pynput.mouse.Button.left,random.randint(1,2))
       time.sleep(random.uniform(0.1,0.3))
       stop()
       keyboardd.press("i")
       time.sleep(random.uniform(0.1,0.15))
       keyboardd.release("i")
       stop()
       time.sleep(random.uniform(1.2,1.5))
       stop()
       pyautogui.click("img\\lopata.png")
       time.sleep(random.uniform(0.2,0.6))
       stop()
       pyautogui.click(kopat_chervei)
       time.sleep(random.uniform(0.2,0.6))
       stop()
       mouse.click(pynput.mouse.Button.left,random.randint(1,2))
       time.sleep(random.uniform(0.2,0.8))
       mouse.click(pynput.mouse.Button.left,random.randint(1,2))
       time.sleep(random.uniform(0.2,0.6))
       stop()
       time.sleep(random.uniform(13.5,15.5))



                     



def process_image(original_image):

    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image


def zakinutt():
    if kb.is_pressed('e') == True:
        zakinut()

def stop():
    if kb.is_pressed('q') == True:
        print('You Pressed A Key!')
        sys.exit()



def check_date(): #ДОДЕЛАТЬ !!!   (0+1)месяц (0+6)день
    res = urllib.request.urlopen('http://just-the-time.appspot.com/')
    result = str(res.read().strip())
    date_list_result= []
    date_list = []
    for i in result:
        if i == 'b':
            pass
        elif i == "'":
            pass
        else:
            date_list.append(i)
    month = str(date_list[5])+str(date_list[6])
    day = str(date_list[8])+str(date_list[9])
    print(date_list)
    if int(month) >0 and int(day) >=11:
        print("Gone")
        sys.exit()
    elif int(month) >=1 and int(day) >=11:    
        print("Gone")
        sys.exit()
    elif int(month) >=2 and int(day) >=0:    
        print("Gone")
        sys.exit()
    





def ss_more():
    while True:
       stop()

       global dolgota
       global vremja
       op = 1
       ob = 1
       vremja = 1
       with mss.mss() as sct:
           monitor_width, monitor_height = pyautogui.size()
           monitor = {"top": 0, "left": 0, "width": monitor_width+100, "height": monitor_height+100}

           while "Screen capturing":
               if kb.is_pressed('q') == True:
                   print('You Pressed A Key!')
                   sys.exit()
               elif kb.is_pressed('e') == True:
                   print('Zakidivaju!')
                   zakinut()
               else:
                   last_time = time.time()

                   img = numpy.array(sct.grab(monitor))
                   template = cv2.imread(poplavok, cv2.IMREAD_GRAYSCALE)
                   w, h = template.shape[::-1]

                   gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                   res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
                   threshold = .8
                   loc = numpy.where(res >= threshold)
                   op += 1
                   ob +=1
                   zakinutt()
                   print (op)
                   for pt in zip(*loc[::-1]):  # Switch collumns and rows
                       cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                       barada = cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                       dolgota = len(barada)
                       dolgota1 = len(barada)
                       stop()
               if dolgota:
                   vremja = op
                   print("vremja= ", vremja)
                   if dolgota1 ==0:
                       dolgota =0
                   else:
                       stop()
                       while dolgota1:
                           stop()
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0




                          
               elif op-vremja>8 and op - vremja<10:
                   zakinut()
                   dolgota = 0
                   dolgota1 = 0

def ss_ozero():
    while True:
       stop()

       global dolgota
       global vremja
       op = 1
       ob = 1
       vremja = 1
       with mss.mss() as sct:
           monitor_width, monitor_height = pyautogui.size()
           monitor = {"top": 0, "left": 0, "width": monitor_width, "height": monitor_height}

           while "Screen capturing":
               if kb.is_pressed('q') == True:
                   print('You Pressed A Key!')
                   sys.exit()
               elif kb.is_pressed('e') == True:
                   print('Zakidivaju!')
                   zakinut()
               else:
                   last_time = time.time()

                   img = numpy.array(sct.grab(monitor))
                   template = cv2.imread(poplavok, cv2.IMREAD_GRAYSCALE)
                   w, h = template.shape[::-1]

                   gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                   res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
                   threshold = .8
                   loc = numpy.where(res >= threshold)
                   op += 1
                   ob +=1
                   print (op)
                   for pt in zip(*loc[::-1]):  # Switch collumns and rows
                       cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                       barada = cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                       dolgota = len(barada)
                       dolgota1 = len(barada)
                       stop()
               if dolgota:
                   vremja = op
                   print("vremja= ", vremja)
                   if dolgota1 ==0:
                       dolgota =0
                   else:
                       stop()
                       while dolgota1:
                           stop()
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0
                           klick()
                           dolgota1 = 0




                          
               elif op-vremja>8 and op - vremja<10:
                   zakinut()
                   dolgota = 0
                   dolgota1 = 0
                    

root = Tk()
lng = Checkbar(root, ['LvL-1', 'LvL-2', 'MK-2'])
tgl = Checkbar(root, ['На червя','На приманку'])



lng.pack(side=TOP,  fill=X)
tgl.pack(side=LEFT)
lng.config(relief=GROOVE, bd=2)

def start_bot_ozero():
   while True:
      global udochka
      global udochka1
      global udochka2
      global udochka3
      global nazhivka
      global primanka
      global chervi
      vibor_udo4ki = list(lng.state())
      vibor_nazhivki = list(tgl.state())
      if vibor_udo4ki[0] == 1 and vibor_nazhivki[0] == 1:
         udochka = udochka1
         nazhivka = chervi
      elif vibor_udo4ki[0] == 1 and vibor_nazhivki[1] == 1:
         udochka = udochka1
         nazhivka = primanka
      elif vibor_udo4ki[1] == 1 and vibor_nazhivki[0] == 1:
         udochka = udochka2
         nazhivka = chervi
      elif vibor_udo4ki[1] == 1 and vibor_nazhivki[1] == 1:
         udochka = udochka2
         nazhivka = primanka
      elif vibor_udo4ki[2] == 1 and vibor_nazhivki[0] == 1:
         udochka = udochka3
         nazhivka = chervi
      elif vibor_udo4ki[2] == 1 and vibor_nazhivki[1] == 1:
         udochka = udochka3
         nazhivka = primanka
      else:
         udochka = udochka3
         nazhivka = primanka         
      root.destroy()
      check_date()
      ss_ozero()
      
def start_bot_more():
   while True:
      global udochka
      global udochka1
      global udochka2
      global udochka3
      global nazhivka
      global primanka
      global chervi
      vibor_udo4ki = list(lng.state())
      vibor_nazhivki = list(tgl.state())
      if vibor_udo4ki[0] == 1 and vibor_nazhivki[0] == 1:
         udochka = udochka1
         nazhivka = chervi
      elif vibor_udo4ki[0] == 1 and vibor_nazhivki[1] == 1:
         udochka = udochka1
         nazhivka = primanka
      elif vibor_udo4ki[1] == 1 and vibor_nazhivki[0] == 1:
         udochka = udochka2
         nazhivka = chervi
      elif vibor_udo4ki[1] == 1 and vibor_nazhivki[1] == 1:
         udochka = udochka2
         nazhivka = primanka
      elif vibor_udo4ki[2] == 1 and vibor_nazhivki[0] == 1:
         udochka = udochka3
         nazhivka = chervi
      elif vibor_udo4ki[2] == 1 and vibor_nazhivki[1] == 1:
         udochka = udochka3
         nazhivka = primanka
      else:
         udochka = udochka3
         nazhivka = primanka         
      root.destroy()
      ss_more()
      





    
Button(root, text='Выйти', command=quit).pack(side=RIGHT)
Button(root, text='Море', command=start_bot_more).pack(side=RIGHT)
Button(root, text='Озеро', command=start_bot_ozero).pack(side=RIGHT)
Button(root, text='Копать\nЧервей', command=kopat).pack(side=RIGHT)
root.mainloop()




                    






                    


 


                    






