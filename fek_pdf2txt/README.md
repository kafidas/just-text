# PDF to Text Extractor for Greek Legal Documents (ET.GR)

Python tool for extracting clean text from Greek government gazette PDFs (ET.GR Issue A').

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyMuPDF](https://img.shields.io/badge/PyMuPDF-1.24+-orange.svg)](https://pymupdf.readthedocs.io/)


## ✨ Features

- **Intelligent Page Cropping** - Automatically removes headers and footers with different margins for first, middle, and last pages
- **OCR Support** - Uses OCR (Greek language) to extract text from scanned documents
- **Hyphenation Handling** - Intelligently merges hyphenated words broken across lines
- **Content Truncation** - Automatically removes content after the Minister of Justice signature
- **Greek Language Optimized** - Specifically tuned for Greek legal terminology and document structure
- **Clean Output** - Removes blank lines and produces clean, readable text files

## ⚠️ Known Issues

- **Annex Handling** - Needs imporvement
- **Line Breaks on Page Breaks** - Some line breaks in output from page to page transition
- **Horizontal elements** - Checks on horizontal pages and tables

## Installation

pip install pymupdf pymupdf4llm

Tesseract OCR required (for scanned PDFs):
- Ubuntu/Debian: sudo apt-get install tesseract-ocr tesseract-ocr-ell
- Windows: Download from UB-Mannheim/tesseract
- macOS: brew install tesseract tesseract-lang

## Usage

python script.py document.pdf

Output: document.txt in same directory

## How It Works

1. Crops each page (different margins for first/middle/last pages)
2. Extracts text with Greek OCR
3. Merges hyphenated words (e.g., Κυβερνή- + σεως -> Κυβερνήσεως)
4. Removes everything after "επί της Δικαιοσύνης Υπουργός"
5. Strips blank lines and saves as .txt

## Troubleshooting

OCR not working? Check Greek language support:

tesseract --list-langs | grep ell



## 🤝 Contributing
Contributions are welcome! Here's how you can help:

Report bugs - Open an issue with detailed description

Suggest features - Share ideas for improvements

Submit PRs - Fix issues or add functionality

Improve documentation - Help make the README better



## 👨‍💻 Author
Lampros KAFIDAS

GitHub: https://github.com/kafidas

LinkedIn: https://www.linkedin.com/in/kafidas/
