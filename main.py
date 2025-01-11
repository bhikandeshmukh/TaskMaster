import os
import logging
from pathlib import Path
from Asset.pdf_handler import PDFHandler
from Asset.image_handler import ImageHandler
from Asset.excel_tool import ExcelTool  # Updated import to use ExcelTool
from Asset.utils import clear_screen, display_logo, list_files_and_select

# Ensure the Output directory exists
output_dir = Path('Output')
output_dir.mkdir(parents=True, exist_ok=True)

# Configure logging with absolute path
log_file_path = output_dir / 'log.log'
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main_menu():
    clear_screen()
    display_logo()

    while True:
        print("\033[92mSelect an option:\033[0m")
        print("\033[92m1. PDF Split\033[0m")
        print("\033[92m2. PDF Merge\033[0m")
        print("\033[92m3. PDF Blank Page Remove\033[0m")
        print("\033[92m4. Image Data Extract\033[0m")
        print("\033[92m5. Excel Tool\033[0m")
        print("\033[92m0. Exit\033[0m")

        choice = input("\033[92mEnter the number of the option: \033[0m")

        if choice == '1':
            pdf_path = list_files_and_select('.pdf')
            if pdf_path:
                PDFHandler.split(pdf_path)

        elif choice == '2':
            folder_path = list_files_and_select(is_folder=True)
            if folder_path:
                PDFHandler.merge(folder_path)

        elif choice == '3':
            pdf_path = list_files_and_select('.pdf')
            if pdf_path:
                PDFHandler.remove_blank(pdf_path)

        elif choice == '4':
            image_path = list_files_and_select(('.jpg', '.jpeg', '.png'))
            if image_path:
                ImageHandler.extract_data(image_path)

        elif choice == '5':
            folder_path = list_files_and_select(is_folder=True)  # Prompt for folder selection
            if folder_path:
                ExcelTool.main_menu(folder_path)  # Pass the folder path to ExcelTool

        elif choice == '0':
            logging.info("Exiting the program.")
            print("\033[92mExiting the program.\033[0m")
            break

        else:
            logging.info("Invalid choice. Please enter a valid option.")
            print("\033[92mInvalid choice. Please enter a valid option.\033[0m")

if __name__ == "__main__":
    main_menu()
