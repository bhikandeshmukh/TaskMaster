import logging
from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS
from pathlib import Path
import os
from fpdf import FPDF

class ImageHandler:
    @staticmethod
    def main_menu():
        """Main menu to select action: extract or remove EXIF data."""
        while True:
            print("\n\033[95m=== Image Tools ===\033[0m")
            print("\033[92m1. Extract EXIF data\033[0m")
            print("\033[92m2. Remove EXIF data\033[0m")
            print("\033[92m3. Batch Convert Images\033[0m")
            print("\033[92m4. Bulk Images to PDF\033[0m")
            print("\033[92m0. Back to Main Menu\033[0m")

            choice = input("\n\033[93mEnter your choice (0-4): \033[0m")

            if choice == '1':
                image_path = list_files_and_select(('.jpg', '.jpeg', '.png'))
                if image_path:
                    ImageHandler.extract_data(image_path)
            elif choice == '2':
                image_path = list_files_and_select(('.jpg', '.jpeg', '.png'))
                if image_path:
                    ImageHandler.remove_exif_data(image_path)
            elif choice == '3':
                folder_path = list_files_and_select(is_folder=True)
                if folder_path:
                    print("\n\033[92mChoose output format:\033[0m")
                    print("\033[92m1. JPEG\033[0m")
                    print("\033[92m2. JPG\033[0m")
                    print("\033[92m3. PNG\033[0m")
                    format_choice = input("\n\033[93mEnter the number corresponding to the format: \033[0m").strip()
                    format_map = {"1": "jpeg", "2": "jpg", "3": "png"}
                    if format_choice in format_map:
                        ImageHandler.batch_convert_format(folder_path, format_map[format_choice])
                    else:
                        print("\n\033[91mInvalid format choice!\033[0m")
            elif choice == '4':
                folder_path = list_files_and_select(is_folder=True)
                if folder_path:
                    output_pdf = input("\n\033[93mEnter the output PDF name (e.g., output.pdf): \033[0m")
                    if not output_pdf.endswith('.pdf'):
                        output_pdf += '.pdf'
                    ImageHandler.images_to_pdf_with_filenames(folder_path, output_pdf)
            elif choice == '0':
                break
            else:
                print("\n\033[91mInvalid choice. Please enter a valid option.\033[0m")

    @staticmethod
    def extract_data(image_path):
        try:
            output_folder = Path('Output/EXIF_Data')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            image = Image.open(image_path)
            exif_data = image._getexif()
            
            output_path = output_folder / f"{Path(image_path).stem}_exif_data.txt"
            
            if exif_data:
                with open(output_path, 'w', encoding='utf-8') as f:
                    for tag_id in exif_data:
                        tag = TAGS.get(tag_id, tag_id)
                        data = exif_data.get(tag_id)
                        f.write(f"{tag}: {data}\n")
                
                logging.info(f"EXIF data saved to {output_path}")
                print(f"\n\033[92m✔ EXIF data extracted to: {output_path}\033[0m")
                return True
            else:
                print("\n\033[93m⚠ No EXIF data found in the image\033[0m")
                return False
        except Exception as e:
            logging.error(f"Error extracting EXIF data: {e}")
            print(f"\n\033[91m❌ Error extracting EXIF data: {e}\033[0m")
            raise

    @staticmethod
    def remove_exif_data(image_path):
        try:
            output_folder = Path('Output/Clean_Images')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            image = Image.open(image_path)
            data = list(image.getdata())
            image_without_exif = Image.new(image.mode, image.size)
            image_without_exif.putdata(data)
            
            output_path = output_folder / f"{Path(image_path).stem}_no_exif{Path(image_path).suffix}"
            image_without_exif.save(output_path)
            
            logging.info(f"EXIF data removed from {image_path}")
            print(f"\n\033[92m✔ Image saved without EXIF data: {output_path}\033[0m")
            return True
        except Exception as e:
            logging.error(f"Error removing EXIF data: {e}")
            print(f"\n\033[91m❌ Error removing EXIF data: {e}\033[0m")
            raise

    @staticmethod
    def compress_image(image_path, quality=85):
        try:
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            image = Image.open(image_path)
            output_path = output_folder / f"{Path(image_path).stem}_compressed{Path(image_path).suffix}"
            
            image.save(output_path, quality=quality, optimize=True)
            
            logging.info(f"Image compressed and saved to {output_path}")
            return True
        except Exception as e:
            logging.error(f"Error compressing image: {e}")
            raise

    @staticmethod
    def convert_format(image_path, target_format='PNG'):
        try:
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            image = Image.open(image_path)
            target_format = target_format.upper()
            
            if image.mode in ('RGBA', 'LA') and target_format == 'JPEG':
                # Convert RGBA to RGB for JPEG
                image = image.convert('RGB')
            
            output_path = output_folder / f"{Path(image_path).stem}.{target_format.lower()}"
            image.save(output_path, target_format)
            
            logging.info(f"Image converted and saved to {output_path}")
            return True
        except Exception as e:
            logging.error(f"Error converting image format: {e}")
            raise

    @staticmethod
    def resize_image(image_path, width=None, height=None):
        try:
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            image = Image.open(image_path)
            original_width, original_height = image.size
            
            if width and height:
                new_size = (width, height)
            elif width:
                ratio = width / original_width
                new_size = (width, int(original_height * ratio))
            elif height:
                ratio = height / original_height
                new_size = (int(original_width * ratio), height)
            else:
                raise ValueError("Either width or height must be specified")
            
            resized_image = image.resize(new_size, Image.LANCZOS)
            output_path = output_folder / f"{Path(image_path).stem}_resized{Path(image_path).suffix}"
            resized_image.save(output_path)
            
            logging.info(f"Image resized and saved to {output_path}")
            return True
        except Exception as e:
            logging.error(f"Error resizing image: {e}")
            raise

    @staticmethod
    def batch_convert_format(input_folder, output_format):
        try:
            output_folder = Path('Output/Converted_Images')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            supported_formats = ('.png', '.jpg', '.jpeg')
            input_files = [f for f in os.listdir(input_folder) 
                         if f.lower().endswith(supported_formats)]

            if not input_files:
                print("\n\033[93m⚠ No supported image files found in the folder\033[0m")
                return False

            for filename in input_files:
                file_path = Path(input_folder) / filename
                try:
                    with Image.open(file_path) as img:
                        img = img.convert("RGB")
                        new_filename = f"{Path(filename).stem}.{output_format}"
                        output_path = output_folder / new_filename
                        
                        img.save(output_path, output_format.upper(), quality=100)
                        logging.info(f"Converted: {file_path} → {output_path}")
                        print(f"\033[92m✔ {filename} → {new_filename}\033[0m")
                        
                except Exception as e:
                    logging.error(f"Error converting {file_path}: {e}")
                    print(f"\033[91m❌ Error converting {filename}: {e}\033[0m")
            
            return True
        except Exception as e:
            logging.error(f"Error in batch conversion: {e}")
            print(f"\n\033[91m❌ Error in batch conversion: {e}\033[0m")
            raise

    @staticmethod
    def images_to_pdf_with_filenames(folder_path, output_pdf):
        try:
            output_folder = Path('Output/PDF_Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            temp_folder = output_folder / "temp"
            temp_folder.mkdir(exist_ok=True)
            
            output_pdf_path = output_folder / output_pdf
            
            # Initialize PDF with A4 dimensions
            A4_WIDTH, A4_HEIGHT = 595.28, 841.89
            pdf = FPDF(unit="pt", format="A4")
            font = ImageFont.load_default()

            image_files = [f for f in os.listdir(folder_path) 
                         if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff"))]

            if not image_files:
                print("\n\033[93m⚠ No supported image files found in the folder\033[0m")
                return False

            try:
                for image_file in sorted(image_files):
                    image_path = Path(folder_path) / image_file
                    print(f"\033[92m✔ Processing: {image_file}\033[0m")

                    with Image.open(image_path) as img:
                        # Scale image to fit A4
                        img_ratio = img.width / img.height
                        a4_ratio = A4_WIDTH / (A4_HEIGHT - 40)

                        if img_ratio > a4_ratio:
                            new_width = A4_WIDTH
                            new_height = int(A4_WIDTH / img_ratio)
                        else:
                            new_height = A4_HEIGHT - 40
                            new_width = int((A4_HEIGHT - 40) * img_ratio)

                        img_resized = img.resize((int(new_width), int(new_height)), Image.LANCZOS)
                        
                        # Create page with filename
                        page = Image.new("RGB", (int(A4_WIDTH), int(A4_HEIGHT)), "white")
                        img_x = (A4_WIDTH - new_width) // 2
                        img_y = (A4_HEIGHT - new_height - 40) // 2
                        page.paste(img_resized, (int(img_x), int(img_y)))

                        # Add filename
                        draw = ImageDraw.Draw(page)
                        text = Path(image_file).stem
                        text_bbox = draw.textbbox((0, 0), text, font=font)
                        text_width = text_bbox[2] - text_bbox[0]
                        text_height = text_bbox[3] - text_bbox[1]
                        text_x = (A4_WIDTH - text_width) // 2
                        text_y = A4_HEIGHT - text_height - 20
                        draw.text((text_x, text_y), text, fill="black", font=font)

                        # Save temporary page
                        temp_path = temp_folder / f"temp_{Path(image_file).stem}.jpg"
                        page.save(temp_path, "JPEG", quality=95)
                        
                        # Add to PDF
                        pdf.add_page()
                        pdf.image(str(temp_path), 0, 0, A4_WIDTH, A4_HEIGHT)
                        temp_path.unlink()

                pdf.output(str(output_pdf_path))
                logging.info(f"PDF created: {output_pdf_path}")
                print(f"\n\033[92m✔ PDF created successfully: {output_pdf_path}\033[0m")
                return True

            finally:
                # Cleanup temporary files
                if temp_folder.exists():
                    for temp_file in temp_folder.glob("*.jpg"):
                        temp_file.unlink(missing_ok=True)
                    temp_folder.rmdir()

        except Exception as e:
            logging.error(f"Error creating PDF: {e}")
            print(f"\n\033[91m❌ Error creating PDF: {e}\033[0m")
            raise

# Example of how to use the class (uncomment the following lines to test):
# if __name__ == "__main__":
#     handler = ImageHandler()
#     handler.main_menu()
