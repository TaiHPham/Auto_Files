import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from scripts.renum_newfiles import renumber_files
from scripts.search_failedDL import search_files

def perform_script():
    selected_script = script_variable.get()
    if selected_script == 'Renumber Files':
        renumber_files(folder_path_entry.get(), output_text, progress_bar, tk)
    elif selected_script == 'Search Failed Download':
        search_files(folder_path_entry.get(), output_text, progress_bar, tk)
    # Add import statements and function calls for other scripts as needed

def select_folder():
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(tk.END, folder_path)

def cancel():
    if messagebox.askyesno('Confirmation', 'Are you sure you want to cancel?'):
        root.destroy()
        
def clear_output():
    output_text.delete(1.0, tk.END)

root = tk.Tk()
root.title('Script Executor')

# Create a Frame widget
frame5 = tk.Frame(root)
frame5.pack(anchor="center", expand=True, pady=(10,10)) 

frame4 = tk.Frame(root)
frame4.pack(anchor="center", expand=True) 

frame3 = tk.Frame(root)
frame3.pack(anchor="center", expand=True, side=tk.BOTTOM, pady=(10,20)) 

frame2 = tk.Frame(root)
frame2.pack(anchor="center", expand=True, side=tk.BOTTOM) 

frame = tk.Frame(root)
frame.pack(anchor="center", expand=True, side=tk.BOTTOM, pady=(20,10))
# Create a Frame widget

folder_path_label = tk.Label(frame5, text='Folder Path:')
folder_path_label.pack()

folder_path_entry = tk.Entry(frame5, width=50)
folder_path_entry.pack()

select_folder_button = tk.Button(frame5, text='Select Folder', command=select_folder)
select_folder_button.pack(pady=(5,0))

output_label = tk.Label(frame4, text='Output:')
output_label.pack()

output_text = tk.Text(frame4, width=50, height=10)
output_text.pack(padx=(10, 10))

clear_button = tk.Button(frame4, text='Clear Output', command=clear_output)
clear_button.pack(pady=(5,0))

# FRAME #
start_button = tk.Button(frame, text='Start', command=perform_script)
start_button.pack(side=tk.LEFT, padx=(0, 10))

cancel_button = tk.Button(frame, text='Cancel', command=cancel)
cancel_button.pack(side=tk.RIGHT, padx=(10, 0))
# FRAME #

# FRAME 2 #
progress_bar = ttk.Progressbar(frame2, mode='determinate')
progress_bar.pack()
# FRAME 2 #

# FRAME 3 #
script_label = tk.Label(frame3, text='Select Script:')
script_label.pack()

scripts = ['Renumber Files', 'Search Failed Download']  # Add more scripts as needed

script_variable = tk.StringVar(root)
script_variable.set(scripts[0])  # Set the default script

script_dropdown = tk.OptionMenu(frame3, script_variable, *scripts)
script_dropdown.pack()
# FRAME 3 #

root.mainloop()
