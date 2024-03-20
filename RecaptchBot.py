import pyautogui
import time
import webbrowser
import random
import math

webbrowser.open("https://patrickhlauke.github.io/recaptcha/")

x_ax = 1920 #Change this to your screens dimensions
y_ax = 1080 #Change this to your screens dimensions

x_center = x_ax/2
y_center = y_ax/2

pyautogui.moveTo(x=x_center,y=y_center, duration=0.0000000001)
time.sleep(1)

def draw_semi_circle(radius):
    start_x, start_y = pyautogui.position()
    step = 5  
    for angle in range(90, -1, -step):
        speed_1 = round(random.uniform(0.001,0.12),4)
        x = start_x + int(radius * math.cos(math.radians(angle)))
        y = start_y + int(radius * math.sin(math.radians(angle)))
        if angle != 90:
            pyautogui.moveTo(x, y, duration=speed_1)
        else:
            pyautogui.moveTo(x, y)

radius = 212

def draw_semi_circle_counter(radius):
    start_x, start_y = pyautogui.position()
    step = 5  
    for angle in range(1 ,90 , step):
        speed_2 = round(random.uniform(0.001,0.12),4)
        x = start_x + int(radius * math.cos(math.radians(angle)))
        y = start_y + int(radius * math.sin(math.radians(angle)))
        if angle != 90:
            pyautogui.moveTo(x, y, duration=speed_2)
        else:
            pyautogui.moveTo(x, y)
radius = 58

def HumanMovement():
    count = 0
    increment_x = 0
    increment_y = 2
    for i in range(5):
        y_rand = random.randint(10,y_ax-300)
        x_rand = random.randint(10,x_ax-400)
        pyautogui.moveTo(x=x_rand,y=y_rand,duration=round(random.uniform(0.001,1.293),4))
        for i in range(1):
            draw_semi_circle(radius)
            draw_semi_circle_counter(radius)
    pyautogui.moveTo(x=x_center+312,y=y_center+212, duration=round(random.uniform(0.001,1.293),4))
    pyautogui.moveTo(x=x_center,y=y_center, duration=round(random.uniform(0.001,0.321),4))

    return(HumanMovement)
HumanMovement()
