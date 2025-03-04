import os
import logging
import time
from pathlib import Path
from tqdm import tqdm
from Asset.pdf_handler import PDFHandler
from Asset.image_handler import ImageHandler
from Asset.excel_tool import ExcelTool
from Asset.utils import clear_screen, display_logo, list_files_and_select

# Ensure the Output directory exists
output_dir = Path('Output')
output_dir.mkdir(parents=True, exist_ok=True)

# Configure logging with absolute path
log_file_path = output_dir / 'log.log'
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def show_progress(duration=1):
    """Show a progress bar for operations."""
    for _ in tqdm(range(100), desc="Processing", ncols=100):
        time.sleep(duration/100)

def main_menu():
    clear_screen()
    display_logo()

    while True:
        print("\n\033[95m=== Main Menu ===\033[0m")
        print("\033[92m1. PDF Tools\033[0m")
        print("\033[92m2. Image Tools\033[0m")
        print("\033[92m3. Excel Tools\033[0m")
        print("\033[92m4. File Management\033[0m")
        print("\033[92m5. About\033[0m")
        print("\033[92m0. Exit\033[0m")

        choice = input("\n\033[93mEnter your choice (0-5): \033[0m")

        try:
            if choice == '1':
                pdf_menu()
            elif choice == '2':
                image_menu()
            elif choice == '3':
                excel_menu()
            elif choice == '4':
                file_management_menu()
            elif choice == '5':
                show_about()
            elif choice == '0':
                print("\n\033[92mThank you for using TaskMaster! Goodbye!\033[0m")
                logging.info("Program terminated by user")
                break
            else:
                print("\n\033[91mInvalid choice! Please try again.\033[0m")

        except Exception as e:
            logging.error(f"Error in main menu: {str(e)}")
            print(f"\n\033[91mAn error occurred: {str(e)}\033[0m")
            input("\nPress Enter to continue...")

def pdf_menu():
    """Submenu for PDF operations"""
    while True:
        clear_screen()
        print("\n\033[95m=== PDF Tools ===\033[0m")
        print("\033[92m1. Split PDF\033[0m")
        print("\033[92m2. Merge PDFs\033[0m")
        print("\033[92m3. Remove Blank Pages\033[0m")
        print("\033[92m4. PDF Compression\033[0m")
        print("\033[92m0. Back to Main Menu\033[0m")

        choice = input("\n\033[93mEnter your choice (0-4): \033[0m")

        try:
            if choice == '1':
                pdf_path = list_files_and_select('.pdf')
                if pdf_path:
                    show_progress(0.5)
                    PDFHandler.split(pdf_path)
                    print("\n\033[92mPDF Split completed successfully!\033[0m")

            elif choice == '2':
                folder_path = list_files_and_select(is_folder=True)
                if folder_path:
                    show_progress(0.5)
                    PDFHandler.merge(folder_path)
                    print("\n\033[92mPDF Merge completed successfully!\033[0m")

            elif choice == '3':
                pdf_path = list_files_and_select('.pdf')
                if pdf_path:
                    show_progress(0.5)
                    PDFHandler.remove_blank(pdf_path)
                    print("\n\033[92mBlank pages removed successfully!\033[0m")

            elif choice == '4':
                pdf_path = list_files_and_select('.pdf')
                if pdf_path:
                    show_progress(0.5)
                    PDFHandler.compress_pdf(pdf_path)
                    print("\n\033[92mPDF compression completed successfully!\033[0m")

            elif choice == '0':
                break

            input("\nPress Enter to continue...")

        except Exception as e:
            logging.error(f"Error in PDF menu: {str(e)}")
            print(f"\n\033[91mAn error occurred: {str(e)}\033[0m")
            input("\nPress Enter to continue...")

