# TaskMaster

A versatile file management and processing tool that helps you handle PDFs, images, and Excel files efficiently.

## Features

### 1. PDF Tools
- Split PDF into separate pages
- Merge multiple PDFs
- Remove blank pages
- Compress PDF files
- Convert images to PDF

### 2. Image Tools
- Extract EXIF data
- Remove EXIF data
- Compress images
- Convert image formats
- Resize images
- Batch image conversion
- Images to PDF with filenames

### 3. Excel Tools
- Merge workbooks (separate sheets)
- Merge worksheets (single sheet)
- Convert Excel to CSV
- Convert CSV to Excel
- Format Excel files

### 4. File Management
- List files and directories
- Create new directories
- Delete files/directories
- Rename files/directories

## Technical Specifications

### File Support
- **PDF**: .pdf files
- **Images**: .jpg, .jpeg, .png, .bmp, .tiff
- **Excel**: .xlsx, .csv

### UI Features
- Color-coded menu interface
- Progress bar for operations
- Clear screen functionality
- Interactive file selection

### Error Handling
- Comprehensive exception handling
- User-friendly error messages
- Logging of all errors
- Graceful exit handling

## Project Structure
```
TaskMaster/
├── main.py                     # Main application file
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
├── Output/                     # Folder for result data storage
└── Asset/
    ├── pdf_handler.py          # PDF processing functions
    ├── image_handler.py        # Image processing functions
    ├── excel_tool.py          # Excel processing functions
    └── utils.py               # Common utility functions
```

## Dependencies
- pikepdf: PDF manipulation
- PIL (Pillow): Image processing
- pandas: Excel/CSV handling
- openpyxl: Excel formatting
- img2pdf: Image to PDF conversion
- tqdm: Progress bar functionality

## System Requirements
- Python 3.x
- Windows/Linux/MacOS compatible
- Minimum 512MB RAM
- Storage space as per usage

## Installation

1. Clone this repository:
```bash
git clone https://github.com/bhikandeshmukh/TaskMaster.git
cd TaskMaster
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the main script:
```bash
python main.py
```

2. Use the interactive menu to:
   - Select the tool category (PDF, Image, Excel, File Management)
   - Choose specific operation
   - Follow on-screen instructions

## Output and Logging
- All processed files are saved in the `Output` directory
- Operation logs are stored in `Output/log.log`
- Log format: timestamp - level - message
- Log levels: INFO, ERROR, CRITICAL

## Author
- **Name**: Bhikan Deshmukh
- **Contact**: https://instagram.com/bhikan_deshmukh
- **Version**: 0.2

## License
This project is proprietary software. All rights reserved.

## Contributing
For major changes, please open an issue first to discuss what you would like to change.

## Support
If you encounter any issues or need assistance:
1. Check the log file at `Output/log.log`
2. Contact the author through Instagram
3. Open an issue in the repository

