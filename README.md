# TaskMaster

**TaskMaster** is a comprehensive file management tool designed to handle PDF, image, and Excel files efficiently. It provides a user-friendly interface for various file operations and data processing tasks.

## Key Features

### 1. PDF Tools
- Split PDF into individual pages
- Merge multiple PDFs
- Remove blank pages
- PDF compression
- Convert images to PDF

### 2. Image Tools
- Extract EXIF data
- Remove EXIF data
- Image compression
- Image format conversion
- Image resizing

### 3. Excel Tools
- Merge workbooks (separate sheets)
- Merge worksheets (single sheet)
- Excel to CSV conversion
- CSV to Excel conversion
- Excel file formatting

### 4. File Management
- List files and directories
- Create new directories
- Delete files/directories
- Rename files/directories

## Requirements

Install required packages:

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pikepdf img2pdf Pillow pandas openpyxl xlsxwriter tqdm
```

## Installation & Usage

1. Clone the repository:
```bash
git clone https://github.com/bhikandeshmukh/TaskMaster.git
cd TaskMaster
```

2. Run the program:
```bash
python main.py
```

3. Select options from the menu and follow the prompts.

## Output
All processed files will be saved in the `Output` folder.

## File Structure
```
TaskMaster/
├── main.py                     # Main application file
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
├── Output/                     # Result storage
└── Asset/
    ├── pdf_handler.py         # PDF processing
    ├── image_handler.py       # Image processing
    ├── excel_tool.py          # Excel processing
    └── utils.py               # Utility functions
```

## Error Handling
- The application includes comprehensive error handling
- All operations are logged in `Output/log.log`
- User-friendly error messages are displayed

## Contributing
Bug reports and feature requests are welcome. Please feel free to submit issues and pull requests.

## License
MIT License

## Author
- Created by: Bhikan Deshmukh
- Instagram: @bhikan_deshmukh

## Version
Current Version: 0.2

