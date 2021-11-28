from time import time
from tkinter import *
import datetime
import threading
from plyer import notification

alarms = dict()


def currenttime():
    while True:
        currenttime = datetime.datetime.now()
        now = currenttime.strftime("%H:%M:%S")
        for i in alarms:
            if now == alarms[i]:
                notification.notify(
                    title=i,
                    message=alarms[i],
                    timeout=10
                )
                break


def addalarm():
    alarms[AlarmName.get()] = AlarmTime.get()
    print(alarms)


if __name__ == "__main__":
    root = Tk()
    root.geometry("600x600")
    changetime = threading.Thread(target=currenttime)
    changetime.start()

    # variables
    NameVar = StringVar()
    TimeVar = StringVar()

    AlarmName = Entry(root, textvariable=NameVar)
    AlarmTime = Entry(root, textvariable=TimeVar)

    AlarmName.pack(side=TOP, pady=10)
    AlarmTime.pack(side=TOP, pady=10)
    AddButton = Button(root, text="Add alarm", command=addalarm)
    AddButton.pack(side=TOP, pady=10)

    root.mainloop()
