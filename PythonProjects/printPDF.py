#! /usr/bin/env python
import sys
import PyPDF2

if len(sys.argv) == 0:
    # If no paramters passed
    print("No paramters passed. No PDF to print.")

if len(sys.argv) > 0:
    # Sets parameters passed to string value
    myPDF = str(sys.argv[1])

    # Error checking
    if (str(myPDF[-4:]) != ".pdf"):
        print("File extension not of correct type. PDFs only please")

    else:
        # Prints pdf 
        print("Printing PDF text from: " + myPDF)
        pdf_file = open(myPDF, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages

        for page in range(num_pages):
            text = pdf_reader.getPage(page)
            print(text.extractText())
