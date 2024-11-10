import os
import fitz  # PyMuPDF
import re
import time
import logging

# Set up logging
logging.basicConfig(filename='pdf_processing.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        logging.error(f"Error opening {pdf_path}: {e}")
        return "", ""
    
    text = ""
    clipped_text = []  # Use a list to store clipped text for each page

    header_footer_texts = set()

    def merge_lines_if_hyphen(lines):
        merged_lines = []
        i = 0
        while i < len(lines) - 1:
            current_line = lines[i].strip()
            next_line = lines[i + 1].strip()
            if (len(current_line) > 1 and (current_line.endswith('-') or current_line.endswith('-\u000d \u000a') or current_line.endswith('-\u000d\u000a\u000d\u000a') or current_line.endswith('-\u000d\u000a')) and not current_line[-2].isspace()):
                if current_line.endswith('-'):
                    merged_lines.append(current_line[:-1] + next_line)
                else:
                    merged_lines.append(current_line[:-3] + next_line)
                i += 2
            else:
                merged_lines.append(current_line)
                i += 1
        
        if i < len(lines):
            merged_lines.append(lines[i].strip())
    
        return merged_lines

    for page_num in range(1, doc.page_count - 1):
        page = doc.load_page(page_num)
        page_text = page.get_text("text").split("\n")
        for line in page_text[:3]:
            header_footer_texts.add(line.strip())

    for page_num in range(doc.page_count - 1):
        page = doc.load_page(page_num)
        page_text = page.get_text("text").split("\n")

        if page_num == 0:
            exclusion_count = 0    
            inside_range = False
            filtered_text = []
            clipped_page_text = []

            for line in page_text:
                if "ΕΦΗΜΕΡΙΔΑ" in line or "ΕΦΗΜΕΡΙ∆Α" in line or "Digitally" in line:
                    inside_range = True
                if "Verified" in line or exclusion_count == 12 or "NOMOΣ" in line or "ΝΟΜΟΣ" in line:
                    inside_range = False

                if not inside_range:
                    filtered_text.append(line)
                else:
                    clipped_page_text.append(line)
                exclusion_count += 1

            clipped_text.append("\n".join(clipped_page_text))
            filtered_text = "\n".join(filtered_text)
        else:
            # Exclude lines containing "verified" (case-insensitive)
            filtered_text = "\n".join(line for line in page_text if line.strip() not in header_footer_texts)
            clipped_page_text = "\n".join(line for line in page_text if line.strip() in header_footer_texts)
            clipped_text.append(clipped_page_text)

        # Merge lines that end with a hyphen and are not followed by a space
        lines = filtered_text.split("\n")
        merged_lines = merge_lines_if_hyphen(lines)
        filtered_text = "\n".join(merged_lines)
        
        # Remove lines starting with "Verified" (case-insensitive)
        cleaned_text = "\n".join(line for line in filtered_text.split("\n") if not line.strip().lower().startswith("verified"))

        # Clean the text: remove non-printing characters, extra spaces, and control characters
        cleaned_text = re.sub(r'\u000d', ' ', cleaned_text)  # Collapsing multiple spaces into one
        cleaned_text = re.sub(r'\u000a', '\n', cleaned_text)  # Collapsing multiple spaces into one
        cleaned_text = re.sub(r'  ', ' ', cleaned_text)  # Collapsing multiple spaces into one
        cleaned_text = cleaned_text.strip()  # Remove leading/trailing whitespace
      

        text += cleaned_text + "\n"

    return text, "\n".join(clipped_text)

def process_pdfs_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        
        try:
            extracted_text, clipped_text = extract_text_from_pdf(pdf_path)
            
            if not extracted_text:
                logging.warning(f"Skipping {pdf_file} due to extraction failure.")
                continue

            output_txt_file = os.path.join(output_folder, f"{os.path.splitext(pdf_file)[0]}.txt")
            with open(output_txt_file, "w", encoding="utf-8") as text_file:
                text_file.write(extracted_text)

            output_clipped_txt_file = os.path.join(output_folder, f"{os.path.splitext(pdf_file)[0]}_trims.txt")
            with open(output_clipped_txt_file, "w", encoding="utf-8") as clipped_file:
                clipped_file.write(clipped_text)

            logging.info(f"Extracted text from {pdf_file} and saved to {output_txt_file}")
            logging.info(f"Clipped text from {pdf_file} saved to {output_clipped_txt_file}")
            
            print(f"Processed {pdf_file}.")
        except Exception as e:
            logging.error(f"Error processing {pdf_file}: {e}")
            print(f"Failed to process {pdf_file}.")

        print("\nWaiting 0.5 sec...\n")
        time.sleep(0.5)

# Define the input and output folders
input_folder = "D:/Documents/R_code/pdf_files"
output_folder = "D:/Documents/R_code/pdf_files/extracted_text_files"

# Process the PDFs
process_pdfs_in_folder(input_folder, output_folder)
