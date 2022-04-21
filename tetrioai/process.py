from PIL import ImageGrab
import pyautogui as pya
import time
import numpy

#make clone array for ai to know what would happen after
#piece is placed wherever

#figure out reward system that prioritizes high scoring clears

#figure out game physics for how pieces would be placed with different rotations

#decide whether to scan for current piece everytime
#or 
#shift next pieces forward then scan for new piece

#make controls for ai and use directInput (ctypes) for input into game





def scan():
    for x in range(10):
        for y in range(20):
            print(f"{x} is x")
            print(f"{y} is y")
            z = ((x*35)+15,700-(y*35)-17.5)
            #pya.moveTo(z[0]+785,z[1]+190)
            print(z)
            px=b.getpixel(z)
            colors.append(px)
            if px!= (0,0,0):
                pb[20-y-1][x]=5
        print(len(colors))
    h=ImageGrab.grab(bbox=(642,237,742,305))
    hcolor=h.getpixel((49,44))
    print(hcolor)
    if hcolor == (16, 146, 208):
        print("held piece is I")
    elif hcolor == (254, 202, 60):
        print("held piece is O")
    elif hcolor == (72, 173, 57):
        print("held piece is S")
    elif hcolor == (255, 124, 31):
        print("held piece is L")
    elif hcolor == (157, 30, 155):
        print("held piece is T")
    elif hcolor == (173, 23, 20):
        print("held piece is Z")
    elif hcolor == (32, 51, 166):
        print("held piece is J")
    for i in range(5):
        ux = 238 + (i*105)
        lx = 308 + (i*105)
        next=ImageGrab.grab(bbox=(1216,ux,1286,lx))
        px=next.getpixel((42,45))
        if px[0] in range(0,15):
            print(f"#{i+1} piece is I")
        elif px[1] in range(220,255):
            print(f"#{i+1} piece is O")
        elif px[1] in range(110,140):
            print(f"#{i+1} piece is L")
        elif px[0] in range(140,165):
            print(f"#{i+1} piece is T")
        elif px[2] in range(15,40):
            print(f"#{i+1} piece is Z")
        elif px[0] in range(20,40):
            print(f"#{i+1} piece is J")
        elif px[0] in range(60,80):
            print(f"#{i+1} piece is S")    
pb=numpy.zeros((20,10))
pya.keyDown("alt")
pya.press("tab")
pya.keyUp("alt")
time.sleep(0.2)
start=time.time()
colors=[]
b=ImageGrab.grab(bbox=(786,190,1135,890))
scan()
h=ImageGrab.grab(bbox=(642,237,742,305))
t=round(time.time()-start,4)
print(f"{t} is the time")
print(pb)
pya.keyDown("alt")
pya.press("tab")
pya.keyUp("alt")