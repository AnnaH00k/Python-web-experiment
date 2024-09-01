# python-scripts/pdf_merger.py

from PyPDF2 import PdfMerger
import sys

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    pdf_list = sys.argv[1:-1]
    output_path = sys.argv[-1]
    merge_pdfs(pdf_list, output_path)
