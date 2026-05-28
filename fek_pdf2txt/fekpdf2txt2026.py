# ------------------------------------- #
#          Developed/Edited by:         #
#           Lampros KAFIDAS             #
# https://www.linkedin.com/in/kafidas/  #
#      https://github.com/kafidas       #
# ------------------------------------- #

###### Python code for extracting readable text from pdf files of et.gr (edition 2026-05)
###### Tested for Issues A' that contain formal laws (no decrees etc)
###### Known issues: Annex handling, line breaks on page breaks

import sys
import pymupdf.layout
import pymupdf4llm


pdf_file = sys.argv[1]
doc = pymupdf.open(pdf_file)

# Crop pages for content extraction
header_crop = 74
footer_crop = 9
first_page_top = 150
first_page_bottom = 9
last_page_top = 74    
last_page_bottom = 63

for page_num, page in enumerate(doc):
    rect = page.rect
    
    if page_num == 0:  # First page
        top_crop = first_page_top
        bottom_crop = first_page_bottom
    elif page_num == len(doc) - 1:  # Last page
        top_crop = last_page_top
        bottom_crop = last_page_bottom
    else:  # Middle pages
        top_crop = header_crop
        bottom_crop = footer_crop
    
    page.set_cropbox((rect.x0, rect.y0 + top_crop, rect.x1, rect.y1 - bottom_crop))

cropped_doc = "cropped_temp.pdf"
doc.save(cropped_doc)
doc.close()

# Main conversion
txt_out = pymupdf4llm.to_text(cropped_doc, use_ocr=True, ocr_language="ell", show_progress=True)

# Post-processing cleaning
def merge_lines_if_hyphen(text):
    text = text + '\n'
    lines = text.split('\n')
    merged = []
    i = 0
    while i < len(lines):
        current_line = lines[i].rstrip()
        
        while current_line.endswith('-') and not current_line.endswith(' -'):
            if i + 1 < len(lines):
                next_line = lines[i + 1].lstrip()
                one_more_line = lines[i + 2].lstrip()
                current_line = current_line[:-1] + next_line + one_more_line
                i += 2
            else:
                break
        
        merged.append(current_line)
        i += 1
    
    return merged

# Process hyphenated line breaks
lines = merge_lines_if_hyphen(txt_out)
non_empty_lines = [line for line in lines if line.strip()]
txt_out = '\n'.join(non_empty_lines)

# Remove everything after last signature
def truncate_after_phrase(text, phrase="επί της Δικαιοσύνης Υπουργός", keep_lines_after=1):
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        if phrase in line:
            # Keep up to the phrase line + keep_lines_after lines
            lines = lines[:i + keep_lines_after + 1]  # +1 because we want to keep the line with phrase too
            break
    
    return '\n'.join(lines)

txt_out = truncate_after_phrase(txt_out)

# Create output text file
output_file = pdf_file.replace('.pdf', '.txt')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(txt_out)

print(f"\nConverted {pdf_file}")
