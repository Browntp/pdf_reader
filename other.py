"""
Uses chat-gpt api to generate a page of good questions and answers
"""

import PyPDF2
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


def open_file(file_name):
    with open(file_name, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfReader(pdf_file)
        page = read_pdf.pages[1]
        page_content = page.extract_text()
        print(page_content)


def main() -> None:
    file_name = "topic2.pdf"
    open_file(file_name)


main()