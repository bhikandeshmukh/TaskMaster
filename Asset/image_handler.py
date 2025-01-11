import logging
from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path

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
        """Extract EXIF data from the image and save it to separate text files."""
        try:
            # Open the image file
            image = Image.open(image_path)
            exif_data = image._getexif()
            
            # Convert image_path to a Path object to use stem
            image_path_obj = Path(image_path)
            exif_output_file = f"{image_path_obj.stem}_exif_data.txt"
            gps_output_file = f"{image_path_obj.stem}_gps_data.txt"
            
            # Check if EXIF data is found
            if exif_data:
                logging.info("EXIF data found.")
                
                gps_data = {}
                
                # Loop through EXIF data
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    # Log only the tag name, not the value
                    # logging.info(f"Tag: {tag_name}, Value: {value}")  # This line is commented out
                
                    if tag_name == 'GPSInfo':
                        gps_data = value  # Store GPS info if found
                
                # Save the EXIF data to a text file
                with open(exif_output_file, 'w') as f:
                    for tag, value in exif_data.items():
                        tag_name = TAGS.get(tag, tag)
                        f.write(f"{tag_name}: {value}\n")  # Save all EXIF data
                
                logging.info(f"EXIF data saved to {exif_output_file}")

                # Save the GPS data to a separate text file
                with open(gps_output_file, 'w') as f:
                    f.write(str(gps_data))  # Save only GPS data
                
                logging.info(f"GPS data saved to {gps_output_file}")
            else:
                logging.info("No EXIF data found.")
        except Exception as e:
            logging.error(f"Error extracting EXIF data: {e}")

    @staticmethod
    def remove_exif_data(image_path):
        """Remove EXIF data from the image and overwrite the original file."""
        try:
            # Open the image file
            image = Image.open(image_path)

            # Save the image without EXIF data, overwriting the original file
            image.save(image_path, "JPEG")  # Overwriting original file with the same name
            
            logging.info(f"EXIF data removed from {image_path}.")
            print(f"EXIF data removed from {image_path}.")
        except Exception as e:
            logging.error(f"Error removing EXIF data: {e}")
            print(f"Error removing EXIF data: {e}")

# Example of how to use the class (uncomment the following lines to test):
# if __name__ == "__main__":
#     handler = ImageHandler()
#     handler.main_menu()
