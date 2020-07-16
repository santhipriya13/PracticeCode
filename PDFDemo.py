import PyPDF2
with open("twopage.pdf",'rb') as file:
 print(file)
# print(dir(PyPDF2))
 #print(dir(PyPDF2.PdfFileReader))

 reader=PyPDF2.PdfFileReader(file)
 page=reader.getPage(0)
 print(page.rotateCounterClockwise(180))
 print(reader.numPages)
 writer=PyPDF2.PdfFileWriter()
 writer.addPage(page)
 with open("tilt.pdf", 'wb') as newfile:
  writer.write(newfile)