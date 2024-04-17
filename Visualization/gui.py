# data format: 
# N x 6 x Timesteps 
# N = number of signals being tracked 
# second dimension of 6 elements is [x_pos, y_pos, z_pos, freq (GHz), power (mW), estimation bubble diameter (m)] in that exact order.
# Each signal (1 to N), has those 6 parameters being tracked for every timestep (1 to T). The example of how I iterate through the 'final_data' vector to make it move in time is also in the Matlab file at the bottom.

import scipy.io # this will be used for opening the .mat file 
import tkinter as tk 
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


#loading the data
#mat = scipy.io.loadmat('test_data.mat')
#organizing the data

#loading the 3d spoace 
# TODO: check to see how tkinter adds a 3d gui instead of whatever i just found 
fig = plt.figure()
ax = plt.axes(projection='3d')


# building the box 
root = tk.Tk()
root.geometry("500x500")
root.title("Flock Force Application ")
label = tk.Label(root, text="Flock Force", font=('Arial',18))
label.pack()
root.mainloop()