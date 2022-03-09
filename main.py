import pyautogui as pg
import win32.win32gui as win32gui
import pygetwindow as pgw
import time

def_x = 177

def moveToFront(title):
    for i in pgw.getAllWindows():
        if title.strip() in i.title.strip():
            win32gui.SetForegroundWindow(i._hWnd)

def checkReqWindow(title):
    for i in pg.getAllWindows():
        if i.title==title:
            moveToFront(i.title)
            #print("present")

checkReqWindow("Homepage | ServiceNow - Work - Microsoft​ Edge")
a = pg.locateCenterOnScreen('images/modnewempty0.png', confidence = 0.5)

#print(a.y)
pg.moveTo(def_x, a.y)
pg.click()