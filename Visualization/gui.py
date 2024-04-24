# data format: 
# N x 6 x Timesteps 
# N = number of signals being tracked 
# second dimension of 6 elements is [x_pos, y_pos, z_pos, freq (GHz), power (mW), estimation bubble diameter (m)] in that exact order.
# Each signal (1 to N), has those 6 parameters being tracked for every timestep (1 to T). The example of how I iterate through the 'final_data' vector to make it move in time is also in the Matlab file at the bottom.

import scipy.io # this will be used for opening the .mat file 
import tkinter as tk
from tkinter import filedialog
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import ctypes
import tkintermapview

#loading the data
#mat = scipy.io.loadmat('test_data.mat')
#organizing the data

#loading the 3d spoace 
# TODO: check to see how tkinter adds a 3d gui instead of whatever i just found 
#fig = plt.figure()
#ax = plt.axes(projection='3d')

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("MATLAB files",
                                                        "*.mat*"),
                                                        ("Databases",
                                                         "*.db*"),
                                                        ("SQLite",
                                                         "*.sqlite*"),
                                                        ("excel",
                                                         "*.xlsx*"),
                                                        ("all files",
                                                         "*.*")))

# building the box
root = tk.Tk() #Create a window widget
#myappid = 'flockforce.gui.v.1'
#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
root.iconbitmap("images/flockforceimage.ico") #Set icon
root.state('zoomed') #Make it fullscreen
root.title("Flock Force GUI")
root.minsize(400, 400) #for minimized window
root.configure(background="light blue")

#Create widgets
label1 = tk.Label(root, text="Flock Force", font=('bold',50), background="light blue",anchor='n')
#frequency dropdown menu
drop1 = tk.StringVar()
# Dropdown menu options
options1 = [
    "3 GHz",
    "4 GHz",
    "5 GHz",
    "6 GHz",
    "7 GHz",
    "8 GHz",
    "9 GHz"
]

# initial menu text
drop1.set("Frequency")

# Create Dropdown menu
freq = tk.OptionMenu(root, drop1, *options1)
freq["width"] = 8
freq["height"] = 2
freq["highlightbackground"] = 'blue'
freq["highlightthickness"] = 2
freq["borderwidth"] = 2
freq["background" ] = "cyan"
freq["activebackground" ] = "blue"
freq["font"] = 'Bold 15'
freq["menu"]["background"] = "gray"
freq["menu"]["foreground"] = "black"
freq["menu"]["font"] = "Bold 15"
freq["menu"]["selectcolor"] = "green"
freq["menu"]["activeborderwidth"] = '4'

#power dropdown menu
drop2 = tk.StringVar()
# Dropdown menu options
options2 = [
    "3 W",
    "4 W",
    "5 W",
    "6 W",
    "7 W",
    "8 W",
    "9 W"
]

# initial menu text
drop2.set("Power")

# Create Dropdown menu
power = tk.OptionMenu(root, drop2, *options2)
power["width"] = 8
power["height"] = 2
power["highlightbackground"] = 'dark red'
power["highlightthickness"] = 2
power["borderwidth"] = 2
power["background"] = "red"
power["activebackground" ] = "dark red"
power["font"] = 'Bold 15'
power["menu"]["background"] = "gray"
power["menu"]["foreground"] = "black"
power["menu"]["font"] = "Bold 15"
power["menu"]["selectcolor"] = "green"
power["menu"]["activeborderwidth"] = '4'

#power = tk.Button(root, text='Power', width = 10, height = 2, background = 'red', font=('bold',15), highlightbackground='dark red', highlightthickness=5, borderwidth=5)
location = tk.Button(root, text='Location', width = 10, height = 2, background = 'lime', font=('bold',15), highlightbackground='green', highlightthickness=5, borderwidth=5)
files = tk.Button(root,command=browseFiles, text='File Explorer', width = 10, height = 2, font=('bold',15), highlightbackground='white', highlightthickness=5, borderwidth=5)
#mapspace = tk.Label(root, width = 10, height = 2, background = "gray", borderwidth=30, border=300)
img = Image.open("images/flockforceimage.png")
img = img.resize((80, 80))
img = ImageTk.PhotoImage(img)
logo = tk.Label(root, image=img) #adding logo image

#define the grid
root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)
root.columnconfigure(3, weight = 1)
root.columnconfigure(4, weight = 1)
root.columnconfigure(5, weight = 1)
root.columnconfigure(6, weight = 1)
root.columnconfigure(7, weight = 1)
root.columnconfigure(8, weight = 0)
root.rowconfigure(0, weight = 0)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.rowconfigure(3, weight = 1)
root.rowconfigure(4, weight = 1)
root.rowconfigure(5, weight = 1)
root.rowconfigure(6, weight = 1)
#place widgets
label1.grid(row = 0, column = 2, columnspan=6, sticky = "n")
freq.grid(row = 1, column = 0, sticky = "se")
power.grid(row = 2, column = 0, sticky = "se")
location.grid(row = 3, column = 0, sticky = "se")
files.grid(row = 4, column = 0, sticky = "se")
logo.grid(row = 0, column = 8, sticky = "ne")
#mapspace.grid(row = 1, column = 2, rowspan = 5, columnspan = 6, sticky = "nesw")

# create map widget
map_widget = tkintermapview.TkinterMapView(root, width=800, height=600, corner_radius=0, highlightthickness=3, highlightbackground='black')
map_widget.grid(row = 1, column = 2, rowspan = 5, columnspan = 6, sticky = "nesw")

# set current widget position for exact coordinates and zoom level
# map_widget.set_position(40.7448, -74.0256)  # Hoboken, NJ
# map_widget.set_zoom(20)

# set current widget position by address (automatically zoomed in)
marker_1 = map_widget.set_address("Stevens Institute of Technology, Hoboken, New Jersey", marker=True)

print(marker_1.position, marker_1.text)  # get position and text

marker_1.set_text("Stevens Institute of Technology")  # set new text
# marker_1.set_position(48.860381, 2.338594)  # change position
# marker_1.delete()

root.mainloop()
