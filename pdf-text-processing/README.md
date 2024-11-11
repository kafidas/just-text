This Python script is designed to process PDF files from et.gr of Greek Laws (FEK A) in a folder, extracting text (and optionally images), and saving the results in specified output folders. <br>
It is tested only for Laws published in Issues A (thus far!)
<br>
<hr>
<br>

### Key Features:
#### Extracts Text from PDF:
- Removes header content based on patterns (typically the first 3 lines of each page).
- Handles hyphenation by merging lines that end with a hyphen.
- Removes blank lines and lines starting with "Verified" from the text.
- Handles last-page-specific conditions to ensure relevant text is captured.
#### Extracts Images (optional):
- Detects and extracts images embedded in the PDF pages.
- Saves the extracted images to a subfolder as JPEG files.
#### Outputs:
- Main body of law
- Text that is trimmed
- Last page for reference checks

<br>

### Breakdown of Functions:
#### extract_text_from_pdf(pdf_path):
Extracts and processes text from the PDF, removing header, dealing with hyphenation, and handling last page text separately.
#### extract_images_from_pdf(pdf_path, output_folder):
Extracts images from each page and saves them as JPEGs.
#### process_pdfs_in_folder(input_folder, output_folder):
Iterates over all PDF files in the input_folder, extracting text and images (if present), and saving them in the output_folder.

<br>

### Usage:
- Place your PDF files in the pdf_files folder.
- The script will generate output in the pdf_files/extracted_text_files folder.
- Make sure all necessary libraries (fitz, PIL, etc.) are installed for the script to work.

<br>

### Main libraries used:
- PyMuPDF (fitz): For reading PDF files, extracting text, and handling images.
- Pillow (PIL): For saving extracted images in JPEG format.
- re: For regular expression-based text processing.
- os and time: For handling file paths and controlling the timing of operations.