def image_menu():
    """Submenu for image operations"""
    while True:
        clear_screen()
        print("\n\033[95m=== Image Tools ===\033[0m")
        print("\033[92m1. Extract EXIF Data\033[0m")
        print("\033[92m2. Remove EXIF Data\033[0m")
        print("\033[92m3. Image Compression\033[0m")
        print("\033[92m4. Image Format Conversion\033[0m")
        print("\033[92m5. Batch Image Conversion\033[0m")
        print("\033[92m6. Images to PDF\033[0m")
        print("\033[92m0. Back to Main Menu\033[0m")

        choice = input("\n\033[93mEnter your choice (0-6): \033[0m")

        try:
            if choice == '1':
                image_path = list_files_and_select(('.jpg', '.jpeg', '.png'))
                if image_path:
                    show_progress(0.3)
                    ImageHandler.extract_data(image_path)
                    print("\n\033[92mImage data extraction completed!\033[0m")

            elif choice == '2':
                image_path = list_files_and_select(('.jpg', '.jpeg', '.png'))
                if image_path:
                    show_progress(0.3)
                    ImageHandler.remove_exif_data(image_path)
                    print("\n\033[92mEXIF data removed successfully!\033[0m")

            elif choice == '3':
                image_path = list_files_and_select(('.jpg', '.jpeg', '.png'))
                if image_path:
                    show_progress(0.3)
                    ImageHandler.compress_image(image_path)
                    print("\n\033[92mImage compression completed!\033[0m")

            elif choice == '4':
                image_path = list_files_and_select(('.jpg', '.jpeg', '.png'))
                if image_path:
                    show_progress(0.3)
                    ImageHandler.convert_format(image_path)
                    print("\n\033[92mImage format conversion completed!\033[0m")

            elif choice == '5':
                folder_path = list_files_and_select(is_folder=True)
                if folder_path:
                    print("\n\033[92mChoose output format:\033[0m")
                    print("\033[92m1. JPEG\033[0m")
                    print("\033[92m2. JPG\033[0m")
                    print("\033[92m3. PNG\033[0m")
                    format_choice = input("\n\033[93mEnter the number corresponding to the format: \033[0m").strip()
                    format_map = {"1": "jpeg", "2": "jpg", "3": "png"}
                    if format_choice in format_map:
                        show_progress(0.5)
                        ImageHandler.batch_convert_format(folder_path, format_map[format_choice])
                        print("\n\033[92mBatch image conversion completed!\033[0m")
                    else:
                        print("\n\033[91mInvalid format choice!\033[0m")

            elif choice == '6':
                folder_path = list_files_and_select(is_folder=True)
                if folder_path:
                    output_pdf = input("\n\033[93mEnter the output PDF name (e.g., output.pdf): \033[0m")
                    if not output_pdf.endswith('.pdf'):
                        output_pdf += '.pdf'
                    show_progress(1.0)
                    ImageHandler.images_to_pdf_with_filenames(folder_path, output_pdf)
                    print("\n\033[92mImages to PDF conversion completed!\033[0m")

            elif choice == '0':
                break

            input("\nPress Enter to continue...")

        except Exception as e:
            logging.error(f"Error in image menu: {str(e)}")
            print(f"\n\033[91mAn error occurred: {str(e)}\033[0m")
            input("\nPress Enter to continue...")

