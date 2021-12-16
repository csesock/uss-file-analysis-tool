import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, simpledialog, filedialog
import tkinter.scrolledtext as tkscrolled
from tkinter.font import Font

import os

window = tk.Tk()
window.geometry('400x550')
window.title('United Systems File Analysis Tool')
window.resizable(False, False)
consoleFont = Font(family="Consolas", size=10)

try:
    dirp = os.path.dirname(__file__)
    photo_icon = PhotoImage(file="assets\\IconSmall.png")
    window.iconphoto(False, photo_icon)
except:
    pass

#s = ttk.Style().theme_use('clam')

download_filename = 'download.dat'

def reset():
    console.delete(1.0, 'end')

def openFile():
    filename = tk.filedialog.askopenfilename(title="Open File")
    if filename == None or filename == '':
        return
    global download_filename
    download_filename = filename
    text.set(os.path.basename(download_filename))

def analyze():
    try:
        with open(download_filename, 'r') as openfile:
            for line in openfile:
                if line.startswith('FHD'):
                    analyze_FHD(line)
                if line.startswith('CHD'):
                    analyze_CHD()
                if line.startswith('RHD'):
                    analyze_RHD()
                if line.startswith('ERH'):
                    analyze_ERH()
                if line.startswith('CUS'):
                    analyze_CUS()
                if line.startswith('CSX'):
                    analyze_CSX()
        analyze_MTR()
        analyze_MTX()
        analyze_MTS()
        analyze_RDG()
        analyze_RFF()
    except Exception as e:
        print(str(e))

def analyze_FHD(line):
    console.insert('end', "Analyzing FHD record...\n")

    tables_indicator = line[3]
    console.insert('end', 'Checking tables indicator at index 3...\n')
    if tables_indicator.upper() != 'N' and tables_indicator.upper() != 'Y':
        console.insert('end', 'Error in FHD record at tables indicator\n')
    else:
        console.insert('end', 'No error found with tables indicator.\n')
    
    optical_probe_indicator = line[4]
    console.insert('end', 'Checking optical probe indicator at index 4...\n')
    if optical_probe_indicator.upper() != 'N' and optical_probe_indicator.upper() != 'Y':
        console.insert('end', 'Error in FHD record at optical probe indicator\n')
    else:
        console.insert('end', 'No error found with optical probe indicator.\n')
    
    version_number_of_table = line[5:10]
    reserved = line[10:13]
    number_of_cycles = line[13:15]
    offsite_record_indicator = line[15]
    wand_record_indicator = line[16]
    extended_route_indicator = line[17]
    pad = line[18:126]
    cf_lf = line[126:127]

def analyze_CHD():
    console.insert('end', "Analyzing CHD record...\n")
    return

def analyze_RHD():
    console.insert('end', "Analyzing RHD record...\n")
    return

def analyze_ERH():
    console.insert('end', "Analyzing ERH record...\n")
    return

def analyze_CUS():    
    console.insert('end', "Analyzing CUS record...\n")
    return

def analyze_CSX():
    console.insert('end', "Analyzing CSX record...\n")
    return

def analyze_MTR():
    console.insert('end', "Analyzing MTR record...\n")
    return

def analyze_MTX():
    console.insert('end', "Analyzing MTX record...\n")
    return

def analyze_MTS():
    console.insert('end', "Analyzing MTS record...\n")
    return

def analyze_RDG():
    console.insert('end', "Analyzing RDG record...\n")
    return

def analyze_RFF():
    console.insert('end', "Analyzing RFF record...\n")
    return

#UI
text = tk.StringVar()
if os.path.isfile('download.dat'):
    text.set('download.dat')
else:
    text.set('None')

labelCurrent = ttk.Label(text="Current file: ").place(x=10, y=10)
labelFile = ttk.Label(textvariable=text, foreground='#3baf29').place(x=80, y=10)

button_open = ttk.Button(text="Open File", command=lambda:openFile()).place(x=70, y=490)
button_analyze = ttk.Button(text="Analyze File", command=lambda:analyze()).place(x=160, y=490)
button_reset = ttk.Button(text="Reset", command=lambda:reset()).place(x=250, y=490)

console = tkscrolled.ScrolledText(height=28, width=51, font=consoleFont, background='black', foreground='white', 
                    insertborderwidth=7, undo=True, bd=3)
console.place(x=10, y=40)

# Menu
menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open...", accelerator='Ctrl+O', command=lambda:openFile())
filemenu.add_command(label="Save", accelerator='Ctrl+S', command=lambda:save())
filemenu.add_command(label="Save As...", accelerator='Ctrl+Alt+S', command=lambda:saveAs())
filemenu.add_separator()
filemenu.add_command(label="Exit", command=lambda:window.destroy())
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Copy", accelerator="Ctrl+C")
editmenu.add_command(label="Paste", accelerator="Ctrl+V")
editmenu.add_separator()
editmenu.add_command(label="Clear Console", accelerator="Ctrl+X", command=lambda:clearConsole(TAB_CONTROL.index(TAB_CONTROL.select())+1))
editmenu.add_command(label="Search...", accelerator="Ctrl+F", command=lambda:searchRecords())

menubar.add_cascade(label="Edit", menu=editmenu)

windowmenu = tk.Menu(menubar, tearoff=0)

window_submenu = Menu(windowmenu)
windowmenu.add_command(label="Reset Window", accelerator="F10", command=lambda:resetWindow())

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", accelerator='F1', command=lambda:aboutDialog())
helpmenu.add_command(label="Purge Log Files", accelerator='F2', command=lambda:Logging.deleteLog(int(logDeleteOldInput.get())))
helpmenu.add_command(label="Check for Updates...")
menubar.add_cascade(label="Help", menu=helpmenu)

if __name__=="__main__":
    window.config(menu=menubar)
    window.mainloop()