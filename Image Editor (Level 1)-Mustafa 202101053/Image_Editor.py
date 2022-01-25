from email import message
from email.mime import image
from email.policy import default
from queue import Full
from tkinter import *
from tkinter import messagebox
from turtle import title
from urllib import response
from tkinter import filedialog
from PIL import ImageTk,Image,ImageEnhance,ImageFilter
import cv2


root=Tk()
root.title('Image Editor')
root.iconbitmap('C:\\Users\\lokha\\Python Practice\\Image Editor (level 1)-Mustafa 202101053\\ICON.ico')
root.geometry("1000x700")

editor_menu = Menu(root)
root.config(menu=editor_menu)



global new_image,img,x




canvas= Canvas(root, width=700, height=500)
canvas.pack(padx=500, pady=200)
in_image = Image.open("C:\\Users\\lokha\\Python Practice\\Image Editor (Level 1)-Mustafa 202101053\\Main screen.jpg")
initial_image = ImageTk.PhotoImage(in_image)
canvas.create_image(0, 0, anchor = NW, image = initial_image)

new_canvas = Canvas(root, width=700, height=500)
new_canvas.pack(padx=500, pady=200)

def new_command():
    global new_image
    canvas.delete('all')
    img = Image.open("C:\\Users\\lokha\\Python Practice\\Image Editor (Level 1)-Mustafa 202101053\\White.jpg")
    new_img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=NW, image=new_img)

def open_command():
    global canvas,img,new_image,x,image_container
    x = filedialog.askopenfilename(initialdir="c:/", title="Open A File..", filetypes=(("PNG files","*.png"),("JPG files", "*.jpg")))
    #print(x)
    img = Image.open(x)
    resized_image = img.resize((540,380))
    new_image = ImageTk.PhotoImage(resized_image)
    image_container = canvas.create_image(0, 0, anchor=NW, image=new_image)
def save_command():
    global new_image
    s_file = messagebox.askyesno(title = "Save File", message="Do you want to save your work?")
    if s_file==1:
        image_file = filedialog.asksaveasfilename(defaultextension="*.*", initialdir=("C:"), title = "Save File", filetypes=(("PNG FILE","*.png"),("JPG FILE","*.jpg")))
        img.save(image_file)
def print_command():
    pass
def resize_command():
    #still left to do 
    global img, resize_img
    width_box = Entry(root, width=5)
    width_box.pack(padx=500,pady=200)
    width_box = int(width_box.get())
    height_box = Entry(root, width=5)
    height_box.pack(padx=500,pady=200)
    height_box = int(height_box.get())
    img = img.resize((width_box,height_box))
    resize_img = ImageTk.PhotoImage(img)
    update_resize_image()

def update_resize_image():
    #still left to do
    global img, resize_img
    canvas.itemconfig(image_container, image = resize_img)

def baw_command():
    #canvas.delete('new_image')
    global new_image, image_container, baw_img, img
    baw_image = img.convert('L')
    baw_resize_image = baw_image.resize((540,380))
    baw_img = ImageTk.PhotoImage(baw_resize_image)
    update_baw_image()

def update_baw_image():
    global image_container, baw_img, img
    canvas.itemconfig(image_container, image = baw_img)
    img = img.convert('L')

def copy_command():
    pass
def cut_command():
    pass
def paste_command():
    pass
def crop_command():
    pass
def rleft_command():
    global img,x,rl_image
    img_1 = img.rotate(angle=270, expand = True)
    img_1 = img_1.resize((540,380))
    rl_image = ImageTk.PhotoImage(img_1)
    update_rleft_image()
    
def update_rleft_image():
    global image_container, rl_image, img
    canvas.itemconfig(image_container, image = rl_image)
    img = img.rotate(angle=270, expand = True)

def rright_command():
    global img, r_image, rr_image
    r_image = img.rotate(angle=90, expand=True)
    r_image = r_image.resize((540,380))
    #r_image.show()
    rr_image = ImageTk.PhotoImage(r_image)
    update_rright_image()

def update_rright_image():
    global image_container, rr_image,img
    canvas.itemconfig(image_container, image = rr_image)
    img = img.rotate(angle=90, expand=True)

def hflip_command():
    global img, new_image, image_2
    img_2 = img.transpose(Image.FLIP_LEFT_RIGHT)   
    img_2 = img_2.resize((540,380))
    image_2 = ImageTk.PhotoImage(img_2)
    update_hflip_image()

def update_hflip_image():
    global image_container, image_2, img
    canvas.itemconfig(image_container, image = image_2)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)

def vflip_command():
    global img, new_image, vflip_image, img_3
    img_3 = img.transpose(Image.FLIP_TOP_BOTTOM) 
    img_3 = img_3.resize((540,380))
    vflip_image = ImageTk.PhotoImage(img_3)
    update_vflip_image()

def update_vflip_image():
    global image_container, vflip_image, img
    canvas.itemconfig(image_container, image = vflip_image)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
def info_command():
    info_label = Label(root, text="This Simple Image Editor is created by Mustafa Lokhandwala")
    info_label.pack()

def delete():
    canvas.delete('all')

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