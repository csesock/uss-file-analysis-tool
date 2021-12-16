import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, simpledialog, filedialog
import tkinter.scrolledtext as tkscrolled
from tkinter.font import Font

import os

window = tk.Tk()
window.geometry('400x400')
window.title('United Systems File Analysis Tool')
window.resizable(False, False)
consoleFont = Font(family="Consolas", size=10)

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
    analyze_FHD()

def analyze_FHD():
    try:
        with open(download_filename, 'r') as openfile:
            console.insert(1.0, "Analyzing FHD record...\n")
            for line in openfile:
                if line.startswith('FHD'):
                    tables_indicator = line[3]
                    if tables_indicator.upper() != 'N' and tables_indicator.upper() != 'Y':
                        console.insert('end', 'Error in FHD record at tables indicator\n')
                    
                    optical_probe_indicator = line[4]
                    if optical_probe_indicator.upper() != 'N' and optical_probe_indicator.upper() != 'Y':
                        console.insert('end', 'Error in FHD record at optical probe indicator\n')
                    
                    version_number_of_table = line[5:10]
                    reserved = line[10:13]
                    number_of_cycles = line[13:15]
                    offsite_record_indicator = line[15]
                    wand_record_indicator = line[16]
                    extended_route_indicator = line[17]
                    pad = line[18:126]
                    cf_lf = line[126:127]
    except FileNotFoundError:
        return
    except Exception as e:
        print(str(e))

#UI
text = tk.StringVar()
if os.path.isfile('download.dat'):
    text.set('download.dat')
else:
    text.set('None')

labelCurrent = ttk.Label(text="Current file: ").place(x=10, y=20)
labelFile = ttk.Label(textvariable=text, foreground='#3baf29').place(x=80, y=20)

button_open = ttk.Button(text="Open File", command=lambda:openFile()).place(x=70, y=350)
button_analyze = ttk.Button(text="Analyze File", command=lambda:analyze()).place(x=160, y=350)
button_reset = ttk.Button(text="Reset", command=lambda:reset()).place(x=250, y=350)

console = tkscrolled.ScrolledText(height=18, width=50, font=consoleFont, background='black', foreground='white', 
                    insertborderwidth=7, undo=True, bd=3)
console.place(x=10, y=50)

if __name__=="__main__":
    window.mainloop()