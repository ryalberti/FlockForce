import tkinter as tk
import tkintermapview

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

# create tkinter window
root = tk.Tk()
root.geometry(f"{800}x{600}")
root.title("Flock Force Application")

label = tk.Label(root, text="Flock Force", font=('Arial',320))
label.pack(pady=20)

# create map widget
map_widget = tkintermapview.TkinterMapView(root, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# set current widget position and zoom
map_widget.set_position(48.860381, 2.338594)  # Paris, France
map_widget.set_zoom(15)

# set current widget position by address
map_widget.set_address("colosseo, rome, italy")

# set current widget position by address
marker_1 = map_widget.set_address("colosseo, rome, italy", marker=True)

print(marker_1.position, marker_1.text)  # get position and text

marker_1.set_text("Colosseo in Rome")  # set new text
# marker_1.set_position(48.860381, 2.338594)  # change position
# marker_1.delete()
root.mainloop()