def excel_menu():
    """Submenu for Excel operations"""
    while True:
        clear_screen()
        print("\n\033[95m=== Excel Tools ===\033[0m")
        print("\033[92m1. Merge Workbooks (Separate Sheets)\033[0m")
        print("\033[92m2. Merge Worksheets (Single Sheet)\033[0m")
        print("\033[92m3. Excel to CSV Conversion\033[0m")
        print("\033[92m4. CSV to Excel Conversion\033[0m")
        print("\033[92m0. Back to Main Menu\033[0m")

        choice = input("\n\033[93mEnter your choice (0-4): \033[0m")

        try:
            if choice in ['1', '2']:
                folder_path = list_files_and_select(is_folder=True)
                if folder_path:
                    show_progress(0.5)
                    if choice == '1':
                        ExcelTool.merge_workbook(folder_path)
                        print("\n\033[92mWorkbooks merged successfully!\033[0m")
                    else:
                        ExcelTool.merge_worksheet(folder_path)
                        print("\n\033[92mWorksheets merged successfully!\033[0m")

            elif choice == '3':
                excel_path = list_files_and_select('.xlsx')
                if excel_path:
                    show_progress(0.3)
                    ExcelTool.excel_to_csv(excel_path)
                    print("\n\033[92mExcel to CSV conversion completed!\033[0m")

            elif choice == '4':
                csv_path = list_files_and_select('.csv')
                if csv_path:
                    show_progress(0.3)
                    ExcelTool.csv_to_excel(csv_path)
                    print("\n\033[92mCSV to Excel conversion completed!\033[0m")

            elif choice == '0':
                break

            input("\nPress Enter to continue...")

        except Exception as e:
            logging.error(f"Error in Excel menu: {str(e)}")
            print(f"\n\033[91mAn error occurred: {str(e)}\033[0m")
            input("\nPress Enter to continue...")

def file_management_menu():
    """Submenu for file management operations"""
    while True:
        clear_screen()
        print("\n\033[95m=== File Management ===\033[0m")
        print("\033[92m1. List Files in Directory\033[0m")
        print("\033[92m2. Create New Directory\033[0m")
        print("\033[92m3. Delete Files/Directories\033[0m")
        print("\033[92m4. Rename Files/Directories\033[0m")
        print("\033[92m0. Back to Main Menu\033[0m")

        choice = input("\n\033[93mEnter your choice (0-4): \033[0m")

        try:
            if choice == '1':
                path = input("\nEnter directory path (or press Enter for current directory): ").strip() or '.'
                print("\nFiles and directories:")
                for item in os.listdir(path):
                    print(f"  {'[DIR]' if os.path.isdir(os.path.join(path, item)) else '[FILE]'} {item}")

            elif choice == '2':
                dir_name = input("\nEnter new directory name: ")
                os.makedirs(dir_name, exist_ok=True)
                print(f"\n\033[92mDirectory '{dir_name}' created successfully!\033[0m")

            elif choice == '3':
                path = input("\nEnter path to delete: ")
                if os.path.exists(path):
                    if os.path.isdir(path):
                        os.rmdir(path)
                        print(f"\n\033[92mDirectory '{path}' deleted successfully!\033[0m")
                    else:
                        os.remove(path)
                        print(f"\n\033[92mFile '{path}' deleted successfully!\033[0m")
                else:
                    print("\n\033[91mPath does not exist!\033[0m")

            elif choice == '4':
                old_name = input("\nEnter current name: ")
                new_name = input("Enter new name: ")
                os.rename(old_name, new_name)
                print(f"\n\033[92mRenamed successfully!\033[0m")

            elif choice == '0':
                break

            input("\nPress Enter to continue...")

        except Exception as e:
            logging.error(f"Error in file management: {str(e)}")
            print(f"\n\033[91mAn error occurred: {str(e)}\033[0m")
            input("\nPress Enter to continue...")

def show_about():
    """Display information about the application"""
    clear_screen()
    print("\n\033[95m=== About TaskMaster ===\033[0m")
    print("\n\033[92mVersion: 0.2")
    print("Author: Bhikan Deshmukh")
    print("\nTaskMaster is a versatile file management and processing tool that helps you:")
    print("  • Manage PDF files (split, merge, remove blank pages)")
    print("  • Handle image files (EXIF data management)")
    print("  • Process Excel files (merge workbooks and worksheets)")
    print("  • Perform basic file management operations")
    print("\nFor more information, visit: https://instagram.com/bhikan_deshmukh\033[0m")
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\033[92mProgram terminated by user. Goodbye!\033[0m")
        logging.info("Program terminated by keyboard interrupt")
    except Exception as e:
        logging.critical(f"Unexpected error: {str(e)}")
        print(f"\n\033[91mAn unexpected error occurred: {str(e)}\033[0m")
