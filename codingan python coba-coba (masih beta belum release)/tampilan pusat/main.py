from tkinter import *
from tkinter import messagebox
import requests
import threading
from io import BytesIO
from PIL import Image
from PIL import ImageTk
import time

flagkamera1 = False
flagmasking1 = False

linkrobot1='http://0.0.0.0:5000/'
linkrobot2='http://0.0.0.0:5000/'

def tugaskamera1():
    global flagkamera1
    while flagkamera1:
        time.sleep(0.1)
        try:
            # response = requests.get('http://192.168.1.101:5000/video_feed', stream=False)
            response = requests.get(linkrobot1+'video_feed', stream=False)
            # print(response.content)
            img = Image.open(BytesIO(response.content))
            img = ImageTk.PhotoImage(img)
            gambarkamera1.configure(image=img)
            gambarkamera1.image = img
        except:
            messagebox.showerror("Error", "Kamera robotnya belum nyala")
            flagkamera1 = False

def dapatmask1():
    global flagmasking1
    while flagmasking1:
        time.sleep(0.1)
        try:
            # response = requests.get('http://192.168.1.101:5000/video_feed', stream=False)
            response = requests.get(linkrobot1+'video_mask', stream=False)
            # print(response.content)
            img = Image.open(BytesIO(response.content))
            img = ImageTk.PhotoImage(img)
            gambarmasking1.configure(image=img)
            gambarmasking1.image = img
        except:
            messagebox.showerror("Error", "Kamera robotnya belum nyala")
            flagkamera = False

def berhenti():
    # response = requests.get('http://192.168.1.101:5000/sip')
    response = requests.get(linkrobot1+'berhenti')

def jalan():
    # response = requests.get('http://192.168.1.101:5000/sip')
    response = requests.get(linkrobot1+'jalan')

def enablecamera1():
    global flagkamera1
    flagkamera1=True
    th01 = threading.Thread(target=tugaskamera1)
    th01.daemon = True
    th01.start()


def enablemask1():
    global flagmasking1
    flagmasking1=True
    th01 = threading.Thread(target=dapatmask1)
    th01.daemon = True
    th01.start()

# def kirimhsvbola():
    

def disablecamera1():
    global flagkamera1
    global flagmasking1
    flagkamera1=False
    flagmasking1 = False

def onClose():
    global flagkamera1
    flagkamera1 = False
    flagmasking1 = False
    root.quit()

root = Tk()
frame = Frame(root)
frame.grid(row = 0, column = 0, padx=10, pady=0)

buttonframe1 = Frame(frame)
buttonframe1.grid(row=1, column=2, padx=10, pady=10)

buttonframe2 = Frame(frame)
buttonframe2.grid(row=2, column=2, padx=10, pady=10)

buttonframe3 = Frame(root)
buttonframe3.grid(row = 0, column = 1, padx=10, pady=0)

kamera1button = Button(buttonframe1, text="Buka Kamera 1", command = enablecamera1)
kamera1button.grid(row = 0, column = 0, padx=10, pady=2)

mask1button = Button(buttonframe1, text="Tampilkan mask 1", command = enablemask1)
mask1button.grid(row = 0, column = 1, padx=10, pady=2)

kamera2button = Button(buttonframe2, text="Buka Kamera 2")
kamera2button.grid(row = 1, column = 0, padx=10, pady=2)

mulaibutton = Button(buttonframe3, text="Robot Jalan", command = jalan)
mulaibutton.grid(row = 0, column = 0, padx=10, pady=2)

stopbutton = Button(buttonframe3, text="Robot berhenti", command = berhenti)
stopbutton.grid(row = 1, column = 0, padx=10, pady=10)

# print(requests.get('http://0.0.0.0:5000/video_feed', stream=True).raw)

labelteks = Label(frame)
labelteks.config(text="gambar kamera")
labelteks.grid(row=0, column=0, padx=5, pady=5)

labelteks1 = Label(frame)
labelteks1.config(text="gambar masking")
labelteks1.grid(row=0, column=1, padx=5, pady=5)

gambarkamera1 = Label(frame)
gambarkamera1.config(width=320 ,height=240)
gambarkamera1.config(background = "white", )
gambarkamera1.config(image=ImageTk.PhotoImage(Image.open("5be55-white-mk630n.jpg")))
gambarkamera1.grid(row=1, column=0, padx=5, pady=5)

gambarmasking1 = Label(frame)
gambarmasking1.config(width=320 ,height=240)
gambarmasking1.config(background = "white", )
gambarmasking1.config(image=ImageTk.PhotoImage(Image.open("5be55-white-mk630n.jpg")))
gambarmasking1.grid(row=1, column=1 , padx=5, pady=5)

gambarkamera2 = Label(frame)
gambarkamera2.config(width=320 ,height=240)
gambarkamera2.config(background = "white", )
gambarkamera2.config(image=ImageTk.PhotoImage(Image.open("5be55-white-mk630n.jpg")))
gambarkamera2.grid(row=2, column=0, padx=5, pady=5)

gambarmasking2 = Label(frame)
gambarmasking2.config(width=320 ,height=240)
gambarmasking2.config(background = "white", )
gambarmasking2.config(image=ImageTk.PhotoImage(Image.open("5be55-white-mk630n.jpg")))
gambarmasking2.grid(row=2, column=1 , padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW", onClose)

root.mainloop()