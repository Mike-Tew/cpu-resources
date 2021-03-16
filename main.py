from tkinter import Tk, Label
import psutil


def get_resource_usage():
    """Get and display CPU and RAM usage every second."""

    cpu_usage = psutil.cpu_percent()
    cpu_label.config(text=f"CPU\n{cpu_usage}")
    memory_usage = psutil.virtual_memory()[2]
    memory_label.config(text=f"RAM\n{memory_usage}%")

    cpu_label.after(1000, get_resource_usage)

root = Tk()
root.geometry("+700+300")

cpu_label = Label(root, text="CPU Load", font=("Helvetica 20"))
cpu_label.grid(row=0, column=0, padx=30)

memory_label = Label(root, text="Memory", font=("Helvetica 20"))
memory_label.grid(row=0, column=1, padx=30)

get_resource_usage()

root.mainloop()