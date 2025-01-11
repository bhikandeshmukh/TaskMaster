import os
import pandas as pd
from pathlib import Path
import logging

class ExcelTool:
    @staticmethod
    def main_menu(folder_path=None):
        """Main menu for merging Excel files with two options."""
        while True:
            print("\nSelect an option:")
            print("1. Merge Workbook (Separate sheets)")
            print("2. Merge Worksheet (Single sheet)")
            print("0. Exit to Main Menu")
            
            choice = input("Enter the number of the option: ").strip()

            if choice == '1':
                if folder_path:
                    ExcelTool.merge_workbook(folder_path)
                else:
                    print("No folder selected. Please select a folder first.")

            elif choice == '2':
                if folder_path:
                    ExcelTool.merge_worksheet(folder_path)
                else:
                    print("No folder selected. Please select a folder first.")

            elif choice == '0':
                break  # Exit back to the main menu

            else:
                print("Invalid choice. Please enter a valid option.")

    @staticmethod
    def merge_workbook(folder_path):
        """Merge all Excel/CSV files in the folder into one workbook with separate sheets for each file."""
        try:
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            output_path = output_folder / "merged_workbook.xlsx"

            with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
                for idx, file_name in enumerate(os.listdir(folder_path)):
                    file_path = os.path.join(folder_path, file_name)
                    if file_name.endswith('.csv') or file_name.endswith('.xlsx'):
                        sheet_name = Path(file_name).stem

                        # Ensure sheet name is <= 31 characters
                        if len(sheet_name) > 31:
                            sheet_name = sheet_name[:28] + f"_{idx + 1}"

                        # Try reading the file with different encodings for CSV files
                        if file_name.endswith('.csv'):
                            df = ExcelTool.read_csv_with_encoding(file_path)
                        else:
                            df = pd.read_excel(file_path)

                        df['Source File'] = file_name
                        df.to_excel(writer, sheet_name=sheet_name, index=False)
                        logging.info(f"Added {file_name} as sheet {sheet_name}")

            print(f"Workbook merged successfully at {output_path}")
            logging.info("All files merged into workbook successfully.")
        except Exception as e:
            logging.error(f"Error in merging workbook: {e}")
            print(f"Error in merging workbook: {e}")

    @staticmethod
    def merge_worksheet(folder_path):
        """Merge all Excel/CSV files in the folder into a single worksheet in one workbook."""
        try:
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            output_path = output_folder / "merged_worksheet.xlsx"
            combined_df = pd.DataFrame()
            
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if file_name.endswith('.csv') or file_name.endswith('.xlsx'):
                    # Try reading the file with different encodings for CSV files
                    df = ExcelTool.read_csv_with_encoding(file_path) if file_name.endswith('.csv') else pd.read_excel(file_path)

                    df['Source File'] = file_name
                    combined_df = pd.concat([combined_df, df], ignore_index=True)
                    logging.info(f"Merged {file_name} into single worksheet")

            combined_df.to_excel(output_path, sheet_name="Sheet1", index=False)

            print(f"Worksheet merged successfully at {output_path}")
            logging.info("All files merged into single worksheet successfully.")
        except Exception as e:
            logging.error(f"Error in merging worksheet: {e}")
            print(f"Error in merging worksheet: {e}")

    @staticmethod
    def read_csv_with_encoding(file_path):
        """Try reading a CSV file with various encodings."""
        encodings = ['utf-8', 'ISO-8859-1', 'latin1', 'utf-16']
        for encoding in encodings:
            try:
                return pd.read_csv(file_path, encoding=encoding)
            except UnicodeDecodeError:
                continue  # Try the next encoding
        # If all encodings fail, raise an error
        raise UnicodeDecodeError(f"Could not decode {file_path} with available encodings.")
