import customtkinter as ctk
import tkinter

# Back End
def start_script(app, script: str):
    if script == "renum_newfiles":
    
def cancel_script():
    print("C")

# Front End
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Script Executor")
app.geometry("400x180")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure((0, 1), weight=1)

# Frame
button_frame = ctk.CTkFrame(app)
button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
optionmenu_frame = ctk.CTkFrame(app)
optionmenu_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

start_button = ctk.CTkButton(master=button_frame, text='Start', command=start_script)
start_button.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

cancel_button = ctk.CTkButton(master=button_frame, text='Cancel', command=cancel_script)
cancel_button.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

option_menu = ctk.CTkOptionMenu(master=optionmenu_frame, dynamic_resizing=False, values=["Renum New Files", "Script2"], command=start_button)
option_menu.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="e")

progress_bar = ctk.CTkProgressBar(app, orientation="horizontal")
progress_bar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

app.mainloop()