import VideoDetection as VdDetection
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import Email
import ImageDetection as ImgDetect

def send():
    try:
        username = TxtEmailFrom.get()
        password = Txtpassword.get()
        to = TxtEmailTo.get()
        subject = TxtSubject.get()
        body = TxtDescription.get("1.0", 'end-1c')
        if username == "" or to == "" or password == "" :
            notif.config(text="All fields required", fg="white")
            return
        else:
            Email.email(username, password, to, subject, body)
    except:
        notif.config(text="Error sending email", fg="white")

def browseImage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image Flle",
                                     filetypes=(("JPG File", "*.jpg"), ("JPG File", "*.jpg"), ("PNG file", ".png"),
                                                ("All Files", "*.*")))
    ImgDetect.detectImage(fln)
    LabelResultat = Label(window, textvariable=fln, text=fln, fg='white' ,background='black')
    LabelResultat.place(x=500, y=330)
    image1 = Image.open('ImgToSend/img0.jpg')
    image1 = image1.resize((430, 315), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    # Position image
    label1.place(x=400, y=10)

def startVideo():
    VdDetection.detectVideo()

window = Tk()
window.geometry("850x370")
window.title('Object detection')
window.iconbitmap('logo.ico')
window.config(background='black')
lblE1 = Label(window, text="détection d'objet",font=('Calibri', 18),fg='white' ,background='black')
lblE1.place(x=150,y=10)
lblEMailFrom = Label(window, text='Email address',fg='white' ,background='black')
lblEMailFrom.place(x=50,y=50)
TxtEmailFrom = Entry(window)
TxtEmailFrom.place(x=150,y=50, width=170 ,height=20)

lblEpassword = Label(window, text='Password',fg='white' ,background='black')
lblEpassword.place(x=50,y=100)
Txtpassword = Entry(window,show="*")
Txtpassword.place(x=150,y=100, width=170 ,height=20)

lblEMailTo = Label(window, text='Email address To',fg='white' ,background='black')
lblEMailTo.place(x=50,y=150)
TxtEmailTo = Entry(window)
TxtEmailTo.place(x=150,y=150, width=170 ,height=20)
lblSubject = Label(window, text='Subject',fg='white' ,background='black')
lblSubject.place(x=50,y=200)
TxtSubject = Entry(window)
TxtSubject.place(x=150,y=200, width=170 ,height=20)
lblDescription = Label(window, text='Content',fg='white' ,background='black')
lblDescription.place(x=50,y=250)
TxtDescription = Text(window)
TxtDescription.place(x=150,y=250, width=230 ,height=50)
btnSend = Button(window, text='Send', command=send)
btnSend.place(x=70,y=330)
btnVideo = Button(window, text='Start video', command=startVideo)
btnVideo.place(x=150,y=330)
lbl = Label(window)
lbl.place(x=400,y=50)
buttonExit = Button(window, text="Exit" ,command=lambda: exit())
buttonExit.place(x=250,y=330)
button5 = Button(window, text="Browse Image" ,command=browseImage)
button5.place(x=400, y=330)

image0 = Image.open('images/img4.jpg')
image0 = image0.resize((430, 315), Image.ANTIALIAS)
test0 = ImageTk.PhotoImage(image0)

label1 = Label(image=test0)
label1.image = test0
# Position image
label1.place(x=400, y=10)

notif = Label(window, text="",bg='black', font=('Calibri', 12), fg="white")
notif.place(x=150, y=300)
window.mainloop()