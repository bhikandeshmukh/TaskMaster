import os  # Ensure os is imported
from pathlib import Path  # Import pathlib for path handling
import logging
import pikepdf  
import img2pdf
from PIL import Image

class PDFHandler:
    @staticmethod
    def split(pdf_path):
        try:
            output_folder = Path('Output/split_pdfs')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            pdf = pikepdf.Pdf.open(pdf_path)
            for i, page in enumerate(pdf.pages):
                new_pdf = pikepdf.Pdf.new()
                new_pdf.pages.append(page)
                output_path = output_folder / f"{Path(pdf_path).stem}_page_{i + 1}.pdf"
                new_pdf.save(output_path)
            
            logging.info(f"PDF split into {len(pdf.pages)} files.")
            return True
        except Exception as e:
            logging.error(f"Error splitting PDF: {e}")
            raise

    @staticmethod
    def merge(folder_path):
        try:
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            pdf_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.pdf')])
            
            if not pdf_files:
                raise ValueError("No PDF files found in the specified folder")

            merged_pdf = pikepdf.Pdf.new()
            
            for filename in pdf_files:
                file_path = Path(folder_path) / filename
                try:
                    pdf = pikepdf.Pdf.open(file_path)
                    merged_pdf.pages.extend(pdf.pages)
                except Exception as e:
                    logging.warning(f"Skipping {filename} due to error: {e}")
                    continue

            if len(merged_pdf.pages) > 0:
                output_path = output_folder / "merged.pdf"
                merged_pdf.save(output_path)
                logging.info(f"PDFs merged successfully. Output saved to {output_path}")
                return True
            else:
                raise ValueError("No valid PDF pages found to merge")
                
        except Exception as e:
            logging.error(f"Error merging PDFs: {e}")
            raise

    @staticmethod
    def remove_blank(pdf_path):
        try:
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            pdf = pikepdf.Pdf.open(pdf_path)
            new_pdf = pikepdf.Pdf.new()
            
            for page in pdf.pages:
                if not page.is_blank:
                    new_pdf.pages.append(page)

            output_path = output_folder / f"{Path(pdf_path).stem}_no_blanks.pdf"
            new_pdf.save(output_path)

            logging.info(f"Blank pages removed successfully. Output saved to {output_path}")
            return True
        except Exception as e:
            logging.error(f"Error removing blank pages: {e}")
            raise

    @staticmethod
    def compress_pdf(pdf_path):
        try:
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            pdf = pikepdf.Pdf.open(pdf_path)
            output_path = output_folder / f"{Path(pdf_path).stem}_compressed.pdf"
            
            pdf.save(output_path, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)

            logging.info(f"PDF compressed successfully. Output saved to {output_path}")
            return True
        except Exception as e:
            logging.error(f"Error compressing PDF: {e}")
            raise

    @staticmethod
    def images_to_pdf(image_folder):
        try:
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            image_files = []
            for ext in ('*.jpg', '*.jpeg', '*.png'):
                image_files.extend(Path(image_folder).glob(ext))
            
            if not image_files:
                raise ValueError("No image files found in the specified folder")

            output_path = output_folder / "images_combined.pdf"
            with open(output_path, "wb") as f:
                f.write(img2pdf.convert([str(img) for img in sorted(image_files)]))

            logging.info(f"Images converted to PDF successfully. Output saved to {output_path}")
            return True
        except Exception as e:
            logging.error(f"Error converting images to PDF: {e}")
            raise
