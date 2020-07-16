import sys
import PyPDF2

inputs =sys.argv[1:]

print(inputs)

def PdfCombiner(PdfList):

    merger=PyPDF2.PdfFileMerger()
    for pdf in PdfList:
        merger.append(pdf)
    with open("super1.pdf", 'wb')as superpdf:
        merger.write(superpdf)

PdfCombiner(inputs)