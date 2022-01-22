from email import message
from tkinter import *
from tkinter import messagebox
from turtle import title
from urllib import response
from tkinter import filedialog
from PIL import ImageTk,Image


root=Tk()
root.title('Image Editor')
root.geometry("1000x1000")

editor_menu = Menu(root)
root.config(menu=editor_menu)
global my_label


def new_command():
    pass
def open_command():
    pass
def save_command():
    s_file = messagebox.askyesno(message="Do you want to save your work?")
    Label(root, text=s_file).pack()
def print_command():
    pass
def resize_command():
    pass
def baw_command():
    pass
def copy_command():
    pass
def cut_command():
    pass
def paste_command():
    pass
def crop_command():
    pass
def copy_command():
    pass
def rleft_command():
    pass
def rright_command():
    pass
def hflip_command():
    pass
def vflip_command():
    pass
def info_command():
    info_label = Label(root, text="This Simple Image Editor is created by Mustafa Lokhandwala")
    info_label.pack()

file_menu = Menu(editor_menu)
editor_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_command)
file_menu.add_separator()
file_menu.add_command(label="Open", command=open_command)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save_command)
file_menu.add_separator()
file_menu.add_command(label="Print", command=print_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)



edit_menu = Menu(editor_menu)
editor_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Resize", command=resize_command)
edit_menu.add_separator()
edit_menu.add_command(label="Black and White", command=baw_command)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=copy_command)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_command)
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=paste_command)
edit_menu.add_separator()
edit_menu.add_command(label="Crop", command=crop_command)
edit_menu.add_separator()
edit_menu.add_command(label="Rotate Left", command=rleft_command)
edit_menu.add_separator()
edit_menu.add_command(label="Rotate Right", command=rright_command)
edit_menu.add_separator()
edit_menu.add_command(label="Horizontal Flip", command=hflip_command)
edit_menu.add_separator()
edit_menu.add_command(label="Vertical Flip", command=vflip_command)
edit_menu.add_separator()

help_menu = Menu(editor_menu)
editor_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About Us", command=info_command)
help_menu.add_separator()




root.mainloop()