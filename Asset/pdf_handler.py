import os  # Ensure os is imported
from pathlib import Path  # Import pathlib for path handling
import logging
from PyPDF2 import PdfReader, PdfWriter

class PDFHandler:
    @staticmethod
    def split(pdf_path):
        try:
            reader = PdfReader(pdf_path)
            for i, page in enumerate(reader.pages):
                writer = PdfWriter()
                writer.add_page(page)
                output_path = f"{pdf_path.stem}_page_{i + 1}.pdf"
                with open(output_path, 'wb') as output_pdf:
                    writer.write(output_pdf)
            logging.info(f"PDF split into {len(reader.pages)} files.")
        except Exception as e:
            logging.error(f"Error splitting PDF: {e}")

    @staticmethod
    def merge(folder_path):
        try:
            output_folder = Path('Output')  # Use pathlib for the output folder path
            output_folder.mkdir(parents=True, exist_ok=True)  # Create Output directory if it doesn't exist
            writer = PdfWriter()

            # Loop through all PDF files in the provided folder path
            for filename in os.listdir(folder_path):
                if filename.endswith(".pdf"):
                    file_path = Path(folder_path) / filename  # Use Path to join paths
                    reader = PdfReader(file_path)
                    for page in reader.pages:
                        writer.add_page(page)

            # Define the output path using pathlib
            output_path = output_folder / "merged.pdf"
            with open(output_path, 'wb') as output_pdf:
                writer.write(output_pdf)

            logging.info(f"PDFs merged successfully. Output saved to {output_path}")
        except Exception as e:
            logging.error(f"Error merging PDFs: {e}")

    @staticmethod
    def remove_blank(pdf_path):
        try:
            reader = PdfReader(pdf_path)
            writer = PdfWriter()
            for page in reader.pages:
                if page.extract_text().strip():  # If page has text
                    writer.add_page(page)

            # Set the output path to the Output directory
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)  # Create Output directory if it doesn't exist
            output_path = output_folder / f"{pdf_path.stem}_no_blanks.pdf"
            
            with open(output_path, 'wb') as output_pdf:
                writer.write(output_pdf)

            logging.info(f"Blank pages removed successfully. Output saved to {output_path}")
        except Exception as e:
            logging.error(f"Error removing blank pages: {e}")
