from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END, Toplevel

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Thanushan\Downloads\Sign Up GUI Python\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("838x546")
window.configure(bg = "#6720E0")

canvas = Canvas(
    window,
    bg = "#6720E0",
    height = 546,
    width = 838,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    419.5,
    221.0,
    image=entry_image_1
)

# Define a function to insert the placeholder text if the entry field is empty
def add_placeholder_text(event):
    if not entry_1.get():
        entry_1.insert(0, "Full Name")

# Define a function to remove the placeholder text if it is present
def remove_placeholder_text(event):
    if entry_1.get() == "Full Name":
        entry_1.delete(0, END)

# Define the entry field with a white background and black text
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)

# Insert a placeholder text into the entry field
entry_1.insert(0, "Full Name")

# Bind the remove_placeholder_text function to the <FocusIn> event of the entry field
entry_1.bind("<FocusIn>", remove_placeholder_text)

# Bind the add_placeholder_text function to the <FocusOut> event of the entry field
entry_1.bind("<FocusOut>", add_placeholder_text)

# Place the entry field on the canvas at position (289, 198) with a width of 261 and a height of 44
entry_1.place(
    x=289.0,
    y=198.0,
    width=261.0,
    height=44.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    419.5,
    284.0,
    image=entry_image_2
)

# Define a function to insert the placeholder text if the entry field is empty
def add_placeholder_text(event):
    if not entry_2.get():
        entry_2.insert(0, "Email")

# Define a function to remove the placeholder text if it is present
def remove_placeholder_text(event):
    if entry_2.get() == "Email":
        entry_2.delete(0, END)

entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)

# Insert a placeholder text into the entry field
entry_2.insert(0, "Email")

# Bind the remove_placeholder_text function to the <FocusIn> event of the entry field
entry_2.bind("<FocusIn>", remove_placeholder_text)

# Bind the add_placeholder_text function to the <FocusOut> event of the entry field
entry_2.bind("<FocusOut>", add_placeholder_text)

entry_2.place(
    x=289.0,
    y=261.0,
    width=261.0,
    height=44.0
)

canvas.create_text(
    279.0,
    176.0,
    anchor="nw",
    text="Sign up to receive product updates about MW.",
    fill="#FFFFFF",
    font=("Inter Regular", 11 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    346.5,
    376.0,
    image=entry_image_3
)

# Define a function to insert the placeholder text if the entry field is empty
def add_placeholder_text(event):
    if not entry_3.get():
        entry_3.insert(0, "From")

# Define a function to remove the placeholder text if it is present
def remove_placeholder_text(event):
    if entry_3.get() == "From":
        entry_3.delete(0, END)

entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)

# Insert a placeholder text into the entry field
entry_3.insert(0, "From")

# Bind the remove_placeholder_text function to the <FocusIn> event of the entry field
entry_3.bind("<FocusIn>", remove_placeholder_text)

# Bind the add_placeholder_text function to the <FocusOut> event of the entry field
entry_3.bind("<FocusOut>", add_placeholder_text)

entry_3.place(
    x=289.0,
    y=353.0,
    width=115.0,
    height=44.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    492.5,
    376.0,
    image=entry_image_4
)

# Define a function to insert the placeholder text if the entry field is empty
def add_placeholder_text(event):
    if not entry_4.get():
        entry_4.insert(0, "To")

# Define a function to remove the placeholder text if it is present
def remove_placeholder_text(event):
    if entry_4.get() == "To":
        entry_4.delete(0, END)

entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)

# Insert a placeholder text into the entry field
entry_4.insert(0, "To")

# Bind the remove_placeholder_text function to the <FocusIn> event of the entry field
entry_4.bind("<FocusIn>", remove_placeholder_text)

# Bind the add_placeholder_text function to the <FocusOut> event of the entry field
entry_4.bind("<FocusOut>", add_placeholder_text)

entry_4.place(
    x=435.0,
    y=353.0,
    width=115.0,
    height=44.0
)

canvas.create_text(
    279.0,
    336.0,
    anchor="nw",
    text="I want to send money",
    fill="#FFFFFF",
    font=("Inter Regular", 11 * -1)
)

def create_popup():
    # create a new window
    popup_window = Toplevel()
    popup_window.title("Pop-up Window")

    # set the size and position of the pop-up window
    popup_window.geometry("400x100+500+300")

    # set the background color of the pop-up window
    popup_window.configure(bg='#6720E0')

    # add a label widget to the popup_window
    label = Label(popup_window, text="Please check your email for further instructions.", anchor="center", bg='#6720E0' ,fg="white", font=("Inter Regular", 10))
    label.pack(fill=BOTH, expand=1, padx=0, pady=0)

def on_entry_change(event):
    if entry_1.get() and entry_2.get() and entry_3.get() and entry_4.get():
        button_1.config(state="normal")
    else:
        button_1.config(state="disabled")
    print("Text fields changed!")  # For debugging purposes

# your existing code for creating the button
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=create_popup,  # open the pop-up window when the button is clicked
    relief="flat",
    cursor="hand2"
)

button_1.place(
    x=342.0,
    y=428.0,
    width=154.0,
    height=48.0
)

canvas.update()
canvas_width = canvas.winfo_width()
canvas.create_text(
    canvas_width/2,
    100.0,
    anchor="center",
    text="Be one of the first.",
    fill="#FFFFFF",
    font=("Inter", 64 * -1, "bold")
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png")
    )
    
image_1 = canvas.create_image(
    184.0,
    422.0,
    image=image_image_1
)

window.resizable(False, False)
window.mainloop()
