from tkinter import *
import datetime
import time
import winsound


tick = Tk()
tick.title("Alarm TKinter")
tick.geometry("600x300")

def alarm(set_time_to):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print("Next Alarm at:",set_time_to+";***","Time Now",now)
        if now == set_time_to:
            print("Wakey wakey")
            winsound.Beep(1000,1000)
            break

def alarm_time():
    set_time_to = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_time_to)

time_format=Label(tick, text= "Enter in 24Hrs format", fg="black",bg="yellow",font="Arial").place(x=0,y=0)
setYourAlarm = Label(tick,text = "Set the Alarm to",fg="blue",bg = "magenta",font="Arial").place(x=0, y=60)
addTime = Label(tick,text = "Hours        Mins       Secs(Enter Zero at least)",font=80).place(x = 120,y=35)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(tick,textvariable = hour,width = 90).place(x=120,y=60)
minTime= Entry(tick,textvariable = min,width = 90).place(x=180,y=60)
secTime = Entry(tick,textvariable = sec,width = 90).place(x=240,y=60)

set_alarm = Button(tick,text = "Set Alarm",fg="red",width = 10,command = alarm_time).place(x =110,y=90)

tick.mainloop()
