import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import time
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

for file in os.listdir('shared_files'):
    filename = os.fsdecode(file)
    listbox.insert(song_counter, filename)
    song_counter = song_counter + 1

def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: " + song_selected)
    else:
        infoLabel.configure(text = "")

playBtn = Button(window, text="Play", width=10, bg='SkyBlue', font=("Calibri", 10), command = play)
playBtn.place(x=30,y=200)

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/' + song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

def resume():
    global song_selected
    mixer.init()
    mixer.music.load("shared_files/" + song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame 
    mixer.init()
    mixer.music.load("shared_files/" + song_selected)
    mixer.music.pause()

stop = btn(window, text="Stop", bd=1, width=10, bg="SkyBlue", font=("Calibri", 10), command = stop)
stop.place(x=200,y=200)

ResumeBtn = Button(window, text="Resume", width=10, bd=1, bg="SkyBlue", font=("Calibri",10), command = resume)
ResumeBtn.place(x=30,y=250)

PauseBtn = Button(window, text="Pause", width=10, bd="SkyBlue", font=("Calibri",10), command = pause)
PauseBtn.place(x=200,y=250)

