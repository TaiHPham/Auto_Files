# Searches the download folder to find any failed downloads that usually contains ext. ".f313"

import os

def search_files(folder_path, output_text, progress_bar, tk):
    files = os.listdir(folder_path)

    total_files = len(files)
    counter = 0
    failed_files = []

    progress_bar['maximum'] = total_files  # Set the maximum value for the progress bar
    for index, file in enumerate(files, start=1):
        counter += 1
        progress_bar['value'] = counter  # Set the current progress value
        progress_bar.update()
        output_text.insert(tk.END, f"Searching {index} out of {total_files} files\n")
        if '.f313' in file:
            failed_files.append(file)

    if failed_files:
        output_text.insert(tk.END, "\nFailed to download files:\n")
        for index, failed_file in enumerate(failed_files, start=1):
            output_text.insert(tk.END, f"{index}. {failed_file}\n")
    else:
        output_text.insert(tk.END, "No files containing '.f313' found.\n")