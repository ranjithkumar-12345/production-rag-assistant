from  pathlib import Path
import PyPDF2
import docx
from bs4 import BeautifulSoup
from typing import Dict,Any,List


def read_pdf(file_path):
    text = ""
    try:
        with open(file_path,"rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text+=extracted +"\n"

    except Exception as e:
        print(f"if we find in (file_path)in errors:{e}")
    return  text.strip()

def read_docx(file_path):
    text = ""
    try:
        reader = docx.Document(file_path)
        for para in reader.paras:
            extracted = para.extract_text()
            if para.extract_text:
                text+=para.extract_text +"\n"

    except Exception as e:
        print(f"if we find in (file_path)in errors:{e}")
    return text.strip()

def read_txt(file_path):
    try:
        with open(file_path,"r",errors ="ignore",encoding="utf-8") as file:
            return file.read().strip()

    except Exception as e:
        print(f"if we find in (file_path)in errors:{e}")
        return ""

def read_html(file_path):
    text=""

    try:
        with open(file_path,"rb",errors ="ignore",encoding="utf-8") as file:
            html =file.read
            soup = BeautifulSoup(html,"html.parser")

        for script_for_style in soup(["script","style"]):
            script_for_style.decompose()
            return soup.get_text(separator="\n", strip=True)
    except Exception as e:
        print(f"if we find in (file_path)in errors:{e}")
        return ""


if __name__ == "__main__":

    file_path = read_pdf(r"C:\Users\hp\Downloads\Great.pdf")
    print(file_path[:1000])

    sample_pdf = read_txt(r"C:\Users\hp\Downloads\Document.txt")
    print(sample_pdf[:2000])
