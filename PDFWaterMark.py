import PyPDF2

template=PyPDF2.PdfFileReader(open("super.pdf", 'rb'))
template.numPages