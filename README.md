# TaskMaster

**TaskMaster** is a versatile tool for managing PDF, image, and Excel files. It allows users to split and merge PDFs, extract EXIF data from images, and merge multiple Excel/CSV files into organized workbooks or worksheets. Ideal for data analysts, it streamlines data consolidation and enhances productivity with user-friendly functionality.

## Features

- **PDF Handling**:
  - Split a PDF into individual pages.
  - Merge multiple PDFs into a single document.
  - Remove blank pages from a PDF.

- **Image Handling**:
  - Extract EXIF data from image files.
  
- **Excel Processing**:
  - Merge multiple Excel and CSV files into separate sheets within a single workbook.
  - Combine multiple Excel and CSV files into a single worksheet.

## Prerequisites

Before using TaskMaster, ensure you have the following installed:
- Python 3.x
- Required Python packages:
  - pandas
  - xlsxwriter
  - PyPDF2
  - Pillow

You can install the required packages using pip:

```bash
pip install pandas xlsxwriter PyPDF2 Pillow
```

Getting Started
Step 1: Clone the Repository
Clone this repository to your local machine using:

```bash
git clone https://github.com/yourusername/TaskMaster.git
cd TaskMaster
```
Step 2: Navigate to the Project Directory
Make sure you are in the TaskMaster directory where the main.py file is located.

Step 3: Prepare Your Data
Organize your PDF, image, and Excel/CSV files in appropriate folders. For Excel processing, ensure your files are located in a single folder.

Step 4: Run the Application
Run the application by executing the following command in your terminal:

```bash
python3 main.py
```
Step 5: Use the Tool
Upon running the application, you will see a menu with several options. Follow the prompts for each task:

1 PDF Split: Select a PDF file to split it into individual pages.
2 PDF Merge: Choose a folder containing PDF files to merge them into one document.
3 PDF Blank Page Remove: Select a PDF file to remove any blank pages.
4 Image Data Extract: Select an image file to extract its EXIF data.
5 Excel Tool: Choose a folder containing Excel or CSV files to:
  Merge them into a single workbook with separate sheets for each file.
  Combine them into a single worksheet.
6 Exit: Choose this option to exit the application.

Step 6: Check the Output
After performing Excel operations, check the Output folder in your project directory for the results. You will find:

merged_workbook.xlsx: Contains each file in a separate sheet.
merged_worksheet.xlsx: Contains all data combined into a single worksheet.
Contribution
If you'd like to contribute to TaskMaster, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the open-source community for their valuable libraries and tools.

