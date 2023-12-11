**CIS 442 Project**

This repository was created as a requirement of CIS 442 (Fall 2023) at UMass Dartmouth.

Author ~ Andrew Raposo

Requirements:
    
    - Users should use/have Python 3.10 or greater installed to run the code of this project.
    - User must run the main.py program to use GUI to find masqueraded files.


Setup Requirements:

    Clone project repo down to local computer

    Using terminal/command prompt navigate to repository folder and with Python create a local python enviroment in the repo folder:
        
        Step 1: Create environment (maybe python or python3 in your terminal)
            Mac/Linux/Windows: python -m venv .env
                               python3 -m venv .env

        Step 2: Activate the python venv
            Windows: call .\.env\Scripts\activate

            Mac/Linux: source ./.env/bin/activate

    Now that virtual environment (venv) is active use Python to execute main.py
    (maybe python or python3 in your terminal)
        python main.py
        python3 main.py

    At this point the GUI should pop up from running the main.py


Using the GUI:

    - You may type in a directory in the top box, this could be a absolute path or a relative path to 
      the main.py file you are running or where ever your current working directory is.
        -> If a dirctory is invalid the program will notify you that it is invalid in the output box at bottom of GUI
           after pressing the "Run" button
    
    - There is also a "Browse Directory" button this will allow you to select a directory from your
      file explorer GUI, this could be (Finder (Mac), File Explorer (Windows), etc...)

    - Once your directory is input or selected from "Browse Dirctory" then you may press the "Run" button,
      this will search within that directory identifying files that are masqueraded printing them to the 
      output box at the bottom of the GUI
        -> This output box is scrollable if there are many masqueraded files


Description:

    This program is capable of taking in directory paths and searching for masqueraded files within the given directory, this
    is possible due to a python dictionary storing lists of "file signatures" that can appear for a given "file extension", this
    dictionary is stored within the signatures.py file as to not clutter the main.py file. Once a directory is either selected or
    given within the GUI, a user may press the "Run" button where the program will scan and determine if there are any masqueraded
    files there, printing out those files to the output box that are masqueraded. Note that it will only scan the current directories
    top level, it does not recursively go through folders inside of the directory.

    Scanning Process: Iterates over files in the directory and checks its extension grabbing the corresponding list of file
    signatures that go to that extension. Then we read in the bytes of the file checking it against each of the file signatures
    we have for that extension, if the files bytes do not match one of the signatures we have for that extension then we have
    a masqueraded file.

    File Signature Data: https://en.wikipedia.org/wiki/List_of_file_signatures
      Note: Program should work with most/all file signatures from the wikipedia table but there are occurences for certain files
      to have different signatures that are not in this list, there are also old and unique file types that may not be contained in
      this comprehensive list

    YouTube Video Demo: https://www.youtube.com/watch?v=tWwvFIeaWCI

    GitHub Repository: https://github.com/Anddar/CIS442-Project

Test Cases:

    This program comes with a TestDir in it, these were the test cases done/used in the demo video and so we can say that files with
    these extensions should be caught by this program. Other test cases have been done as well and so I will include those extensions
    here as well:

    - ISO
    - TXT
    - PDF
    - PNG
    - XLSX
    - JPG/JPEG
    - MP4