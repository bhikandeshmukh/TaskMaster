import logging
from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path
import os

class ImageHandler:
    @staticmethod
    def main_menu():
        """Main menu to select action: extract or remove EXIF data."""
        while True:
            print("\nSelect an option:")
            print("1. Extract EXIF data")
            print("2. Remove EXIF data")
            print("0. Exit")

            choice = input("Enter the number of the option: ")

            if choice == '1':
                image_path = input("Enter the path of the image to extract EXIF data: ")
                ImageHandler.extract_data(image_path)
            elif choice == '2':
                image_path = input("Enter the path of the image to remove EXIF data: ")
                ImageHandler.remove_exif_data(image_path)
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    @staticmethod
    def extract_data(image_path):
        try:
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            image = Image.open(image_path)
            exif_data = image._getexif()
            
            image_path_obj = Path(image_path)
            output_path = output_folder / f"{image_path_obj.stem}_exif_data.txt"
            
            if exif_data:
                with open(output_path, 'w', encoding='utf-8') as f:
                    for tag_id in exif_data:
                        tag = TAGS.get(tag_id, tag_id)
                        data = exif_data.get(tag_id)
                        f.write(f"{tag}: {data}\n")
                
                logging.info(f"EXIF data saved to {output_path}")
                return True
            else:
                logging.info("No EXIF data found")
                return False
        except Exception as e:
            logging.error(f"Error extracting EXIF data: {e}")
            raise

    @staticmethod
    def remove_exif_data(image_path):
        try:
            output_folder = Path('Output')
            output_folder.mkdir(parents=True, exist_ok=True)
            
            image = Image.open(image_path)
            data = list(image.getdata())
            image_without_exif = Image.new(image.mode, image.size)
            image_without_exif.putdata(data)
            
            output_path = output_folder / f"{Path(image_path).stem}_no_exif{Path(image_path).suffix}"
            image_without_exif.save(output_path)
            
            logging.info(f"EXIF data removed. Image saved to {output_path}")
            return True
        except Exception as e:
            logging.error(f"Error removing EXIF data: {e}")
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

# Example of how to use the class (uncomment the following lines to test):
# if __name__ == "__main__":
#     handler = ImageHandler()
#     handler.main_menu()
