#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 214. Exercise: PDF Merger

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
        print("Program to combine PDFs. Provide two or more pdf files.")
        print("Output will be in file1_.pdf")
        print(f"Run it as: python '{script_name.name}' file1.pdf file2.pdf <file3.pdf>")
        os._exit(1)
    for pdf in inp[1:]:
        if (pathlib.Path(pdf).suffix) != ".pdf":
            print(f"All files should have .pdf extension. Check '{pdf}' file")
            os._exit(1)
        if not (pathlib.Path(pdf).exists()):
            print(f"Couldn't find '{pdf}' file")
            os._exit(1)
            

def pdf_combiner(pdf_list):

    # adding '_' to the first pdf. This should be simplier!!!!!
    pdf1 = pdf_list[0]
    pdf1_path=pathlib.Path(pdf1).parents[0]
    pdf1_name=pathlib.Path(pdf1).stem
    pdf1_ext=pathlib.Path(pdf1).suffix
    combined_pdf = pathlib.Path.joinpath(pdf1_path, pdf1_name+"_"+pdf1_ext)
    print(f"Combined PDF will be in the file '{combined_pdf}' ")
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(f"adding '{pdf}' ... ")
        merger.append(pdf)

    merger.write(str(combined_pdf))

inputs = sys.argv
check_inputs(inputs)

pdfs=sys.argv[1:]
pdf_combiner(pdfs)
