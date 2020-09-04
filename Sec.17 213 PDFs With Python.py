#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 213. PDFs With Python

# https://pypi.org/project/PyPDF2/
# https://pythonhosted.org/PyPDF2/index.html

# pip install PyPDF2

import PyPDF2

with open('Sec.17 213 PDFs With Python/dummy.pdf', 'rb') as file1:
    # print(file)
    reader = PyPDF2.PdfFileReader(file1)
    print("reader.numPages: ", reader.numPages)
    print("reader.documentInfo: ", reader.documentInfo)
    print("reader.getPage(0): ", reader.getPage(0))
    page1 = reader.getPage(0)
    page1.rotateClockwise(90)
    
    writer=PyPDF2.PdfFileWriter()
    writer.addPage(page1)
    with open('Sec.17 213 PDFs With Python/dummy_rotated.pdf', 'wb') as file2:
        writer.write(file2)

