# Written By: Andrew Raposo
# Date: 2023-10-23
# Description: This program is a masquaraded file finder. It takes in a directory and searches for
#             masquaraded files in that directory. It does this by comparing the file signature of
#             the file to the file signature that corresponds to the file extension of the file.
#             If it does not match then we have a masquaraded file.

# Reference: This project was given by the University of Massachusetts Dartmouth for the course 
# CIS 442 - Digital Forensics taught by Professor Gohkan Kul.

import os, tkinter as tk
from tkinter import filedialog, scrolledtext
from signatures import file_signatures

# Determines if path is real meaning and existing directory
def check_directory(directory):
    if str(directory).strip() == "":
        clear_output()
        write_to_output("Directory field is empty.\n")
        return False
    
    elif not os.path.isdir(directory):
        clear_output()
        write_to_output(f"Directory does not exist: {directory}\n")
        return False
    
    return True

# Matches file signature to files in a directory given, and finds masquaraded files in that directory.
def match_file_signatures(dir_path):
    for _file in os.listdir(dir_path):
        if os.path.isdir(_file):
            continue

        file_path = os.path.abspath(os.path.join(dir_path, _file))
        file_extension = _file.split(".")[-1]
        
        if file_extension not in file_signatures:
            continue
        elif file_extension == "txt":
            with open(file_path, "rb") as f:
                file_contents = f.read(16)
                if not all([32 <= byte <= 126 for byte in file_contents]):
                    write_to_output(f"Masquaraded file found: {file_path}, contents:  {file_contents}\n")
                    continue
            continue

        file_signature = file_signatures[file_extension]
        found_signature_match = False

        for signature in file_signature:
            with open(file_path, "rb") as f:
                if isinstance(signature, str):
                    file_contents = f.read(int(len(signature)/2))
                else:
                    file_contents = f.read(len(signature))

            if isinstance(signature, str):
                if "?" in signature:
                    part1_signature, part2_signature = bytes.fromhex(signature.split("?")[0]), bytes.fromhex(signature.split("?")[-1])
                    if file_contents[:len(part1_signature)] == part1_signature and file_contents[-len(part2_signature):] == part2_signature:
                        found_signature_match = True
                        break
            elif file_contents == signature:
                found_signature_match = True
                break

        if not found_signature_match:
            # Print the masquaraded file to the output box
            write_to_output(f"Masquaraded file found: {file_path}, contents:  {file_contents}\n")

# Opens the file system search to allow the user to select a directory
def open_file_dialog():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

# Submits the directory that the user has entered to find masquaraded files in
def submit_action():
    # Get the input directory
    directory = directory_entry.get()

    # Check if directory is valid
    if not check_directory(directory):
        return

    # Clear the output box
    clear_output()

    # Start searching for masquaraded files
    write_to_output(f"Processing directory: {directory}\n")
    match_file_signatures(directory)

# Clears the output box in the GUI
def clear_output():
    output_text.delete('1.0', tk.END)

def write_to_output(text):
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, text)
    output_text.config(state=tk.DISABLED)

def main():
    # Start the GUI
    window.mainloop()

    return 0

if __name__ == '__main__':
    # Create the main window
    window = tk.Tk()
    window.title("Masquaraded File Finder")

    # Configure the window to be resizable
    window.geometry("600x400") 
    window.resizable(width=True, height=True) 

    # Directory Input
    directory_label = tk.Label(window, text="Enter Directory:")
    directory_label.pack()
    directory_entry = tk.Entry(window, width=65)
    directory_entry.pack()

    # Browse Button
    browse_button = tk.Button(window, text="Browse Directory", command=open_file_dialog)
    browse_button.pack()

    # Submit Button
    submit_button = tk.Button(window, text="Run", command=submit_action)
    submit_button.pack()

    # Output Box
    output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=20)
    output_text.pack()
    output_text.config(state=tk.DISABLED)

    main()