import PyPDF2
from split_string import split_string
from api import get_response
from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdfUpload' in request.files:
        pdf_file = request.files['pdfUpload']
        filename = secure_filename(pdf_file.filename)

        user_files_dir = os.path.join(app.root_path, 'user_files')  # Use app.root_path for relative path
        if not os.path.exists(user_files_dir):
            os.makedirs(user_files_dir)

        pdf_file.save(os.path.join(user_files_dir, filename))
        QandA = return_QA(filename)
        return render_template("output_questions.html", data=QandA)

 


numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
"""
Uses chat-gpt api to generate a page of good questions and answers
"""

def open_file(file_name):
    with open(file_name, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfReader(pdf_file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()
        return page_content


def return_QA(filename) -> None:
    
    file_name = f"./user_files/{filename}"
    file = open_file(file_name)
    list_of_strings = split_string(file)
    
    response = get_response(list_of_strings)
    
    return response


if __name__ == "__main__":
    
    app.run(debug=True)
    