
import PyPDF2
from split_string import split_string
from api import get_response



 


numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
"""
Uses chat-gpt api to generate a page of good questions and answers
"""

def open_file(file_name):
    with open(file_name, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfReader(pdf_file)
        page = read_pdf.pages[1]
        page_content = page.extract_text()
        return page_content


def main() -> None:
 
    
    file_name = "topic2.pdf"
    file = open_file(file_name)
    list_of_strings = split_string(file)
    print(get_response(list_of_strings))


main()