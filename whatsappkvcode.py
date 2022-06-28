import pyautogui as pg
import pywhatkit as kit
import flask
import datetime as datetime
import time
from datetime import date, timedelta

MobileNumber = ["+xxxxxxxxxx","+xxxxxxxxx1","+x2"]


def sendwhatimmkvmsg(nowmobilenumber1):
    WIDTH, HEIGHT = pg.size()
    #kit.sendwhatmsg_instantly(nowmobilenumber1, "Hello")
    today = datetime.datetime.now()
    print(today)
    todayt = today + datetime.timedelta(0,59)
    print(todayt)
    thour=todayt.hour
    ttminute=(todayt.minute)
    waittime=15
    Tabclosetime=20 #20
    kit.sendwhatmsg(nowmobilenumber1,"Dear Sadhaka, Thanks for registering with 'PRAYAS - PRAkriti YogA Samhitha'. Will include you in the session starting Feb 14th 2022. Will send you a message few days before the session - Krishnan V, Yoga Teacher",thour,ttminute,waittime)#,True,Tabclosetime)
    pg.click(WIDTH / 2, HEIGHT / 2)
    pg.press("enter")
                     

def sendwhatkvmsg(nowmobilenumber):
    import pyautogui
    import keyboard as k
    today = datetime.datetime.now()
    print(today)
    todayt = today + datetime.timedelta(0,89)
    print(todayt)
    thour=todayt.hour
    ttminute=(todayt.minute)
    waittime=25
    Tabclosetime=20 #20
    kit.sendwhatmsg(nowmobilenumber,"Dear Sadhaka, Thanks for registering with 'PRAYAS - PRAkriti YogA Samhitha'. Will include you in the session starting Feb 14th 2022. Will send you a message few days before the session - Krishnan V, Yoga Teacher",thour,ttminute,waittime)#,True,Tabclosetime)
    #for i in range(5):
     #   pg.press("tab")
    time.sleep(20)
    pyautogui.click(x=175, y=243)
    pyautogui.press("enter")
    pyautogui.write("cavallona")
    time.sleep(5)
    pyautogui.doubleClick(x=216, y=383)
    pyautogui.click(x=1044, y=688)
    pyautogui.write("Auguri, buon anno!")
    pyautogui.press("enter")
    #pyautogui.press("enter")

for x in MobileNumber:
    sendwhatkvmsg(x)
    #sendwhatimmkvmsg(x)
