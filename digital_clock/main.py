import tkinter
import time


def update(time_display_label, date_display_label, window):
    time_display_label.config(text=time.strftime("%H:%M:%S"))
    date_display_label.config(text=time.strftime("%a, %d %b %Y"))
    window.after(1000, update, time_display_label, date_display_label, window)


def main():
    window = tkinter.Tk()
    window.title("Clock")

    # https://freeicons.io/regular-life-icons/clock-icon-17785#
    icon_photo = tkinter.PhotoImage(file='images/clock.png')
    window.iconphoto(True, icon_photo)

    time_display_label = tkinter.Label(
        master=window,
        font=("Arial", 50),
        fg='red',
        bg='black',
        padx=20
    )
    time_display_label.pack()

    date_display_label = tkinter.Label(
        master=window,
        font=("Ink Free", 20)
    )
    date_display_label.pack()

    update(time_display_label, date_display_label, window)

    window.mainloop()


if __name__ == '__main__':
    main()
