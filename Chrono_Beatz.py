# import libraries from tkinter
from tkinter import *
from tkinter.ttk import *
import datetime
import time
import platform
import math
import pygame
from tkinter import filedialog

# initialize Pygame Mixer
pygame.mixer.init()

# create tkinter GUI
chronobeatz = Tk()
chronobeatz.title("CHRONO BEATZ")
chronobeatz.geometry("350x400")
chronobeatz.resizable(0,0)

# create function to control the clock time and date
def clock():
    date_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M/%p")
    date,time1 = date_time.split()
    time2,time3 = time1.split('/')
    hour,minutes = time2.split(':')
    if int(hour) > 12 and int(hour) < 24:
        time = str(int(hour) - 12) + ':' + minutes + ' ' + time3
    else:
        time = time2 + ' ' + time3
    time_label.config(text = time)
    date_label.config(text = date)
    time_label.after(1000, clock)
# create function to control button that lets user add mp3 files
def add_song():
        song = filedialog.askopenfilename(initialdir='', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))
        alarm_box.insert(END, song)
# create function to control the alarm execution
def alarm():
        main_time = datetime.datetime.now().strftime("%H:%M %p")
        alarm_time = get_alarm_time_entry.get()
        alarm_time1,alarm_time2 = alarm_time.split(' ')
        alarm_hour, alarm_minutes = alarm_time1.split(':')
        main_time1,main_time2 = main_time.split(' ')
        main_hour1, main_minutes = main_time1.split(':')
        if int(main_hour1) > 12 and int(main_hour1) < 24:
                main_hour = str(int(main_hour1) - 12)
        else:
                main_hour = main_hour1
        if int(alarm_hour) == int(main_hour) and int(alarm_minutes) == int(main_minutes) and main_time2 == alarm_time2:
                for i in range(3):
                        alarm_status_label.config(text='Time Is Up')
                        song = alarm_box.get(ACTIVE)
                        pygame.mixer.music.load(song)
                        pygame.mixer.music.play(loops=0)
                get_alarm_time_entry.config(state='enabled')
                set_alarm_button.config(state='enabled')
                get_alarm_time_entry.delete(0,END)
                alarm_status_label.config(text = '')
        else:
                alarm_status_label.config(text='Alarm Has Been Set')
                get_alarm_time_entry.config(state='disabled')
                set_alarm_button.config(state='disabled')
        alarm_status_label.after(1000, alarm)
# create function to stop audio player
def stop():
        pygame.mixer.music.stop()
# create function to reset alarm settings
def reset():
    get_alarm_time_entry.config(state='enabled')
    set_alarm_button.config(state='enabled')
    get_alarm_time_entry.delete(0,END)
    alarm_status_label.config(text = '')
    
# loop to add weight for empty rows using grid method for cosmetic purposes
rows = 0
while rows < 50:
    chronobeatz.rowconfigure(rows, weight=2)
    chronobeatz.columnconfigure(rows, weight=2)
    rows += 1
# clock display settings
time_label = Label(chronobeatz, font= "tahoma 30 bold")
time_label.grid(row = 0, column = 0, columnspan = 2)
# date display settings
date_label = Label(chronobeatz, font = 'tahoma 20 bold')
date_label.grid(row = 2, column = 0, columnspan = 2)
# display settings for box containing Alarm mp3 files
alarm_box = Listbox(chronobeatz, background="black", foreground="white", width=60, height=5)
alarm_box.grid(row = 5, column = 0, columnspan = 2)
# display settings for Add mp3 file button
get_alarm_song_button = Button(chronobeatz, text = 'Add mp3 file', command=add_song)
get_alarm_song_button.grid(row = 6, column = 0, columnspan = 2)
# display settings for Instructions for using box containing Alarm mp3 files
set_song_instructions_label = Label(chronobeatz, font = 'calibri 10 bold', text = "Click on desired song to set as active alarm")
set_song_instructions_label.grid(row = 7, column = 0, columnspan = 2)
# display settings for user input box for setting alarm time
get_alarm_time_entry = Entry(chronobeatz, font = 'calibri 15 bold')
get_alarm_time_entry.grid(row = 10, column = 0, columnspan = 2)
# display settings for instructions regarding format of user input
alarm_instructions_label = Label(chronobeatz, font = 'calibri 10 bold', text = "Enter Alarm Time in 12 hour format + AM/PM = 08:00 PM")
alarm_instructions_label.grid(row = 11, column = 0, columnspan = 2)
# display settings for Set Alarm button
set_alarm_button = Button(chronobeatz, text = "Set Alarm", command=alarm)
set_alarm_button.grid(row = 13, column = 0, sticky = "E")
# display settings for Silence Alarm button
stop_alarm_button = Button(chronobeatz, text = "Silence Alarm", command=stop)
stop_alarm_button.grid(row = 13, column = 1, sticky = "W")
# display settings for Reset Alarm button
reset_alarm_button = Button(chronobeatz, text = "Reset Alarm", command=reset)
reset_alarm_button.grid(row = 14, column = 0, sticky = "E")
# display settings for user alert message regarding alarm set status
alarm_status_label = Label(chronobeatz, font = 'calibri 15 bold')
alarm_status_label.grid(row = 15, column = 0, columnspan = 2)
# call clock function
clock()
chronobeatz.mainloop()
