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
            writer = PdfWriter()
            for filename in os.listdir(folder_path):
                if filename.endswith(".pdf"):
                    reader = PdfReader(os.path.join(folder_path, filename))
                    for page in reader.pages:
                        writer.add_page(page)
            with open(os.path.join(folder_path, "merged.pdf"), 'wb') as output_pdf:
                writer.write(output_pdf)
            logging.info("PDFs merged successfully.")
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
            output_path = f"{pdf_path.stem}_no_blanks.pdf"
            with open(output_path, 'wb') as output_pdf:
                writer.write(output_pdf)
            logging.info("Blank pages removed successfully.")
        except Exception as e:
            logging.error(f"Error removing blank pages: {e}")
