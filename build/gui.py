
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("901x528")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 528,
    width = 901,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    504.0,
    0.0,
    901.0,
    528.0,
    fill="#E5E3FF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    703.0,
    333.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_1.place(
    x=568.0,
    y=313.0,
    width=270.0,
    height=39.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    703.0,
    210.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_2.place(
    x=568.0,
    y=190.0,
    width=270.0,
    height=39.0
)

canvas.create_text(
    558.0,
    159.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    561.0,
    275.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 13 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=611.0,
    y=437.0,
    width=184.0,
    height=48.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    703.0,
    39.0,
    image=image_image_1
)

canvas.create_text(
    665.0,
    73.0,
    anchor="nw",
    text="Music for you",
    fill="#777777",
    font=("Sansation Regular", 12 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    250.0,
    253.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=873.0,
    y=5.0,
    width=25.0,
    height=22.0
)
window.resizable(False, False)
window.mainloop()
