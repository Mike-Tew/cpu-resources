# TODO
# Change colors depending on usage percentages.

from tkinter import Tk, Label
import psutil


def get_resource_usage():
    """Get and display CPU and RAM usage every second."""

    cpu_usage = psutil.cpu_percent()
    cpu_load_label.config(text=f"{cpu_usage}%")
    memory_usage = psutil.virtual_memory()[2]
    memory_load_label.config(text=f"{memory_usage}%")

    cpu_label.after(1000, get_resource_usage)

root = Tk()
root.geometry("+700+300")
root.title("Resource Usage")

cpu_label = Label(root, text="CPU", font=("Helvetica 15"))
cpu_label.grid(row=0, column=0, padx=20, pady=[10, 0])

cpu_load_label = Label(root, text="0.0%", font=("Helvetica 13"))
cpu_load_label.grid(row=1, column=0, pady=[0, 10])

memory_label = Label(root, text="RAM", font=("Helvetica 15"))
memory_label.grid(row=0, column=1, padx=20, pady=[10, 0])

memory_load_label = Label(root, text="0.0%", font=("Helvetica 13"))
memory_load_label.grid(row=1, column=1, pady=[0, 10])

get_resource_usage()

root.mainloop()