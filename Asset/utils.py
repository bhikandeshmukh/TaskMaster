import os

def clear_screen():
    """Clear the console screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    """Display the logo on the screen."""
    logo = """
    \033[93m+++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m
       \033[93m_____         _    __  __           _\033[0m            
      \033[93m|_   _|_ _ ___| | _|  \/  | __ _ ___| |_ ___ _ __\033[0m 
        \033[93m| |/ _ / __| |/ / |\/| |/ _ / __| __/ _ \ '__|\033[0m
        \033[93m| | (_| \__ \   <| |  | | (_| \__ \ ||  __/ |\033[0m   
        \033[93m|_|\__,_|___/_|\_\_|  |_|\__,_|___/\__\___|_|\033[0m      
    \033[91m                 v.0.2 \033[91mAuthor - Bhikan Deshmukh\033[0m
    \033[93m+++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m
    """
    print(logo)

def list_files_and_select(extension=None, is_folder=False):
    """
    List files and folders in the current directory and allow the user to select one.
    
    Parameters:
    - extension: File extension to filter (e.g., '.pdf' or '.jpg'). If None, all files are listed.
    - is_folder: If True, only folders are listed.
    
    Returns:
    - The selected file or folder path, or None if an invalid selection is made.
    """
    parent_dir = os.getcwd()

    if is_folder:
        items = [f for f in os.listdir(parent_dir) if os.path.isdir(f)]
    else:
        # Correct logic for filtering files by extension
        items = [f for f in os.listdir(parent_dir) if extension is None or f.endswith(extension)]

    if not items:
        print("\033[92mNo valid files or folders found.\033[0m")
        return None

    print("\033[92mAvailable files and folders:\033[0m")
    for idx, item in enumerate(items, start=1):
        print(f"\033[92m{idx}. {item}\033[0m")

    try:
        selection = int(input("\033[92mEnter the number of the file or folder you want to select: \033[0m").strip())
        if 1 <= selection <= len(items):
            return os.path.join(parent_dir, items[selection - 1])
        else:
            print("\033[92mInvalid selection.\033[0m")
            return None
    except ValueError:
        print("\033[92mInvalid input. Please enter a number.\033[0m")
        return None
