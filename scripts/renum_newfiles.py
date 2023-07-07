# rename_files_script.py

import os

def renum_newfiles(folder_path, output_text):
    files = os.listdir(folder_path)
    new_files = [file for file in files if len(file.split('_')[0]) == 5]
    new_files.sort()

    total_files = len(files)
    total_new_files = len(new_files)
    starting_number = total_files - total_new_files + 1

    output_text.delete(1.0, tk.END)

    for i, file in enumerate(new_files, starting_number):
        new_number = str(i)
        original_title = file.split('_', 1)[1]
        new_title = new_number + '_' + original_title
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_title))
        output_text.insert(tk.END, f'Renamed {file} to {new_title}\n\n')
