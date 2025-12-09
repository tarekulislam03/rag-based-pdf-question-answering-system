from pypdf import PdfReader
import json


def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text_lists = []
    for page in reader.pages:
        text_lists.append(page.extract_text())
    return(text_lists)
        