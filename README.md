**CIS 442 Project**

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

    Now that venv is active use Python to execute main.py
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