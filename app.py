import Tkinter as tk
import tkFileDialog
import os

root = tk.Tk()
root.resizable
apps = []

if os.path.isfile('apps.txt'):
    with open('apps.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():
    for widget in frame_1.winfo_children():
        widget.destroy()

    filename = tkFileDialog.askopenfilename(initialdir="/", title="Select File",
                                            filetypes=(("aplications", "*.app"), ("all files", "*.*")))
    apps.append(filename)

    for app in apps:
        label = tk.Label(frame_1, text=app, bg="#263D42")
        label.pack()


def runApp():
    for app in apps:
        cmd = "open -a {0}".format(app)
        os.system(cmd)


def clearApp():
    del apps[:]
    for app in apps:
        label = tk.Label(frame_1, text=app, bg="#263D42")
        label.pack()


frame_1 = tk.Frame(root, bg="#263D42", width=700, height=400)
frame_1.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

frame_2 = tk.Frame(root, bg="gray", width=400, height=400)
frame_2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

openFile = tk.Button(frame_2, text="Open File", command=addApp)
openFile.pack()

runApps = tk.Button(frame_2, text="Run Apps", command=runApp)
runApps.pack()

emptyList = tk.Button(frame_2, text="Clear", command=clearApp)
emptyList.pack()

for app in apps:
    label = tk.Label(frame_1, text=app, bg="#263D42")
    label.pack()

root.mainloop()

with open('apps.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
