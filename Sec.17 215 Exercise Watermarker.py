#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 215. Exercise: Watermarker

# Program to combine PDFs

# https://pypi.org/project/PyPDF2/
# https://pythonhosted.org/PyPDF2/index.html


import PyPDF2

import sys
import os
import pathlib

def check_inputs(inp):
    """
    Check if two or more arguments were provided
    """
    if len(inp) < 3:
        script_name = pathlib.Path(str(inp[0]))
        print("Program to add watermark on PDFs. Provide two or more pdf files.")
        print(f"Run it as: python '{script_name.name}' FileToApplyWatermark.pdf Watermark.pdf")
        os._exit(1)
    for pdf in inp[1:]:
        if (pathlib.Path(pdf).suffix) != ".pdf":
            print(f"All files should have .pdf extension. Check '{pdf}' file")
            os._exit(1)
        if not (pathlib.Path(pdf).exists()):
            print(f"Couldn't find '{pdf}' file")
            os._exit(1)
            



def pdf_watermark(pdf_file, watermark):

    # adding '_' to the first pdf. This should be simplier!!!!!
    pdf1 = pdf_file
    pdf1_path=pathlib.Path(pdf1).parents[0]
    pdf1_name=pathlib.Path(pdf1).stem
    pdf1_ext=pathlib.Path(pdf1).suffix
    combined_pdf_path = pathlib.Path.joinpath(pdf1_path, pdf1_name+"_"+pdf1_ext)
    print(f"File with watermark will be in the file '{combined_pdf_path}' ")
    
    watermarkFile = PyPDF2.PdfFileReader(open(watermark, 'rb'))
    watermarkPage = watermarkFile.getPage(0)
    pdfFile = PyPDF2.PdfFileReader(open(pdf_file, 'rb'))
    output = PyPDF2.PdfFileWriter()

    for pageNum in range(pdfFile.getNumPages()):
        page = pdfFile.getPage(pageNum)
        page.mergePage(watermarkPage)
        output.addPage(page)

    with open(combined_pdf_path, 'wb') as combined_pdf:
        output.write(combined_pdf)
        

inputs = sys.argv
check_inputs(inputs)

pdf_watermark(inputs[1], inputs[2])
