# This script will take any file with 5 digits (yt-dlp default numbering) and renumber the new files to latest number of the files
# If the last number is 123_filename > 00001_filename will be 124_filename > 00002_filename will be 125_filename

import os

def renumber_files(folder_path, output_text, progress_bar, tk):
    files = os.listdir(folder_path)
    new_files = [file for file in files if len(file.split('_')[0]) == 5]
    new_files.sort()

    total_files = len(files)
    total_new_files = len(new_files)
    starting_number = total_files - total_new_files + 1

    progress_bar['maximum'] = total_new_files  # Set the maximum value for the progress bar

    output_text.delete(1.0, tk.END)

    for i, file in enumerate(new_files, starting_number):
        new_number = str(i)
        original_title = file.split('_', 1)[1]
        new_title = new_number + '_' + original_title
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_title))
        output_text.insert(tk.END, f'Renamed {file} to {new_title}\n\n')
        output_text.update()
        progress_bar['value'] = i - starting_number + 1  # Set the current progress value
        progress_bar.update()

