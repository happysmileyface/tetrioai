import pyautogui as pya
from PIL import ImageGrab
import numpy
import time
pya.keyDown("alt")
pya.press("tab")
pya.keyUp("alt")
time.sleep(0.5)
x = numpy.zeros((20,10))
for i in range(len(x)):
    x[i] = '_'
print(x)
#
#pya.moveTo(1258,595)
#while True:
#    print(pya.position())
#    time.sleep(1)
#for i in range(5):
    #ux = 238 + (i*105)
    #lx = 308 + (i*105)
    #next=ImageGrab.grab(bbox=(1216,ux,1286,lx))
    #px=next.getpixel((42,45))
    #if px[0] in range(0,15):
        #print(f"#{i+1} piece is I")
    #elif px[1] in range(220,255):
        #print(f"#{i+1} piece is O")
    #elif px[1] in range(110,140):
        #print(f"#{i+1} piece is L")
    #elif px[0] in range(140,165):
        #print(f"#{i+1} piece is T")
    #elif px[2] in range(15,40):
        #print(f"#{i+1} piece is Z")
    #elif px[0] in range(20,40):
        #print(f"#{i+1} piece is J")
    #elif px[0] in range(60,80):
        #print(f"#{i+1} piece is S")
#1258,  [288,393,491,595,703]
#1249-12

#1191,233
#1330,725
#-105
#658  728

#1  (1216,238,1286,308)
#
#2  (1216,343,1286,413)
#
#3  (1216,448,1286,518)
#(255, 122, 30) is L   (70, 171, 55) is S   (8, 172, 228) is I   (153, 26, 153) is T   (29, 51, 160) is J   (182, 25, 28) is Z   (252, 234, 62) is O
#4  (1216,553,1286,623)
#(255, 123, 31) is L   (71, 172, 55) is S   (8, 172, 228) is I  (153, 24, 154) is T  (29, 52, 159) is J   (183, 26, 29) is Z   (252, 235, 63) is O
#5  (1216,658,1286,728)
#(255, 124, 31) is L   (71, 173, 56) is S   (8, 172, 228) is I   (153, 24, 154) is T   (28, 52, 158) is J   (185, 27, 31) is Z   (252, 236, 63) is O     



#pya.keyDown("alt")
#pya.press("tab")
#pya.keyUp("alt")     