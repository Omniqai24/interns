import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

root=Tk()
root.title("Music Player")

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

playlist=Listbox(root,selectmode=MULTIPLE,bg="gold",fg="Black",font=('arial',9),width=35)
playlist.grid(columnspan=5)

os.chdir(r'D:\songs')
songs=os.listdir()

for i in songs:
    playlist.insert(END,i)

playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('arial',10),bg="silver",fg="brown",padx=8,pady=8)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',10),bg="silver",fg="brown",padx=8,pady=8)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',10),bg="silver",fg="brown",padx=8,pady=8)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',10),bg="silver",fg="brown",padx=8,pady=8)
Resumebtn.grid(row=1,column=3)

mainloop()
