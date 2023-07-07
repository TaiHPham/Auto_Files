import os
import tkinter as *
import customtkinter
from tkinter import filedialog, messagebox
from scripts.renum_newfiles import renum_newfiles

def perform_script():
    selected_script = script_variable.get()
    if selected_script == 'renum_newfiles':
        rename_files(folder_path_entry.get(), output_text)
    # Add import statements and function calls for other scripts as needed

def select_folder():
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(tk.END, folder_path)

def cancel():
    if messagebox.askyesno('Confirmation', 'Are you sure you want to cancel?'):
        root.destroy()

root = customtkinter.CTk()
root.title('Script Executor')

customtkinter.set_appearance_mode("light")

folder_path_label = customtkinter.CTkLabel(master=root, text='Folder Path:')
folder_path_label.pack()

folder_path_entry = customtkinter.CTkEntry(master=root, width=50)
folder_path_entry.pack()

select_folder_button = customtkinter.CTkButton(master=root, text='Select Folder', command=select_folder)
select_folder_button.pack()

output_label = customtkinter.CTkLabel(master=root, text='Output:')
output_label.pack()

output_text = tk.Text(root, width=50, height=10)
output_text.pack()

script_label = customtkinter.CTkLabel(master=root, text='Select Script:')
script_label.pack()

scripts = ['Rename Files', 'Script 2', 'Script 3']  # Add more scripts as needed

script_variable = tk.StringVar(root)
script_variable.set(scripts[0])  # Set the default script

script_dropdown = customtkinter.CTkOptionMenu(root, script_variable, *scripts)
script_dropdown.pack()

start_button = customtkinter.CTkButton(master=root, text='Start', command=perform_script)
start_button.pack()

cancel_button = customtkinter.CTkButton(master=root, text='Cancel', command=cancel)
cancel_button.pack()

root.mainloop()
