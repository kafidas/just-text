# PDF Text Extraction for et.gr (Edition 2024)
This Python script is designed to process PDF files from **et.gr**, specifically targeting Issues A' that contain formal laws. <br>
It extracts readable text from multiple PDF files of **et.gr** stored in a folder, and saving the results in specified output subfolder. <br>
The script processes the PDFs by cleaning up headers, last page footers, and other metadata, and it also handles special cases like hyphenation at the end of lines and omitted final lines. <br>
The output includes the full extracted text, clipped text (headers removed), and the content from the last page (for reference).

<br>
<hr>
<br>

### Key Features:
#### Extracts Text from PDF:
- Removes header content based on patterns (typically the first 3 lines of each page).
- Handles hyphenation by merging lines that end with a hyphen.
- Removes blank lines and lines starting with "Verified" from the text.
- Handles last-page-specific conditions to ensure relevant text is captured.
- Handles non-standard page sizes.
#### Outputs:
- Main body of law - Full extracted text (`.txt`)
- Text that is trimmed - Clipped text (`_trims.txt`)
- Last page for reference checks (`_last_page.txt`)

<br>

### Breakdown of Functions:
#### extract_text_from_pdf(pdf_path):
Extracts and processes text from the PDF, removing header, dealing with hyphenation, and handling last page text separately.
#### process_pdfs_in_folder(input_folder, output_folder):
Iterates over all PDF files in the input_folder, extracting text and images (if present), and saving them in the output_folder.

<br>

### Usage:
- Make sure all necessary libraries (fitz, PIL, etc.) are installed for the script to work.
- Place your PDF files in the pdf_files folder.
- Running the script will generate output in the pdf_files/extracted_text_files folder.
- For each PDF, the script will generate:
-- <filename>.txt (full extracted text)
-- <filename>_trims.txt (clipped text with headers and footers removed)
-- <filename>_last_page.txt (text from the last page)
# Example
If you have a PDF named example.pdf in the pdf_files folder, the output will be:<br>
- example.txt (full text)
- example_trims.txt (clipped text)
- example_last_page.txt (text from the last page)

<br>

## Requirements
- Python 3.x
- Libraries:
-- PyMuPDF (fitz): For reading PDF files, extracting text, and handling images.
-- Pillow (PIL): For saving extracted images in JPEG format.
-- re: For regular expression-based text processing.
-- os: For handling file paths.

Developed/Edited by: Lampros KAFIDAS
