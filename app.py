# help us create the gui
import tkinter as tk
# filedialog allows us to select the programs / apps and add them to the gui. Text will allow us to display text.
from tkinter import filedialog, Text
# Allows us to run the apps/programs on the computer
import os


root = tk.Tk()
apps = []


if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text-app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


# Lets make the gui larger
canvas = tk.Canvas(root, height=550, width=550, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# why am I coding on a friday night? Because I want to be a TECH MOGUL!

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42", command=addApp)

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#263D42", command=runApps)

runApps.pack()

root.mainloop()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()
# When we close our app, it will write the txt file of all the files we have opened.
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
